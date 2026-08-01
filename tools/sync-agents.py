#!/usr/bin/env python3
"""Discover and check synchronization of Eyu agent materials."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CHINESE_PATTERN = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF]")
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class SyncPair:
    source: str
    target: str
    marker: str


@dataclass(frozen=True)
class SkillMetadata:
    name: str
    skill_target: str
    metadata_target: str
    marker: str


def marker_slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").upper()


def normalized_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def normalized_sha256(path: Path) -> str:
    return hashlib.sha256(normalized_text(path).encode("utf-8")).hexdigest()


def document_pairs(source_dir: str, target_dir: str, prefix: str) -> list[SyncPair]:
    root = REPO_ROOT / source_dir
    if not root.is_dir():
        return []
    return [
        SyncPair(
            source=source.relative_to(REPO_ROOT).as_posix(),
            target=f"{target_dir}/{source.name}",
            marker=f"{prefix}_{marker_slug(source.stem)}_ZH_CN_SHA256",
        )
        for source in sorted(root.glob("*.md"), key=lambda path: path.name)
    ]


def discover() -> tuple[list[SyncPair], list[SkillMetadata]]:
    pairs = [SyncPair("AGENTS.zh-CN.md", "AGENTS.md", "AGENTS_ZH_CN_SHA256")]
    pairs.extend(document_pairs("docs/agents/zh-CN", "docs/agents", "AGENT_DOCS"))
    pairs.extend(document_pairs("docs/tasks/zh-CN", "docs/tasks", "TASK_DOCS"))

    metadata: list[SkillMetadata] = []
    skills_root = REPO_ROOT / ".agents" / "skills"
    if skills_root.is_dir():
        for skill_dir in sorted((path for path in skills_root.iterdir() if path.is_dir()), key=lambda path: path.name):
            source = skill_dir / "SKILL.zh-CN.md"
            if not source.is_file():
                continue
            name = skill_dir.name
            skill_target = f".agents/skills/{name}/SKILL.md"
            pairs.append(
                SyncPair(
                    source=source.relative_to(REPO_ROOT).as_posix(),
                    target=skill_target,
                    marker=f"{marker_slug(name)}_SKILL_ZH_CN_SHA256",
                )
            )
            metadata.append(
                SkillMetadata(
                    name=name,
                    skill_target=skill_target,
                    metadata_target=f".agents/skills/{name}/agents/openai.yaml",
                    marker=f"{marker_slug(name)}_OPENAI_SKILL_MD_SHA256",
                )
            )
    return pairs, metadata


def marker_values(text: str, marker: str, yaml: bool = False) -> list[str]:
    if yaml:
        pattern = re.compile(rf"^# {re.escape(marker)}: ([^\s]+)$", re.MULTILINE)
    else:
        pattern = re.compile(rf"<!-- {re.escape(marker)}: ([^\s]+) -->")
    return pattern.findall(text)


def check_pair(pair: SyncPair) -> list[str]:
    source = REPO_ROOT / pair.source
    target = REPO_ROOT / pair.target
    if not source.is_file():
        return [f"Missing source file: {pair.source}"]
    if not target.is_file():
        return [f"{pair.target} is missing for {pair.source}."]

    target_text = normalized_text(target)
    values = marker_values(target_text, pair.marker)
    failures: list[str] = []
    if len(values) != 1:
        failures.append(f"{pair.target} must contain exactly one valid {pair.marker} marker.")
    elif not re.fullmatch(r"[a-fA-F0-9]{64}", values[0]):
        failures.append(f"{pair.target} has an invalid sync marker.")
    elif values[0].lower() != normalized_sha256(source):
        failures.append(f"{pair.target} has a stale source marker for {pair.source}.")
    if CHINESE_PATTERN.search(target_text):
        failures.append(f"{pair.target} still contains Chinese text.")
    return failures


def quoted_interface_value(text: str, field: str) -> list[str]:
    pattern = re.compile(rf'^  {re.escape(field)}: "([^"]*)"$', re.MULTILINE)
    return pattern.findall(text)


def check_skill_metadata(item: SkillMetadata) -> list[str]:
    failures: list[str] = []
    if not SKILL_NAME_PATTERN.fullmatch(item.name) or len(item.name) > 64:
        failures.append(f"Invalid skill directory name: {item.name}")

    skill = REPO_ROOT / item.skill_target
    metadata = REPO_ROOT / item.metadata_target
    if not skill.is_file():
        return failures
    if not metadata.is_file():
        return failures + [f"{item.metadata_target} is missing for {item.skill_target}."]

    skill_text = normalized_text(skill)
    name_values = re.findall(r"^name:\s*([^\s]+)\s*$", skill_text, re.MULTILINE)
    if name_values != [item.name]:
        failures.append(f"{item.skill_target} must declare skill name '{item.name}' exactly once.")

    metadata_text = normalized_text(metadata)
    values = marker_values(metadata_text, item.marker, yaml=True)
    if len(values) != 1 or not re.fullmatch(r"[a-fA-F0-9]{64}", values[0]):
        failures.append(f"{item.metadata_target} must contain exactly one valid {item.marker} marker.")
    elif values[0].lower() != normalized_sha256(skill):
        failures.append(f"{item.metadata_target} has a stale source marker for {item.skill_target}.")

    if metadata_text.count("interface:\n") != 1:
        failures.append(f"{item.metadata_target} must contain exactly one interface mapping.")
    for field in ("display_name", "short_description", "default_prompt"):
        field_values = quoted_interface_value(metadata_text, field)
        if len(field_values) != 1 or not field_values[0]:
            failures.append(f"{item.metadata_target} must contain one quoted non-empty {field} field.")
    descriptions = quoted_interface_value(metadata_text, "short_description")
    if len(descriptions) == 1 and not 25 <= len(descriptions[0]) <= 64:
        failures.append(f"{item.metadata_target} short_description must contain 25 to 64 characters.")
    prompts = quoted_interface_value(metadata_text, "default_prompt")
    if len(prompts) == 1 and f"${item.name}" not in prompts[0]:
        failures.append(f"{item.metadata_target} default_prompt must reference ${item.name}.")
    return failures


def discover_orphans(pairs: list[SyncPair], metadata: list[SkillMetadata]) -> list[str]:
    known = {pair.target for pair in pairs} | {item.metadata_target for item in metadata}
    candidates: list[Path] = []
    for directory in ("docs/agents", "docs/tasks"):
        root = REPO_ROOT / directory
        if root.is_dir():
            candidates.extend(path for path in root.glob("*.md") if path.is_file())
    skills_root = REPO_ROOT / ".agents" / "skills"
    if skills_root.is_dir():
        candidates.extend(path for path in skills_root.glob("*/SKILL.md") if path.is_file())
        candidates.extend(path for path in skills_root.glob("*/agents/openai.yaml") if path.is_file())
    return sorted(path.relative_to(REPO_ROOT).as_posix() for path in candidates if path.relative_to(REPO_ROOT).as_posix() not in known)


def run_check(pairs: list[SyncPair], metadata: list[SkillMetadata]) -> int:
    failures = [failure for pair in pairs for failure in check_pair(pair)]
    failures.extend(failure for item in metadata for failure in check_skill_metadata(item))
    failures.extend(f"{path} has no matching source file." for path in discover_orphans(pairs, metadata))
    if failures:
        print("Agent synchronization check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("All discovered English agent files and skill metadata pass synchronization checks.")
    return 0


def print_prompt(pairs: list[SyncPair], metadata: list[SkillMetadata]) -> None:
    print("Synchronize English agent files from their Chinese sources.\n")
    print("Required markers:")
    for pair in pairs:
        print(f"- {pair.target}: <!-- {pair.marker}: {normalized_sha256(REPO_ROOT / pair.source)} -->")
    for item in metadata:
        skill = REPO_ROOT / item.skill_target
        if skill.is_file():
            print(f"- {item.metadata_target}: # {item.marker}: {normalized_sha256(skill)}")
    print("\nAfter editing, run: python3 ./tools/sync-agents.py --check")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--prompt", action="store_true")
    args = parser.parse_args()
    pairs, metadata = discover()
    if args.check:
        return run_check(pairs, metadata)
    print_prompt(pairs, metadata)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

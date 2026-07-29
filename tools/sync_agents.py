#!/usr/bin/env python3
"""Check Chinese-source and English AI-file synchronization.

The script never modifies files. Without --check it prints a synchronization
prompt containing every discovered pair and the current normalized source hash.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CHINESE_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


@dataclass(frozen=True)
class SyncPair:
    source: Path
    target: Path
    marker: str
    label: str


@dataclass(frozen=True)
class SyncState:
    pair: SyncPair
    source_hash: str
    target_exists: bool
    marker_count: int
    stored_hash: str
    contains_chinese: bool

    @property
    def in_sync(self) -> bool:
        return (
            self.target_exists
            and self.marker_count == 1
            and self.stored_hash == self.source_hash
            and not self.contains_chinese
        )


def marker_slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").upper()


def normalized_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")


def normalized_sha256(path: Path) -> str:
    return hashlib.sha256(normalized_text(path).encode("utf-8")).hexdigest()


def document_pairs(
    source_dir: str,
    target_dir: str,
    marker_prefix: str,
    label_prefix: str,
) -> list[SyncPair]:
    root = REPO_ROOT / source_dir
    if not root.exists():
        return []

    return [
        SyncPair(
            source=source.relative_to(REPO_ROOT),
            target=Path(target_dir) / source.name,
            marker=f"{marker_prefix}_{marker_slug(source.stem)}_ZH_CN_SHA256",
            label=f"{label_prefix} {source.stem}",
        )
        for source in sorted(root.glob("*.md"))
    ]


def skill_pairs() -> list[SyncPair]:
    root = REPO_ROOT / ".agents" / "skills"
    if not root.exists():
        return []

    pairs: list[SyncPair] = []
    for skill_dir in sorted(path for path in root.iterdir() if path.is_dir()):
        source = skill_dir / "SKILL.zh-CN.md"
        if source.exists():
            pairs.append(
                SyncPair(
                    source=source.relative_to(REPO_ROOT),
                    target=(skill_dir / "SKILL.md").relative_to(REPO_ROOT),
                    marker=f"{marker_slug(skill_dir.name)}_SKILL_ZH_CN_SHA256",
                    label=f"skill {skill_dir.name}",
                )
            )
    return pairs


def discover_pairs() -> list[SyncPair]:
    pairs = [
        SyncPair(
            source=Path("AGENTS.zh-CN.md"),
            target=Path("AGENTS.md"),
            marker="AGENTS_ZH_CN_SHA256",
            label="root AGENTS",
        )
    ]
    pairs.extend(document_pairs("docs/agents/zh-CN", "docs/agents", "AGENT_DOCS", "agent context"))
    pairs.extend(document_pairs("docs/tasks/zh-CN", "docs/tasks", "TASK_DOCS", "task document"))
    pairs.extend(skill_pairs())
    return pairs


def discover_orphans(known_targets: set[Path]) -> list[Path]:
    candidates: list[Path] = []
    for directory in (Path("docs/agents"), Path("docs/tasks")):
        root = REPO_ROOT / directory
        if root.exists():
            candidates.extend(path.relative_to(REPO_ROOT) for path in root.glob("*.md"))

    skills_root = REPO_ROOT / ".agents" / "skills"
    if skills_root.exists():
        candidates.extend(
            target.relative_to(REPO_ROOT)
            for target in skills_root.glob("*/SKILL.md")
        )

    return sorted(path for path in candidates if path not in known_targets)


def sync_state(pair: SyncPair) -> SyncState:
    source = REPO_ROOT / pair.source
    target = REPO_ROOT / pair.target
    if not source.exists():
        raise FileNotFoundError(f"Missing source file: {pair.source}")

    source_hash = normalized_sha256(source)
    target_exists = target.exists()
    target_text = normalized_text(target) if target_exists else ""
    marker_pattern = re.compile(
        rf"<!-- {re.escape(pair.marker)}: ([a-fA-F0-9]{{64}}) -->"
    )
    marker_matches = marker_pattern.findall(target_text)

    return SyncState(
        pair=pair,
        source_hash=source_hash,
        target_exists=target_exists,
        marker_count=len(marker_matches),
        stored_hash=marker_matches[0].lower() if len(marker_matches) == 1 else "",
        contains_chinese=bool(CHINESE_PATTERN.search(target_text)),
    )


def run_check(states: list[SyncState], orphans: list[Path]) -> int:
    failed = [state for state in states if not state.in_sync]
    for state in failed:
        pair = state.pair
        if not state.target_exists:
            print(f"{pair.target} is missing for {pair.source}.")
            continue
        if state.marker_count == 0:
            print(f"{pair.target} has no valid sync marker for {pair.source}.")
        elif state.marker_count > 1:
            print(f"{pair.target} has duplicate sync markers for {pair.source}.")
        elif state.stored_hash != state.source_hash:
            print(f"{pair.target} has a stale source marker for {pair.source}.")
            print(f"Stored hash:  {state.stored_hash}")
            print(f"Current hash: {state.source_hash}")
        if state.contains_chinese:
            print(f"{pair.target} still contains Chinese text.")

    for orphan in orphans:
        print(f"{orphan} has no matching Chinese source file.")

    if failed or orphans:
        return 1

    print(
        "All discovered English agent files have current source markers "
        "and pass English-content checks."
    )
    return 0


def print_prompt(states: list[SyncState], orphans: list[Path]) -> None:
    print("Synchronize the English AI-facing files from their Chinese source files.\n")
    print("Rules:")
    print("- Treat Chinese files as the source of truth.")
    print("- Keep English concise, direct, and free of untranslated Chinese text.")
    print("- Preserve commands, paths, warnings, validation rules, and forbidden actions.")
    print("- Add or update exactly one matching marker in each English file:")
    for state in states:
        print(
            f"- {state.pair.target}: "
            f"<!-- {state.pair.marker}: {state.source_hash} -->"
        )
    print("- Do not modify Chinese source files unless explicitly asked.")
    print("- Do not create .agents/skills/*/zh-CN/SKILL.md.\n")
    print("Pairs:")
    for state in states:
        print(f"- {state.pair.source} -> {state.pair.target}")
    if orphans:
        print("\nOrphaned English files to resolve:")
        for orphan in orphans:
            print(f"- {orphan}")
    print("\nAfter editing, run:")
    print("python3 ./tools/sync_agents.py --check")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check all discovered pairs")
    args = parser.parse_args()

    pairs = discover_pairs()
    states = [sync_state(pair) for pair in pairs]
    orphans = discover_orphans({pair.target for pair in pairs})
    if args.check:
        return run_check(states, orphans)

    print_prompt(states, orphans)
    return 0


if __name__ == "__main__":
    sys.exit(main())

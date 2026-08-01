#!/usr/bin/env python3
"""Validate Eyu pull-request and commit subjects."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass


ALLOWED_TYPES = ("feat", "fix", "refactor", "perf", "docs", "test", "build", "ci", "style", "chore", "revert")
TYPE_PATTERN = "|".join(ALLOWED_TYPES)
SUBJECT_PATTERN = re.compile(
    rf"^(?P<type>{TYPE_PATTERN})(?:\((?P<scope>[a-z0-9]+(?:-[a-z0-9]+)*)\))?"
    r"(?P<breaking>!)?: (?P<description>\S.*)$"
)
CHINESE_PATTERN = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF]")
WIP_PATTERN = re.compile(r"^(?:wip|chore\(wip\))!?:", re.IGNORECASE)


@dataclass(frozen=True)
class CommitSubject:
    sha: str
    subject: str


def validation_error(subject: str) -> str | None:
    if WIP_PATTERN.match(subject):
        return "WIP commits are local checkpoints and cannot be published"
    match = SUBJECT_PATTERN.fullmatch(subject)
    if match is None:
        return "expected '<type>(<scope>)!: <Chinese description>'"
    if not CHINESE_PATTERN.search(match.group("description")):
        return "description must contain at least one Chinese character"
    return None


def read_commit_subjects(base: str, head: str) -> list[CommitSubject]:
    try:
        result = subprocess.run(
            ["git", "log", "--no-merges", "--format=%H%x00%s", f"{base}..{head}"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() or error.stdout.strip() or "git log failed"
        raise RuntimeError(detail) from error
    commits: list[CommitSubject] = []
    for line in result.stdout.splitlines():
        if line:
            sha, separator, subject = line.partition("\0")
            if not separator:
                raise RuntimeError(f"Unexpected git log output: {line}")
            commits.append(CommitSubject(sha, subject))
    return commits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()
    failures: list[str] = []
    if error := validation_error(args.title):
        failures.append(f"PR title '{args.title}': {error}")
    try:
        commits = read_commit_subjects(args.base, args.head)
    except RuntimeError as error:
        print(f"Unable to inspect commit subjects: {error}", file=sys.stderr)
        return 2
    if not commits:
        failures.append(f"No non-merge commits found in {args.base}..{args.head}")
    for commit in commits:
        if error := validation_error(commit.subject):
            failures.append(f"Commit {commit.sha[:12]} '{commit.subject}': {error}")
    if failures:
        print("PR policy check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"PR title and {len(commits)} non-merge commit subject(s) pass Eyu policy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

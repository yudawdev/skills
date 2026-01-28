#!/usr/bin/env python3
"""Suggest a git branch name from a short summary."""

import argparse
import datetime
import re


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest a branch name.")
    parser.add_argument("summary", nargs="*", help="Short summary for branch name")
    parser.add_argument("--type", default="feature", help="Branch type prefix")
    parser.add_argument("--date", action="store_true", help="Append YYYY-MM-DD")
    args = parser.parse_args()

    summary = " ".join(args.summary).strip()
    if not summary:
        summary = "new-change"

    prefix = args.type.strip().lower().rstrip("/")
    slug = slugify(summary) or "new-change"

    if args.date:
        today = datetime.date.today().isoformat()
        slug = f"{slug}-{today}"

    # Keep it reasonably short
    slug = slug[:50].rstrip("-")

    print(f"{prefix}/{slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

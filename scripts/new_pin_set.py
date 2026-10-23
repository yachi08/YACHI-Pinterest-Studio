#!/usr/bin/env python3
"""Create a new YACHI Pinterest Studio pin-set workspace without overwriting data."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def safe_name(value: str) -> str:
    value = value.strip().replace("/", "-").replace("\\", "-")
    value = re.sub(r"[\x00-\x1f:*?\"<>|]", "-", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-. ")
    return value[:80] or "new-pin-set"


def main() -> int:
    parser = argparse.ArgumentParser(description="新しいピン企画フォルダを作成します。")
    parser.add_argument("name", help="企画フォルダ名")
    parser.add_argument("--theme", default="", help="企画テーマ")
    args = parser.parse_args()

    project = Path(__file__).resolve().parent.parent
    template = project / "templates" / "pin_set"
    destination = project / "pins" / safe_name(args.name)

    if destination.exists():
        print(f"ERROR: 既に存在します: {destination}", file=sys.stderr)
        return 2

    shutil.copytree(template, destination)
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    status = {
        "pin_set_name": args.name.strip(),
        "theme": args.theme.strip(),
        "status": "idea",
        "created_at": now,
        "updated_at": now,
        "approvals": {
            "material_scope": {"approved": None, "approved_at": None},
            "package": {"approved": False, "approved_at": None},
        },
        "pins": [],
    }
    (destination / "status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    brief = destination / "00_brief.md"
    brief.write_text(
        "# ピン企画\n\n"
        f"- 企画名: {args.name.strip()}\n"
        f"- テーマ: {args.theme.strip() or '未設定'}\n"
        "- 狙う読者:\n- 誘導先:\n- 社長がこのテーマを選んだ理由:\n",
        encoding="utf-8",
    )
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

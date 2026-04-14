from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"

EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".obsidian",
    "site",
    "docs",
    ".vscode",
    "memories",
    "scripts",
}


def main() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    for source in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in source.relative_to(ROOT).parts):
            continue
        if source.name == "README.md":
            continue
        destination = DOCS_DIR / source.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


if __name__ == "__main__":
    main()
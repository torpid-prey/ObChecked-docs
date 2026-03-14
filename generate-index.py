from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "docs-index.md"

INCLUDE_EXTENSIONS = {
    ".md",
    ".aud",
    ".json",
    ".png",
}

EXCLUDE_FILES = {
    ".gitkeep",
    "docs-index.md",
    "_template.md",
    "generate_docs_index.py",
}

EXCLUDE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".vscode",
}

TYPE_LABELS = {
    ".md": "Doc",
    ".aud": "Audit File",
    ".json": "Config",
    ".png": "Image",
}


def should_exclude(path: Path) -> bool:
    if path.name in EXCLUDE_FILES:
        return True

    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True

    return False


def nice_title(path: Path) -> str:
    stem = path.stem.replace("-", " ").replace("_", " ").strip()
    title = stem.title()

    label = TYPE_LABELS.get(path.suffix.lower(), "")
    if label:
        return f"{title} ({label})"
    return title


def group_files(files: list[Path]) -> dict[str, dict[str, list[Path]]]:
    grouped: dict[str, dict[str, list[Path]]] = {}

    for path in files:
        parts = path.parts

        if len(parts) == 1:
            top_group = "Root"
            sub_group = ""
        elif len(parts) == 2:
            top_group = parts[0]
            sub_group = ""
        else:
            top_group = parts[0]
            sub_group = parts[1]

        grouped.setdefault(top_group, {})
        grouped[top_group].setdefault(sub_group, [])
        grouped[top_group][sub_group].append(path)

    return grouped


def sort_key(path: Path):
    return (path.suffix.lower(), path.as_posix().lower())


def write_index() -> None:
    files = [
        path.relative_to(ROOT)
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in INCLUDE_EXTENSIONS
        and not should_exclude(path.relative_to(ROOT))
    ]

    files.sort(key=lambda p: p.as_posix().lower())
    grouped = group_files(files)

    lines: list[str] = []
    lines.append("# Repository Index")
    lines.append("")
    lines.append("This page lists documentation, configuration, audit files, and screenshots in the repository.")
    lines.append("")

    for top_group in sorted(grouped.keys(), key=str.lower):
        lines.append(f"## {top_group.replace('-', ' ').replace('_', ' ').title()}")
        lines.append("")

        subgroups = grouped[top_group]

        if "" in subgroups:
            for file_path in sorted(subgroups[""], key=sort_key):
                rel = file_path.as_posix()
                title = nice_title(file_path)
                lines.append(f"- [{title}]({rel})")
            lines.append("")

        for sub_group in sorted((k for k in subgroups.keys() if k != ""), key=str.lower):
            lines.append(f"### {sub_group.replace('-', ' ').replace('_', ' ').title()}")
            lines.append("")

            for file_path in sorted(subgroups[sub_group], key=sort_key):
                rel = file_path.as_posix()
                title = nice_title(file_path)
                lines.append(f"- [{title}]({rel})")

            lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Working in: {ROOT}")
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    write_index()
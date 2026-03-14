from pathlib import Path

ROOT = Path(".")
OUTPUT = ROOT / "docs-index.md"

# Files to exclude from the generated index
EXCLUDE_FILES = {
    ".gitkeep",
    "docs-index.md",
}

# Folders to exclude if needed
EXCLUDE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
}


def should_exclude(path: Path) -> bool:
    if path.name in EXCLUDE_FILES:
        return True

    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True

    return False


def title_from_name(path: Path) -> str:
    name = path.stem.replace("-", " ").replace("_", " ")
    return name.title()


def build_tree(paths):
    tree = {}
    for path in paths:
        parts = path.parts
        current = tree
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current.setdefault("__files__", []).append(path)
    return tree


def render_tree(tree, base: Path, depth: int = 0) -> list[str]:
    lines = []
    indent = "  " * depth

    dirs = sorted(k for k in tree.keys() if k != "__files__")
    files = sorted(tree.get("__files__", []))

    for directory in dirs:
        lines.append(f"{indent}- **{directory}/**")
        lines.extend(render_tree(tree[directory], base, depth + 1))

    for file_path in files:
        rel = file_path.as_posix()
        title = title_from_name(file_path)
        lines.append(f'{indent}- [{title}]({rel})')

    return lines


def main():
    md_files = [
        path.relative_to(ROOT)
        for path in ROOT.rglob("*.md")
        if path.is_file() and not should_exclude(path.relative_to(ROOT))
    ]

    md_files.sort()

    tree = build_tree(md_files)

    lines = [
        "# Documentation Index",
        "",
        "This page lists all Markdown documentation files in the repository.",
        "",
    ]

    lines.extend(render_tree(tree, ROOT))
    lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()

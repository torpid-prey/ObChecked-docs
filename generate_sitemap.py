from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "sitemap.xml"

SITE_BASE = "https://torpid-prey.github.io/ObChecked-docs/"

INCLUDE_EXTENSIONS = {".md"}

EXCLUDE_FILES = {
    ".gitkeep",
    "_template.md",
    "generate_docs_index.py",
    "generate_sitemap.py",
    "google4ea0181efa2e0b16.html",
    "robots.txt",
    "sitemap.xml",
    "_config.yml",
}

EXCLUDE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".vscode",
}


def should_exclude(path: Path) -> bool:
    if path.name in EXCLUDE_FILES:
        return True

    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True

    return False


def path_to_url(rel_path: Path) -> str:
    """
    Convert a markdown file path into a GitHub Pages URL.
    Removes the .md extension.
    """

    url_path = rel_path.as_posix()[:-3]

    return SITE_BASE + url_path


def collect_urls() -> list[str]:
    md_files = [
        path.relative_to(ROOT)
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in INCLUDE_EXTENSIONS
        and not should_exclude(path.relative_to(ROOT))
    ]

    urls = []

    for rel_path in sorted(md_files, key=lambda p: p.as_posix().lower()):
        urls.append(path_to_url(rel_path))

    return urls


def write_sitemap(urls: list[str]) -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    for url in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(url)}</loc>")
        lines.append("  </url>")

    lines.append("</urlset>")
    lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    urls = collect_urls()
    write_sitemap(urls)

    print(f"Working in: {ROOT}")
    print(f"Generated: {OUTPUT}")
    print(f"URLs written: {len(urls)}")


if __name__ == "__main__":
    main()
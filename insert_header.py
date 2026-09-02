#!/usr/bin/env python3
"""Insert the shared radio-astro-tools site header into rendered notebook pages.

Run after nbconvert has exported the notebooks to HTML and they have been
copied into docs/, so that each rendered notebook page carries the same top
navigation bar as https://radio-astro-tools.github.io/tutorials/.
"""
import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent / "docs"
HEADER_FILE = DOCS_DIR / "_header.html"

# index.html already has the header baked in; _header.html is the include itself.
SKIP = {"index.html", HEADER_FILE.name}

HEAD_RESOURCES = """
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400italic,400,700' rel='stylesheet' type='text/css' />
<link rel="stylesheet" type="text/css" href="css/style.css" />
<link rel="stylesheet" type="text/css" href="css/jquery.sidr.light.css" />
<script src="js/analytics.js"></script>
</head>"""

BODY_TAG_RE = re.compile(r"(<body[^>]*>)", re.IGNORECASE)


def inject(path: Path, header_html: str) -> bool:
    html = path.read_text(encoding="utf-8")

    if 'id="wrapper"' in html:
        return False  # header already present

    html = html.replace("</head>", HEAD_RESOURCES, 1)
    html, n = BODY_TAG_RE.subn(lambda m: m.group(1) + header_html, html, count=1)
    if n == 0:
        print(f"warning: no <body> tag found in {path}", file=sys.stderr)
        return False

    path.write_text(html, encoding="utf-8")
    return True


def main() -> None:
    header_html = HEADER_FILE.read_text(encoding="utf-8")
    targets = sorted(p for p in DOCS_DIR.glob("*.html") if p.name not in SKIP)

    if not targets:
        print("No rendered notebook pages found in docs/", file=sys.stderr)
        return

    for path in targets:
        if inject(path, header_html):
            print(f"Inserted header into {path.relative_to(DOCS_DIR.parent)}")


if __name__ == "__main__":
    main()

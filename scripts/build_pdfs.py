#!/usr/bin/env python3
"""Converte Markdown com MathJax/LaTeX e diagramas Mermaid para PDF."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = ("CFG", "CGA", "CGE", "INTRODUÇÃO")
MERMAID = re.compile(r"```mermaid\s*\n(.*?)\n```", re.S)


def convert(source: Path) -> None:
    try:
        text = source.read_text(encoding="utf-8")
    except OSError:
        print(f"SKIP {source.relative_to(ROOT)}", file=sys.stderr)
        return
    diagrams = list(MERMAID.finditer(text))
    with tempfile.TemporaryDirectory(prefix="md-pdf-") as tmpdir:
        temp = Path(tmpdir)
        for number, match in enumerate(diagrams, 1):
            mmd = temp / f"diagram-{number}.mmd"
            png = temp / f"diagram-{number}.png"
            mmd.write_text(match.group(1), encoding="utf-8")
            subprocess.run(["mmdc", "-i", str(mmd), "-o", str(png), "-b", "transparent"], check=True)
            text = text.replace(match.group(0), f"![Diagrama {number}]({png.as_posix()})", 1)
        intermediate = temp / source.name
        intermediate.write_text(text, encoding="utf-8")
        output = source.with_suffix(".pdf")
        subprocess.run([
            "pandoc", str(intermediate), "--from=markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables",
            "--standalone", "--pdf-engine=lualatex", "--variable=geometry:margin=2cm",
            "--variable=mainfont:Latin Modern Roman", "--output", str(output)
        ], cwd=ROOT, check=True)
        print(f"OK {output.relative_to(ROOT)}")


def main() -> int:
    if shutil.which("pandoc") is None or shutil.which("lualatex") is None:
        print("Instale pandoc e lualatex.", file=sys.stderr)
        return 2
    if len(sys.argv) > 1:
        paths = [ROOT / arg for arg in sys.argv[1:]]
    else:
        paths = [p for d in TARGET_DIRS for p in (ROOT / d).rglob("*.md") if p.name != "README.md"]
    paths = [p for p in paths if p.is_file() and "node_modules" not in p.parts]
    if any("```mermaid" in p.read_text(encoding="utf-8") for p in paths) and shutil.which("mmdc") is None:
        print("Instale Mermaid CLI: npm install --global @mermaid-js/mermaid-cli", file=sys.stderr)
        return 2
    for path in sorted(paths):
        convert(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

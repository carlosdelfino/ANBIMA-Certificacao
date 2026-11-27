#!/usr/bin/env python3
"""Converte Markdown com MathJax/LaTeX e diagramas Mermaid para PDF."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = ("CFG", "CGA", "CGE", "INTRODUÇÃO", "WEB3-RWA-E-STABLECOINS")
MERMAID = re.compile(r"```mermaid\s*\n(.*?)\n```", re.S)
CODE_SPAN = re.compile(r"```.*?```|`[^`\n]+`", re.S)
MATH_SPAN = re.compile(r"\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)|\$[^$\n]+\$", re.S)
ACCENTED = re.compile(r"[À-ÿ]+")
MATH_SYMBOLS = {"≠": r"\neq", "≤": r"\leq", "≥": r"\geq", "≈": r"\approx"}


def _fix_math_span(match: re.Match) -> str:
    span = match.group(0)
    for symbol, command in MATH_SYMBOLS.items():
        span = span.replace(symbol, f" {command} ")
    return ACCENTED.sub(lambda m: f"\\text{{{m.group(0)}}}", span)


def _fix_text_segment(segment: str) -> str:
    """Troca símbolos Unicode fora da matemática por comandos TeX em modo math."""
    parts, last = [], 0
    for match in MATH_SPAN.finditer(segment):
        chunk = segment[last:match.start()]
        for symbol, command in MATH_SYMBOLS.items():
            chunk = chunk.replace(symbol, f"${command}$")
        parts += [chunk, match.group(0)]
        last = match.end()
    chunk = segment[last:]
    for symbol, command in MATH_SYMBOLS.items():
        chunk = chunk.replace(symbol, f"${command}$")
    parts.append(chunk)
    return "".join(parts)


def normalize_unicode(text: str) -> str:
    """Substitui glifos ausentes nas fontes LaTeX, preservando blocos de código."""
    parts, last = [], 0
    for match in CODE_SPAN.finditer(text):
        parts.append(_fix_text_segment(MATH_SPAN.sub(_fix_math_span, text[last:match.start()])))
        parts.append(match.group(0))
        last = match.end()
    parts.append(_fix_text_segment(MATH_SPAN.sub(_fix_math_span, text[last:])))
    return "".join(parts)


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
        text = normalize_unicode(text)
        intermediate = temp / source.name
        intermediate.write_text(text, encoding="utf-8")
        output = source.with_suffix(".pdf")
        subprocess.run([
            "pandoc", str(intermediate), "--from=markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables",
            "--standalone", "--pdf-engine=lualatex", "--variable=geometry:margin=2cm",
            "--variable=mainfont:Latin Modern Roman", "--variable=monofont:DejaVu Sans Mono",
            "--output", str(output)
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

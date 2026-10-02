#!/usr/bin/env python3
"""Baixa cópias de estudo de normas a partir dos endereços oficiais da CVM."""
from pathlib import Path
from urllib.request import urlopen

DEST = Path(__file__).resolve().parents[1] / "normas"
URLS = {
    "Resolucao-CVM-175-consolidada.pdf": "https://conteudo.cvm.gov.br/cvm_institucional/export/sites/cvm/legislacao/resolucoes/anexos/100/resol175consolid.pdf",
    "Resolucao-CVM-19-consolidada.pdf": "https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/resolucoes/anexos/001/resol019consolid.pdf",
    "Resolucao-CVM-20-consolidada.pdf": "https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/resolucoes/anexos/001/resol020consolid.pdf",
    "Resolucao-CVM-21-consolidada.pdf": "https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/resolucoes/anexos/001/resol021consolid.pdf",
}

DEST.mkdir(parents=True, exist_ok=True)
for filename, url in URLS.items():
    target = DEST / filename
    try:
        with urlopen(url, timeout=30) as response, target.open("wb") as out:
            out.write(response.read())
        print(f"OK {target}")
    except Exception as exc:
        target.unlink(missing_ok=True)
        print(f"FALHA {filename}: {exc}")

# Exportação Markdown para PDF

Os documentos usam equações MathJax e blocos `mermaid`. As fórmulas usam sintaxe TeX compatível com MathJax e são renderizadas pelo motor LaTeX do Pandoc; os diagramas Mermaid são renderizados em PNG pelo Mermaid CLI antes da composição do PDF.

## Dependências

- Python 3.10+
- Pandoc
- TeX Live com `lualatex`
- Node.js LTS/npm e Mermaid CLI: `npm install --global @mermaid-js/mermaid-cli`

## Uso

Na raiz do projeto:

```bash
python3 scripts/build_pdfs.py
python3 scripts/build_pdfs.py CFG/README.md CGE/README.md
```

PDFs saem ao lado dos arquivos Markdown correspondentes. O script não baixa dependências; MathJax é processado pelo LaTeX local e Mermaid usa CLI local.

Normativas oficiais:

```bash
python3 scripts/download_normas.py
```

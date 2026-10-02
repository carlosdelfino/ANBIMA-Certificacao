---
trigger: always_on
---
# Paleta de Cores - GenAI RH (Rapport Tecnologia)

Esta paleta foi extraída diretamente do site [rapport.tec.br](https://rapport.tec.br/) e de sua imagem principal (`img/header.jpg`), servindo como base de design para a estilização do sistema.

## Cores Institucionais (do site CSS)

| Cor | Hex | Nome/Função | Aplicação Sugerida |
| :---: | :---: | :--- | :--- |
| <span style="display:inline-block; width:30px; height:30px; background-color:#F05F40; border-radius:4px; border:1px solid #ccc;"></span> | `#F05F40` | Laranja Rapport (Primária) | Botões principais, links ativos, destaques visuais, marca. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#eb3812; border-radius:4px; border:1px solid #ccc;"></span> | `#eb3812` | Laranja Escuro (Hover/Active) | Estados de foco, hover e pressionado dos elementos interativos. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#222222; border-radius:4px; border:1px solid #ccc;"></span> | `#222222` | Preto Grafite (Dark/Text) | Textos principais em modo claro, **fundo principal em modo escuro**, cabeçalhos de tabelas. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#ffffff; border-radius:4px; border:1px solid #ccc;"></span> | `#ffffff` | Branco Puro (Fundo/Contraste) | Fundos principais das telas, cards, contrastes em botões primários. |

---

## Cores de Tons da Imagem de Cabeçalho (`header.jpg`)

Estas cores foram extraídas diretamente da imagem principal do site utilizando algoritmo de quantização e servem para criar gradients, micro-animações, fundos secundários e bordas elegantes.

| Cor | Hex | Classificação | Aplicação Sugerida |
| :---: | :---: | :--- | :--- |
| <span style="display:inline-block; width:30px; height:30px; background-color:#fcc650; border-radius:4px; border:1px solid #ccc;"></span> | `#fcc650` | Amarelo Ouro | Alertas de status (ex: rascunho, em andamento), ícones de destaque. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#cc7501; border-radius:4px; border:1px solid #ccc;"></span> | `#cc7501` | Laranja Queimado / Bronze | Destaques secundários, bordas ativas ou estados alternativos. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#712d23; border-radius:4px; border:1px solid #ccc;"></span> | `#712d23` | Marrom Avermelhado / Vinho | **Fundo de cards em modo escuro**, textos secundários em modo claro, textos em botões de tons quentes claros. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#ce6e6d; border-radius:4px; border:1px solid #ccc;"></span> | `#ce6e6d` | Coral Suave / Rosa Velho | Elementos de erro/atenção leves, ilustrações ou badges. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#070404; border-radius:4px; border:1px solid #ccc;"></span> | `#070404` | Preto Profundo / Quase Preto | Cores de sombra, fundos pretos absolutos em modo escuro. |
| <span style="display:inline-block; width:30px; height:30px; background-color:#f7d4ca; border-radius:4px; border:1px solid #ccc;"></span> | `#f7d4ca` | Pêssego Suave | Fundos secundários claros (modo impressão), bordas leves, **texto secundário/muted em modo escuro**. |

---

## Tokenização em CSS Variables

Recomenda-se utilizar os seguintes nomes de variáveis CSS em `:root` para o design system do sistema:

```css
:root {
  /* Brand Colors */
  --color-primary: #F05F40;
  --color-primary-hover: #eb3812;
  --color-dark: #222222;
  --color-light: #ffffff;

  /* Accent Colors (From Main Image) */
  --color-accent-gold: #fcc650;
  --color-accent-bronze: #cc7501;
  --color-accent-wine: #712d23;
  --color-accent-coral: #ce6e6d;
  --color-accent-peach: #f7d4ca;
  --color-accent-deep-black: #070404;

  /* Semantic Colors — Dark Theme (default) */
  --color-bg-main: var(--color-dark);          /* #222222 — fundo principal */
  --color-bg-card: var(--color-accent-wine);   /* #712d23 — fundo de cards */
  --color-text-main: var(--color-light);       /* #ffffff — texto principal */
  --color-text-muted: var(--color-accent-peach); /* #f7d4ca — texto secundário */
  --color-border: rgba(255, 255, 255, 0.15);   /* bordas sutis sobre fundo escuro */
  --color-link: var(--color-accent-gold);      /* #fcc650 — links e subtítulos */

  /* Semantic Colors — Light Theme (print/PDF) */
  --color-bg-main-light: var(--color-light);       /* #ffffff */
  --color-bg-card-light: var(--color-accent-peach); /* #f7d4ca */
  --color-text-main-light: var(--color-dark);      /* #222222 */
  --color-text-muted-light: var(--color-accent-wine); /* #712d23 */
  --color-border-light: rgba(34, 34, 34, 0.15);
  --color-link-light: var(--color-accent-bronze);  /* #cc7501 */
}
```

---

## Mapeamento de Cores para Dashboards e Gráficos

Ao aplicar a paleta em dashboards (Chart.js, vis-network, etc.), utilize o seguinte mapeamento:

| Elemento | Modo Escuro | Modo Claro (Print) |
| :--- | :---: | :---: |
| Fundo principal | `#222222` | `#ffffff` |
| Fundo de cards | `#712d23` | `#f7d4ca` |
| Texto principal | `#ffffff` | `#222222` |
| Texto secundário (muted) | `#f7d4ca` | `#712d23` |
| Links / subtítulos h3 | `#fcc650` | `#cc7501` |
| Títulos h2 / destaque | `#F05F40` | `#F05F40` |
| Bordas | `rgba(255,255,255,0.15)` | `rgba(34,34,34,0.15)` |
| Alertas (linhas de risco) | `rgba(235,56,18,.12)` | `rgba(235,56,18,.08)` |
| Risco ALTO | `#eb3812` | `#eb3812` |
| Risco MODERADO | `#fcc650` | `#fcc650` |
| Risco CONTROLADO | `#F05F40` | `#F05F40` |
| Grafo: Infra/DEX | `#cc7501` | `#cc7501` |
| Grafo: Deployer | `#fcc650` | `#fcc650` |
| Grafo: Carteira externa | `#F05F40` | `#F05F40` |
| Grafo: fundo | `#070404` | `#070404` |
| Chart.js defaults.color | `#f7d4ca` | `#712d23` |
| Chart.js defaults.borderColor | `rgba(255,255,255,0.15)` | `rgba(34,34,34,0.15)` |
| Paleta de gráficos (21 cores) | `#F05F40, #fcc650, #cc7501, #eb3812, #ce6e6d, #f7d4ca, #d4502e, #b5651d, #fdd97a, #d9908f, #fae5df, #ff7a5c, #e89642, #ffd98a, #f54020, #c43d18, #8a3a2c, #5d3a32, #eb6b4a, #e07a3a, #d49a5a` | (mesma) |

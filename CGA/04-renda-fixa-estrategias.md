# CGA — Tema 2: Gestão de Carteiras – Renda Fixa

> Peso na prova: **18–22%**. Este é um dos temas mais cobrados — domine imunização, estratégias de curva e derivativos.

## 2.1 Gestão de RF em relação a benchmark

| Estratégia | Objetivo | Risco relativo (tracking error) | Características |
|---|---|---|---|
| **Indexação pura** | Replicar o índice (ex: IMA-B, IDA) | Quase zero | Compra todos os papéis do índice nas mesmas proporções; baixo custo, baixa rotatividade |
| **Enhanced indexing** | Superar levemente o índice | Baixo | Pequenos desvios permitidos: papéis "baratos", duration marginalmente diferente |
| **Gestão ativa** | Bater o índice de forma relevante | Alto | Apostas em duration, curva, crédito, emissores; maior custo e rotatividade |

- **Por que indexar?** Mercado de RF eficiente, custos baixos, e nem sempre o gestor consegue gerar alfa consistente.
- **Tracking error**: desvio-padrão da diferença de retorno carteira vs. benchmark. Indexação pura → ~0.
- **Na prática**: a escolha depende do mandato do cliente — fundos "IMA-B ativo" aceitam tracking error maior; fundos indexados prometem espelhar o índice.

## 2.2 Gestão de RF em relação a passivos (imunização)

### O problema que a imunização resolve

Um fundo de pensão (ou seguradora) tem **obrigações futuras conhecidas** (pagar aposentadorias). Se os juros **caírem**, o valor presente do passivo **sobe** — e se os ativos não subirem na mesma proporção, o fundo fica descasado ("mismatch"). Se os juros **subirem**, ocorre o inverso. A imunização faz o **ativo reagir à taxa de juros da mesma forma que o passivo**, neutralizando o risco.

### Condições da imunização clássica

1. **Duration da carteira = duration do passivo** (igualdade de dollar duration);
2. **Valor presente dos ativos ≥ VP do passivo**;
3. **Convexidade do ativo ≥ convexidade do passivo** (a carteira ganha mais quando juros caem e perde menos quando sobem).

> **Rebalanceamento contínuo**: a duration muda com o tempo e com a taxa — a imunização exige ajustes periódicos.

### Métricas essenciais

- **Duration (modificada)**: sensibilidade percentual do preço a uma variação paralela de 1 p.p. na taxa. ΔP/P ≈ −D × Δi.
- **Dollar duration (DV01 × 10.000)**: sensibilidade em R$ do preço por variação de 1 p.p. Usada para casar ativo e passivo em **valor**, não só em %.
- **Spread duration**: sensibilidade ao spread de crédito (não à taxa livre de risco). Importante em crédito privado.
- **Key rate duration**: sensibilidade a movimentos em **vértices específicos** da curva (ex: só o vértice de 5 anos mexe). Capta movimentos **não paralelos**.
- **Convexidade**: correção de segunda ordem — mede quanto a própria duration muda com a taxa. Convexidade maior = melhor desempenho em grandes oscilações.

### Estruturas de carteira vs. passivo

| Estrutura | Composição | Uso típico |
|---|---|---|
| **Bullet** | Papéis concentrados num vencimento próximo ao do passivo | Casar com passivo único (uma obrigação) |
| **Barbell** | Papéis nos extremos (curto + longo prazo), nada no meio | Mesma duration do bullet, mas **maior convexidade**; perde se a curva ficar mais "arqueada" no meio |
| **Ladder (escadinha)** | Vencimentos distribuídos uniformemente | Liquidez recorrente; reinvestimento suave ao longo do tempo |
| **Cash-flow matching** | Cada fluxo do ativo casa com cada fluxo do passivo | Imunização perfeita por construção; dispensa rebalanceamento, mas é menos flexível e pode custar mais |

**Exemplo**: passivo de R$ 100 mi em 10 anos, duration 7. Opções: bullet de títulos com ~7 anos de duration, ou barbell (50% em duration 2 + 50% em duration 12 ≈ 7). O barbell tem mais convexidade, mas depende do formato da curva.

**Exemplo numérico de imunização**: passivo de R$ 100 mi com duration 7.
- Juros **caem** 1 p.p. → passivo sobe ~7% (≈ R$ 7 mi a mais de obrigação). Ativo com duration 7 também sobe ~7% → casado.
- Juros **sobem** 1 p.p. → passivo cai ~7%; ativo cai ~7% → casado.
- Se o ativo tivesse duration só 3, na queda de juros o passivo subiria 7% e o ativo apenas 3% → **déficit de ~R$ 4 mi**. É esse descasamento que a imunização elimina.
- Com convexidade do ativo **maior** que a do passivo, movimentos grandes favorecem o fundo nos dois sentidos.

## 2.3 Outras estratégias

### Combinações e alavancagem

Estratégias de RF raramente vêm isoladas — o gestor **combina** posições: duration + aposta de curva + crédito + hedge cambial, de modo que cada fonte de retorno (ver 2.4) contribua conforme a convicção.

- **Alavancagem via futuros**: comprar futuro de DI/DÓLAR exige só margem — exposição maior que o patrimônio.
- **Alavancagem via opções**: prêmio pequeno, exposição grande (delta).
- **Repos (compromissadas)**: tomar funding barato lastreado nos próprios títulos para comprar mais RF (carry trade).

**Exemplo de carry via repo**: financiar a R$ a CDI e comprar NTN-B pagando IPCA + 6% — lucra-se a diferença entre o rendimento do papel e o custo do funding, mas a posição amplifica perdas se a taxa real subir (marcação a mercado + alavancagem).

### Derivativos

| Instrumento | Uso |
|---|---|
| **Termo** | Travar preço futuro de compra/venda; sem fluxo diário |
| **Futuros (DI, DAP, DÓLAR)** | Hedge ou aposta direcional com ajuste diário e alta liquidez |
| **Opções** | Hedge assimétrico: limita perda mantendo ganho (put protetora) |
| **Swaps (DI×pré, DI×IPCA)** | Trocar indexador sem vender o papel — ex: trocar pré por CDI |
| **Derivativos de crédito (CDS)** | Comprar/vender proteção contra default de um emissor |

**Como funciona o CDS**: o comprador de proteção paga um prêmio periódico; se o emissor der default, recebe o valor de face (ou a perda incorrida). Permite "vender" risco de crédito sem alienar o papel — útil quando o título é ilíquido.

**Por que derivativos?** Ajustam a exposição rapidamente, com pouco capital e sem mexer na carteira física — essencial para gestão tática e alavancagem.

### Hedge e seguro de carteira

- **Hedge de câmbio**: dólar futuro ou swap cambial para carteiras com passivo/ativo descasado em moeda.
- **Hedge de juros**: vender futuro de DI protege carteira pré-fixada de alta de juros.
- **Hedge de crédito**: CDS ou redução de exposição setorial.
- **Seguro de carteira (portfolio insurance)**: réplica dinâmica de put — vender ativos quando caem para "travar" piso. **Limitações**: custo de rebalanceamento, gaps de mercado, liquidez em estresse (a estratégia falha justo quando mais precisa — ver crise de 1987).

### Gestão da curva de juros

**Formatos**: normal (ascendente), invertida (descendente), flat, e com "barriga" (humped).

**Teorias da estrutura a termo**:

| Teoria | Ideia central | Implicação |
|---|---|---|
| **Expectativas puras** | A taxa longa é a média das taxas curtas esperadas | Curva ascendente → mercado espera alta de juros. Não há prêmio por prazo |
| **Preferência por liquidez** | Investidores exigem **prêmio** para travar prazo maior | Curva tende a ser ascendente mesmo sem expectativa de alta |
| **Segmentação de mercado** | Cada vértice tem oferta/demanda próprias (bancos curtos, previdências longas) | Qualquer formato é possível; a curva não "prevê" nada |

**Estratégias de curva** (apostas no **formato**, não no nível):

| Estratégia | Aposta | Operação |
|---|---|---|
| **Steepening (aumento de inclinação)** | Juros longos sobem mais (ou caem menos) que curtos | Long nos vértices curtos + short nos longos |
| **Flattening (achatamento)** | Juros longos caem mais (ou sobem menos) que curtos | Long nos vértices longos + short nos curtos |
| **Butterfly** | O "meio" da curva performa diferente das pontas | Ex: long 5a + short 2a e 10a quando a barriga vai se corrigir |

**Leitura intuitiva**: imagine a curva como uma corda entre os vértices curtos e longos. Steepening = a ponta longa sobe; flattening = a ponta longa desce; butterfly = o meio se desalinha das pontas. As apostas são montadas com posições compradas/vendidas em vértices distintos, equilibradas por key rate duration para isolar o formato — não o nível — da curva.

**Exemplo (steepening)**: gestor compra NTN curta e vende futuro de vértice longo (DV01s equivalentes). Se a curva abrir (longo sobe mais que curto), a posição lucra independentemente de os juros subirem ou caírem em nível.

### Crédito privado, ASG e títulos temáticos

- **Crédito privado**: debêntures, CRI/CRA, FIDCs — retorno = taxa livre de risco + **spread de crédito** (prêmio por risco de default e iliquidez).
- **Análise ASG (ESG)**: avaliar emissor também por fatores ambientais, sociais e de governança — cada vez mais exigida por investidores institucionais e políticas de fundos.
- **Títulos temáticos**: *green bonds* (projetos ambientais), *social bonds*, *sustainability-linked* (metas ESG atreladas ao custo da dívida).

## 2.4 Fontes de retorno de uma carteira de RF

1. **Duration**: ganho/perda por movimento do **nível** das taxas (maior fonte, mais risco).
2. **Convexidade**: ganho extra em grandes movimentos de taxa.
3. **Moeda**: exposição cambial (títulos indexados a dólar, hedge imperfeito).
4. **Mercados**: alocação entre países/segmentos (emergentes vs. desenvolvidos).
5. **Setores/emissores**: spread de crédito por segmento.
6. **Seleção de papéis (security selection)**: escolher o título "barato" dentro do mesmo setor/rating.

> **Atribuição de retorno**: decompor o desempenho da carteira nesses fatores para saber de onde veio o alfa (ou a perda).

## Dicas para a prova

- **Imunização ≠ hedging puro**: imunizar é casar duration/convexidade com **passivos**; hedge é eliminar risco de um ativo/benchmark.
- **Dollar duration (DV01)** é o que se casa na prática — duration percentual sozinha não basta quando os valores diferem.
- **Barbell vs. Bullet** com mesma duration: o barbell tem **mais convexidade**, mas sofre mais com movimentos não paralelos.
- **Convexidade alta é sempre desejável** (tudo mais constante) — quem tem mais convexidade performa melhor em qualquer grande oscilação.
- Steepening = apostar na **abertura** da curva; flattening = no **fechamento**; butterfly = correção da **barriga**.
- Expectativas puras: curva **prevê** juros futuros; preferência por liquidez: curva embute **prêmio**; segmentação: curva reflete só **oferta/demanda** local.
- Swaps trocam **fluxos/indexadores** sem vender o papel — questões sobre "transformar pré em pós" → swap DI×pré.
- Seguro de carteira falha em **gaps e estresse de liquidez** — a prova adora essa limitação.

## Checklist de estudo

- [ ] Sei diferenciar indexação pura, enhanced indexing e gestão ativa pelo tracking error
- [ ] Sei explicar por que imunização protege contra movimentos de juros (e por que precisa de rebalanceamento)
- [ ] Domino duration, dollar duration, spread duration, key rate duration e convexidade
- [ ] Sei montar bullet, barbell e ladder e dizer as vantagens de cada
- [ ] Sei quando usar cash-flow matching vs. imunização por duration
- [ ] Conheço os usos de termo, futuros, opções, swaps e CDS
- [ ] Sei hedging de câmbio, juros e crédito — e as limitações do seguro de carteira
- [ ] Domino as 3 teorias da curva e as estratégias steepening/flattening/butterfly
- [ ] Sei listar e atribuir as fontes de retorno de uma carteira de RF

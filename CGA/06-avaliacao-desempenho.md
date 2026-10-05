# Tema 4 — Avaliação de Desempenho

Este tema representa de 11% a 15% da prova. Para quem está mudando de carreira, pense nele como três perguntas: **quanto a carteira rendeu, por que rendeu e se o retorno compensou o risco?**
## 4.1 Mensuração de performance
### Retorno sem fluxos externos

Quando não há aportes nem resgates no período, o retorno é:

\[
R = \frac{V_f - V_i + D}{V_i}
\]

Em que `Vi` é o valor inicial, `Vf` é o valor final e `D` representa rendimentos distribuídos. Se foram reinvestidos, já estarão refletidos em `Vf` e não devem ser somados novamente.
### Retorno com fluxos externos

Aportes e resgates não são resultado da gestão. É preciso separar o efeito dos fluxos do ganho ou perda dos ativos. A escolha depende da pergunta:

- **TWR (Time-Weighted Return):** elimina o efeito do tamanho e do momento dos fluxos; avalia o gestor.
- **MWR (Money-Weighted Return):** considera valor e data dos fluxos; avalia a experiência do investidor.
### Taxa de retorno total

A taxa de retorno total reúne variação de preço e renda recebida:

\[
R_{total}=\frac{P_f-P_i+Rendimentos}{P_i}
\]

Ela inclui juros, cupons, dividendos e ganhos de capital. Compare retornos na mesma moeda e com tratamento consistente de custos, impostos e proventos.
### TWR: retorno ponderado pelo tempo

Divida o horizonte em subperíodos sempre que houver fluxo externo, calcule o retorno de cada subperíodo e faça a ligação geométrica:

\[
TWR=\prod_{t=1}^{n}(1+R_t)-1
\]

Exemplo: retornos de 10% e -5% resultam em `(1,10 × 0,95) - 1 = 4,5%`, e não 5%. O TWR é o padrão para comparar gestores porque eles normalmente não controlam aportes e resgates.
### MWR: retorno ponderado pelo dinheiro

O MWR é a taxa interna de retorno (TIR) que iguala o valor presente dos fluxos ao valor final:

\[
0=-V_0+\sum_{t=1}^{n}\frac{FC_t}{(1+MWR)^t}+\frac{V_f}{(1+MWR)^n}
\]

Ele atribui mais peso aos períodos em que havia mais capital investido. Um grande aporte antes de uma queda piora o MWR, mesmo que o TWR do gestor permaneça igual.
### Anualização

Para retorno acumulado em `n` períodos por ano:

\[
R_{anual}=(1+R_{período})^{n}-1
\]

Para volatilidade, sob independência e estabilidade: `σanual = σperíodo × √n`. Não multiplique retorno composto por 12 e não anualize períodos muito curtos sem contextualizar.
## 4.2 Atribuição de performance

A atribuição explica a diferença entre carteira e benchmark. Ela transforma “superou o índice” em decisões identificáveis.
### Benchmark

Benchmark é uma referência para política, risco e avaliação. Deve ser **investível, mensurável, não ambíguo, apropriado, previamente definido, compatível com o estilo e refletir a oportunidade de investimento**.

Tipos comuns: índice amplo de mercado, índice de estilo, benchmark absoluto (como CDI + meta), carteira customizada e grupo de pares. Um benchmark composto deve ter pesos e regra de rebalanceamento explícitos.

Testes de qualidade incluem: coerência com o mandato; cobertura dos ativos; baixa exposição sistemática residual; estabilidade do beta; atribuição explicável; disponibilidade de dados; possibilidade prática de reprodução. Trocar a referência depois de observar o resultado cria viés.
### Atribuição macro

Avalia decisões do patrocinador ou comitê: alocação estratégica, alocação tática, escolha de gestores e efeitos de implementação. Compara política de longo prazo, exposição efetiva e resultados dos gestores selecionados.
### Atribuição micro

No modelo Brinson, o retorno ativo é decomposto em:

- **Alocação:** sobre ou subponderar um segmento que performou diferente do benchmark.
- **Seleção:** escolher ativos que renderam diferente do segmento de referência.
- **Interação:** efeito conjunto entre peso ativo e seleção; pode ser apresentado separadamente ou agregado.

Use pesos do início do período e retornos consistentes. A soma dos efeitos, mais resíduos de ligação, deve reconciliar o retorno ativo.
### Atribuição em renda fixa

A decomposição pode separar **carry e cupom, rolldown, variação da curva livre de risco, duration, inclinação e curvatura, spread de crédito, seleção de emissores, inflação, câmbio e negociação**. Duration e key-rate duration ajudam a localizar a exposição na curva. Convexidade explica parte não linear.

O benchmark deve ter duration, qualidade de crédito, indexador e universo comparáveis. Um ganho por alongar duration não deve ser confundido com seleção de crédito.
## 4.3 Avaliação ajustada ao risco

Considere retornos e taxa livre de risco na mesma periodicidade. Alfa e índices positivos são desejáveis, mas só fazem sentido com amostra, benchmark e modelo adequados.

| Medida | O que mede | Fórmula | Quando usar |
|---|---|---|---|
| Retorno total | Ganho de preço e renda | `(Vf − Vi + renda) / Vi` | Período sem fluxos ou ativo individual |
| TWR | Desempenho sem efeito dos fluxos | `∏(1 + Rt) − 1` | Comparar gestores e fundos |
| MWR/TIR | Experiência do capital investido | Taxa que zera o VPL dos fluxos | Avaliar investidor, projeto ou carteira com fluxos controlados |
| Alfa de Jensen | Retorno além do previsto pelo CAPM | `α = Rp − [Rf + βp(Rm − Rf)]` | Avaliar habilidade após ajustar por risco sistemático |
| Razão de Treynor | Excesso de retorno por beta | `(Rp − Rf) / βp` | Carteira bem diversificada; risco relevante é sistemático |
| Índice de Sharpe | Excesso de retorno por risco total | `(Rp − Rf) / σp` | Comparar carteiras completas ou não diversificadas |
| Information Ratio | Retorno ativo por risco ativo | `(Rp − Rb) / TE` | Avaliar consistência contra benchmark |
| Tracking Error | Volatilidade do retorno ativo | `σ(Rp − Rb)` | Controlar desvio em relação ao benchmark |
| M² | Sharpe convertido em retorno comparável | `Rf + Sharpep × σm` (ou diferença para `Rm`) | Comunicar performance ajustada ao risco em pontos percentuais |
### Leitura das medidas

O **Alfa de Jensen** depende do CAPM e do beta estimado. A **Razão de Treynor** ignora risco diversificável. O **Sharpe** usa volatilidade total e pode ser instável quando o excesso de retorno é negativo.

O **Information Ratio** combina valor agregado e consistência; maior IR indica mais retorno ativo por unidade de tracking error. TE baixo não significa risco absoluto baixo. O **M²** alavanca ou desalavanca a carteira até a volatilidade do mercado, facilitando comparação em unidades de retorno.
### Controle de qualidade

Valide preços, proventos, fluxos, câmbio, calendário, taxas, benchmark e cortes de horário. Reconcilie custodiante, administrador e gestor; investigue resíduos; documente metodologias; preserve trilha de auditoria; aplique revisão independente.

Evite viés de sobrevivência, seleção de períodos, backfill e troca retrospectiva de benchmark. Informe retornos bruto e líquido de taxas conforme o objetivo, use séries suficientemente longas e teste significância e estabilidade.
## Dicas para a prova

- Se a pergunta é sobre **gestor**, prefira TWR; se é sobre **experiência do investidor**, prefira MWR.
- Fluxo externo exige subperíodo no TWR; rendimento do ativo integra o retorno total.
- Sharpe usa desvio-padrão; Treynor usa beta; Information Ratio usa tracking error.
- Alfa compara retorno realizado ao retorno exigido pelo CAPM.
- Atribuição explica a origem; avaliação ajustada ao risco julga a qualidade.
- Em renda fixa, separe carry, curva, duration e spread de crédito.
## Checklist de estudo

- [ ] Calculo retorno total, TWR, MWR e retorno anualizado.
- [ ] Sei explicar por que TWR e MWR podem divergir.
- [ ] Reconheço propriedades, tipos e testes de um bom benchmark.
- [ ] Distingo atribuição macro de alocação, seleção e interação.
- [ ] Decomponho performance de renda fixa por fatores.
- [ ] Comparo Jensen, Treynor, Sharpe, IR, TE e M².
- [ ] Identifico vieses e controles de qualidade dos dados.

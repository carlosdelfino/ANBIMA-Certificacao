# 3. Números, taxas e fórmulas sem medo

Não tente decorar tudo de uma vez. Primeiro entenda o que cada número responde e quais informações entram no cálculo. As fórmulas abaixo são versões introdutórias; regulamento, contrato, edital ou metodologia podem definir detalhes diferentes.

## 3.1 Retorno: quanto mudou meu dinheiro?

Se você compra uma cota por R$ 100 e depois ela vale R$ 110, a valorização foi R$ 10, ou 10% sobre o preço inicial:

$$Retorno=\frac{Preço\ final-Preço\ inicial}{Preço\ inicial}.$$

Se durante o período recebeu R$ 5 de distribuição, o retorno total simplificado é 15%: R$ 10 de valorização + R$ 5 recebidos, divididos pelos R$ 100 iniciais. Na vida real, considere datas, reinvestimento, impostos, custos e a origem da distribuição.

- **Retorno nominal** não desconta inflação.
- **Retorno real** tenta medir ganho de poder de compra: \((1+r_{nominal})/(1+inflação)-1\).
- **Retorno acumulado** soma o efeito de vários períodos compostos; retorno anualizado converte a um ritmo anual equivalente. Não confunda os dois.

## 3.2 Juros compostos: o rendimento também rende

Com R$ 100 investidos a 10% por ano, sem saques, custos, impostos ou risco:

- ao fim de 1 ano: R$ 110;
- ao fim de 2 anos: R$ 121, pois 10% incide sobre R$ 110;
- ao fim de 3 anos: R$ 133,10.

A fórmula geral é \(VF=VP(1+i)^n\): VF é valor futuro, VP é valor presente, i é taxa por período e n é quantidade de períodos. Taxa mensal deve ser comparada com prazo mensal; anual com prazo anual.

## 3.3 Valor presente: comparar dinheiro de datas diferentes

Receber R$ 110 daqui a um ano, com taxa de desconto de 10%, equivale a R$ 100 hoje:

$$VP=\frac{VF}{(1+i)^n}.$$

A **taxa de desconto** representa o retorno exigido para esperar e assumir riscos naquele cálculo. Quanto maior a taxa ou mais distante o pagamento, menor tende a ser o valor presente.

## 3.4 Título de renda fixa, taxa e preço

Imagine um título que pagará R$ 110 em um ano. Se a taxa usada pelo mercado for 10%, vale perto de R$ 100 hoje. Se a taxa subir para 20%, o mesmo R$ 110 vale cerca de R$ 91,67:

$$Preço=\frac{Pagamento\ futuro}{1+taxa}.$$

Por isso, um título com pagamentos fixos pode cair de preço quando as taxas de mercado sobem. “Renda fixa” descreve como os pagamentos são definidos; não significa preço imóvel nem retorno garantido em qualquer data de venda.

## 3.5 Duration: sensibilidade dos títulos a juros

Duration resume, de forma aproximada, a sensibilidade do preço de um título a mudanças na taxa de desconto. Uma duration modificada de 4 sugere que uma alta de 1 ponto percentual (0,01) pode reduzir o preço em cerca de 4%, antes de ajustes de convexidade:

$$\frac{\Delta Preço}{Preço}\approx-Duration\ modificada\times\Delta taxa.$$

- Duration maior costuma significar maior sensibilidade a juros.
- O sinal negativo expressa a relação inversa: taxa sobe, preço tende a cair.
- É aproximação para movimentos pequenos e relativamente simples da curva; não prevê toda oscilação.
- Duration não é a data de vencimento, embora ambas sejam medidas de tempo relacionadas aos fluxos.

## 3.6 Spread: a diferença adicional

Se um título público de referência paga 10% e uma empresa oferece 13% em prazo comparável, a diferença de 3 pontos percentuais é uma aproximação de spread. Ele pode compensar risco de crédito, dificuldade de revenda, incerteza e condições de oferta e demanda. Spread maior não significa automaticamente que o investimento é melhor: pode sinalizar risco maior.

## 3.7 Risco, volatilidade, Sharpe e VaR

**Volatilidade** resume a oscilação dos retornos históricos ou estimados. Não informa sozinha a chance de default, a liquidez ou o tamanho de uma perda extrema.

O **índice de Sharpe** responde: “quanto retorno acima de uma referência livre de risco houve para cada unidade de oscilação?”

$$Sharpe=\frac{Retorno\ da\ carteira-Taxa\ de\ referência}{Volatilidade\ da\ carteira}.$$

Maior Sharpe histórico pode ser interessante para comparação coerente, mas não garante melhor investimento futuro. Janelas, frequência, custos e formato dos retornos mudam a leitura.

**VaR** é uma estimativa de quantil. Se o VaR de um dia a 99% é R$ 1 milhão, o modelo estima que, em 99 de cada 100 dias comparáveis, a perda não ultrapassaria esse valor. Isso não diz quanto se pode perder no 1% restante. O resultado depende do modelo e dos dados. **ES (Expected Shortfall)** tenta resumir perdas médias para além do quantil; cenários de estresse ajudam a imaginar eventos extremos.

## 3.8 EBITDA: resultado operacional não é dinheiro no bolso

EBITDA é uma medida de resultado antes de juros, impostos, depreciação e amortização. Pode ajudar a comparar empresas, mas ainda não descontou tudo o que consome dinheiro.

Uma empresa pode mostrar EBITDA positivo e continuar sem caixa para pagar dívida se tiver de investir muito em máquinas (**CAPEX**), pagar impostos, financiar clientes ou quitar juros e principal. **OPEX** são gastos da operação cotidiana, como energia e equipe.

## 3.9 VPL/NPV e TIR/IRR: vale a pena investir?

- **VPL (valor presente líquido / NPV):** traz pagamentos futuros para o valor de hoje e subtrai o investimento inicial. VPL positivo diz que o projeto supera a taxa de desconto adotada, nas premissas usadas.
- **TIR (taxa interna de retorno / IRR):** taxa que faria o VPL ficar zero. É um percentual útil, mas pode ser enganoso quando os fluxos alternam sinais, os projetos têm escalas diferentes ou o dinheiro entra em datas muito diferentes.

Exemplo: você paga R$ 100 hoje e recebe R$ 60 no fim de cada um dos próximos dois anos. Com taxa de desconto de 10%:

$$VPL=-100+\frac{60}{1{,}10}+\frac{60}{1{,}10^2}\approx R\$4{,}13.$$

Nesse cenário simplificado, o VPL é positivo. A conclusão só vale se a taxa, as datas e os pagamentos forem razoáveis.

## 3.10 WACC: custo médio do dinheiro da empresa

Uma empresa financia seus projetos com capital dos sócios e dinheiro emprestado. **WACC** (custo médio ponderado de capital, ou CMPC) estima uma taxa média para remunerar essas fontes:

$$WACC=\frac{E}{D+E}K_e+\frac{D}{D+E}K_d(1-T).$$

E representa capital próprio, D dívida, \(K_e\) custo do capital próprio, \(K_d\) custo da dívida e T a alíquota de imposto adotada quando há benefício fiscal aplicável. A fórmula exige premissas coerentes; não é uma taxa universal pronta para copiar.

## 3.11 FCFF e FCFE: para quem sobra o caixa?

- **FCFF:** caixa gerado pelo negócio que está disponível para credores e acionistas, depois de gastos operacionais e investimentos necessários. Em geral, é comparado ao WACC.
- **FCFE:** caixa que sobra para os acionistas depois das necessidades do negócio e da dívida. Em geral, é comparado ao custo do capital próprio.

Uma fórmula didática do FCFF é:

$$FCFF=EBIT(1-T)+Depreciação\ e\ amortização-CAPEX-\Delta Capital\ de\ giro.$$

A definição exata de impostos, investimento e capital de giro depende do modelo financeiro usado.

## 3.12 DSCR: há caixa para pagar a dívida?

O **DSCR** compara o caixa disponível para pagar a dívida com o pagamento exigido no período:

$$DSCR=\frac{Caixa\ disponível\ para\ serviço\ da\ dívida}{Juros+principal\ devidos}.$$

Se há R$ 120 de caixa e R$ 100 de pagamento da dívida, DSCR = 1,20x. Naquela definição e naquele período, há R$ 1,20 de caixa para cada R$ 1,00 devido. Abaixo de 1,00x, o caixa calculado não cobre o pagamento. Cada contrato pode definir os itens incluídos de maneira específica.

## 3.13 Resumo: a pergunta que cada medida tenta responder

| Termo | Pergunta simples |
|---|---|
| Retorno | Quanto o investimento ganhou ou perdeu? |
| Volatilidade | Quanto os resultados oscilaram? |
| Duration | Quanto o preço pode reagir a uma mudança nas taxas? |
| Sharpe | Quanto retorno excedente houve por unidade de oscilação? |
| VaR | Qual perda-quantil o modelo estima num prazo definido? |
| VPL | Quanto valem hoje os fluxos futuros, descontado o investimento? |
| TIR | Qual taxa zera o VPL dos fluxos? |
| WACC | Qual custo médio das fontes de financiamento da empresa? |
| FCFF/FCFE | Quanto caixa existe para todos os financiadores ou para os acionistas? |
| DSCR | O caixa projetado cobre o pagamento da dívida? |

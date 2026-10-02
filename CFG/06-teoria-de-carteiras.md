# Tema 6 — Teoria de carteiras e modelos de precificação (8–12%)

## Por que combinar ativos muda o problema

Investir em um ativo isolado exige estimar seu retorno e risco. Uma carteira acrescenta uma pergunta: como os ativos se comportam juntos? A variância total depende das variâncias individuais e das covariâncias. Por isso um ativo arriscado pode reduzir o risco agregado se suas fontes de retorno forem diferentes das posições existentes.

## Preferências e utilidade

Investidor escolhe distribuição risco-retorno segundo riqueza e preferências. Aversão ao risco geralmente implica utilidade marginal decrescente e penalidade para variância; neutralidade considera valor esperado; propensão ao risco pode ocorrer em faixas. Saciabilidade é ponto em que mais consumo não aumenta utilidade. Dominância estocástica compara distribuições sem impor uma utilidade específica; dominância de primeira ordem é preferência de qualquer agente que prefira mais a menos.

Uma representação simples de utilidade média-variância é $U=E(R)-\frac{\lambda}{2}\sigma^2$, em que $E(R)$ é retorno esperado, $\sigma^2$ a variância e $\lambda$ a aversão ao risco. Não é descrição perfeita de toda preferência, mas ajuda a entender por que alguém exige retorno maior para aceitar mais incerteza. Tolerância ao risco observada em questionário, capacidade financeira de suportar perdas e necessidade de liquidez são conceitos relacionados, porém distintos.

## Fronteira eficiente e combinação com ativo livre de risco

Uma carteira é eficiente se não existe outra que entregue retorno esperado maior com o mesmo risco, ou risco menor para o mesmo retorno esperado. O conjunto eficiente depende das premissas sobre retornos, volatilidades, correlações, restrições e custos. Pequenos erros nas estimativas de retorno esperado podem produzir pesos extremos; otimização matemática não transforma entrada incerta em verdade.

Com ativo livre de risco e possibilidade de combinar posições, a linha que tangencia a fronteira arriscada representa combinações de melhor retorno excedente por risco sob as hipóteses do modelo. Na prática, taxas de empréstimo e aplicação podem diferir, há limites de alavancagem, impostos, custos, liquidez e risco de modelo. Use a construção como referência e aplique limites justificáveis.

## CAPM e beta

O CAPM relaciona retorno esperado ao risco sistemático: $E(R_i)=R_f+\beta_i[E(R_m)-R_f]$. Beta mede sensibilidade histórica ou estimada ao mercado de referência; beta 1 sugere exposição alinhada ao mercado no modelo, beta acima de 1 maior sensibilidade e beta negativo relação inversa média. Beta não mede risco total e pode mudar com alavancagem, negócio, janela, frequência e índice escolhido.

O prêmio de mercado $E(R_m)-R_f$ é uma expectativa, não um número diretamente observável sem hipóteses. CAPM é útil como linguagem e estimativa de custo do capital próprio, mas a relação pode falhar em amostras, mercados e horizontes. Não conclua que beta baixo significa ativo seguro: risco específico, iliquidez, concentração, cauda e crédito continuam presentes.

## Fatores e modelos multifatoriais

Modelos multifatoriais explicam retornos por exposições a fontes comuns, como mercado, tamanho, valor, qualidade, momentum, juros ou inflação. Eles ajudam a separar seleção de exposição sistemática. Uma carteira que superou o índice por estar sobreponderada em um fator valorizado não necessariamente demonstrou habilidade de seleção independente.

Fatores precisam de definição operacional, dados sem viés de sobrevivência, custos, capacidade e análise fora da amostra. Estratégia pode parecer boa historicamente por mineração de dados ou mudança estrutural. Explique fator como exposição mensurável e monitore se o mecanismo econômico ainda é plausível.

## Limites e uso responsável de modelos

Retornos passados são amostras ruidosas. Covariâncias estimadas em períodos calmos podem subestimar correlação em crises; retorno esperado é ainda mais difícil de estimar com precisão. Use intervalos, cenários, restrições transparentes e comparação com pesos simples. Documente dados, janela, moeda, frequência e reequilíbrio. Reavalie quando o regime ou a tese de investimento muda.

## Fronteira eficiente

Combinações de ativos produzem retorno esperado \(E[R_p]=w'\mu\) e variância \(w'\Sigma w\), com \(\sum w_i=1\), limites e custos. Fronteira eficiente contém carteiras que maximizam retorno para risco dado ou minimizam risco para retorno dado. Carteira de variância mínima global tem menor variância factível. Restrições a venda a descoberto, custos e impostos mudam a fronteira.

Ativo livre de risco permite combinação linear com carteira arriscada. Em hipóteses do modelo, carteira tangente maximiza Sharpe; linha de mercado de capitais liga taxa livre de risco e carteira de mercado. Alavancagem amplia retorno e risco; financiamento real raramente ocorre à taxa livre de risco. Hipóteses de expectativas homogêneas, mercados sem fricção e acesso simétrico são limitações.

## Beta e CAPM

\(\beta_i=Cov(R_i,R_m)/Var(R_m)\), sensibilidade ao retorno de mercado. CAPM: \(E[R_i]=R_f+\beta_i(E[R_m]-R_f)\). SML liga retorno requerido e beta; risco diversificável não recebe prêmio no modelo, risco sistemático recebe. Beta histórico depende de janela, benchmark e alavancagem. CAPM simplifica múltiplos riscos e não garante previsão correta.

## DDM, DCF e múltiplos

Gordon: \(P_0=D_1/(k_e-g)\), requer crescimento sustentável \(g<k_e\). Modelos multiestágios separam transição e maturidade. FCFE desconta pelo custo de equity; FCFF pelo WACC. Múltiplos (P/L, P/VP, P/Vendas, P/FC, EV/EBITDA, PEG, dividend yield) dependem de comparáveis, contabilidade, ciclo, crescimento e risco. Definições e denominadores devem ser consistentes.

## Modelos de fatores

Modelo de índice relaciona ativo a um fator comum, como mercado. Modelos multifatoriais acrescentam fatores macro ou fundamentais; APT deriva de ausência de arbitragem sob hipóteses, sem exigir carteira de mercado única. Fatores são exposições, não explicações causais automáticas. Risco de especificação, data mining e mudança de regime afetam robustez.

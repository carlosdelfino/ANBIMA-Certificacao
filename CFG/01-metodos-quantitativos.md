# Tema 1 — Métodos quantitativos (8–12%)

## Tempo, taxas e fluxos

Capitalização discreta: \(FV=PV(1+i)^n\); contínua: \(FV=PV e^{rt}\). Taxa efetiva por subperíodo deve refletir frequência: \(i_{ef}=(1+j/m)^m-1\), para taxa nominal anual j capitalizada m vezes. Anuidade postecipada: \(PV=C[1-(1+i)^{-n}]/i\). Perpetuidade constante: \(PV=C/i\); crescimento perpétuo: \(PV=C_1/(i-g)\), requer \(i>g\).

## Estatística descritiva e retornos

Média aritmética \(\bar{x}=\sum x_i/n\); ponderada \(\sum w_ix_i\); geométrica de retornos \([\prod(1+r_i)]^{1/n}-1\). Mediana é quantil 50%; moda é valor mais frequente. Variância amostral usa divisor \(n-1\); desvio-padrão é raiz. Covariância e correlação: \(\rho_{xy}=Cov(x,y)/(\sigma_x\sigma_y)\). Correlação não indica causalidade.

Retorno esperado discreto: \(E[R]=\sum p_ir_i\); variância: \(\sum p_i(r_i-E[R])^2\). Para dois ativos: \(\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho\sigma_1\sigma_2\). Variável contínua usa densidade e integrais. Normal é simétrica; lognormal modela variável positiva multiplicativa; t-Student tem caudas mais pesadas com graus de liberdade finitos.

## Amostragem e inferência

Erro padrão da média aproximadamente \(s/\sqrt{n}\) sob amostragem apropriada. Intervalo de confiança depende de distribuição, variância conhecida/desconhecida e tamanho amostral. Não é probabilidade de o parâmetro fixo estar dentro deste intervalo específico, na leitura frequentista: é cobertura do procedimento em repetidas amostras.

Teste de hipóteses define H0/H1, estatística, nível de significância e regra decisória. Erro tipo I rejeita H0 verdadeira; tipo II não rejeita H0 falsa. p-valor é probabilidade (sob H0 e modelo) de resultado tão extremo quanto o observado; não é probabilidade de H0 ser verdadeira. Significância estatística não implica relevância econômica.

## Regressão

Modelo simples \(Y=\beta_0+\beta_1X+\epsilon\); múltiplo adiciona variáveis. \(\beta\) é associação condicional ao modelo, não causalidade automática. R² mede fração da variação amostral explicada; não prova bom modelo nem forecasting eficaz. Premissas clássicas incluem forma funcional adequada, exogeneidade, ausência de colinearidade perfeita e hipóteses sobre erros para inferência. Heterocedasticidade, autocorrelação, endogeneidade, multicolinearidade, outliers, mudança estrutural e sobreajuste limitam previsões. ANOVA testa variância explicada/conjunta conforme especificação.

## Exemplo de risco de estimação

Uma carteira mostra volatilidade baixa em 24 observações mensais. Amostra pequena, crise ausente e avaliação pouco frequente podem tornar a estimativa imprecisa. Relate janela, frequência, fonte, método e incerteza; complemente com cenários históricos e hipotéticos.

## Intuição: população, amostra e estimativa

Imagine que você queira saber a oscilação típica de todas as debêntures de um mercado. Talvez não seja possível observar todos os títulos, todos os dias e todos os preços. Você seleciona uma **amostra** de observações e calcula uma estatística. A estatística é um retrato da amostra; o parâmetro que deseja conhecer pertence à população e é desconhecido.

A média amostral pode mudar se outra amostra for escolhida. Por isso, a média tem uma distribuição de amostragem. Sob condições apropriadas, o erro-padrão da média diminui aproximadamente como \(s/\sqrt{n}\): aumentar a amostra reduz parte da incerteza, embora dados enviesados ou mal coletados continuem ruins.

**Intervalo de confiança** descreve a cobertura de um procedimento em muitas repetições. Um intervalo de 95% não quer dizer, na interpretação frequentista, que há 95% de probabilidade de o parâmetro fixo estar dentro daquele intervalo já calculado. Quer dizer que o método produziria intervalos que cobrem o parâmetro em aproximadamente 95% de amostras repetidas, sob suas premissas.

## Distribuições: modelos, não descrições perfeitas

A distribuição normal é simétrica e concentra a maior parte dos valores perto da média. É prática em diversos cálculos, mas retornos financeiros podem ter assimetria e eventos extremos mais frequentes do que a normal sugeriria. A distribuição lognormal é útil para variáveis positivas que evoluem por fatores multiplicativos; a t de Student tem caudas mais pesadas, dependendo dos graus de liberdade.

Uma escolha de distribuição é uma hipótese de trabalho. Antes de usar percentis ou VaR, pergunte se os dados, o horizonte, a frequência e as caudas são compatíveis com a hipótese. Em crises, padrões históricos podem falhar justamente quando a estimativa importa mais.

## Testes de hipóteses com um exemplo

Suponha que um analista alegue que um fundo teve retorno médio mensal diferente de zero. Defina \(H_0:\mu=0\) e uma hipótese alternativa. Escolha nível de significância, calcule uma estatística com os dados e compare com a distribuição apropriada. Rejeitar \(H_0\) significa que os dados são pouco compatíveis com a hipótese nula segundo o modelo; não prova que a estratégia é boa, persistente ou causal.

- **Erro tipo I:** concluir diferença quando a hipótese nula era verdadeira.
- **Erro tipo II:** não detectar uma diferença existente.
- **Poder:** chance de detectar uma diferença real sob determinado desenho.
- **p-valor:** probabilidade, se a hipótese nula e o modelo fossem verdadeiros, de obter resultado tão extremo ou mais extremo que o observado.

Testar muitas estratégias até alguma parecer significativa aumenta o risco de falso achado. Também é preciso pensar em tamanho do efeito, custos, risco e possibilidade de repetição fora da amostra.

## Regressão: entender a relação estimada

Uma regressão linear simples escreve uma relação aproximada como \(Y=\beta_0+\beta_1X+\epsilon\). Se Y for retorno de uma ação e X retorno do mercado, \(\beta_1\) descreve como Y varia em média com X no modelo e na amostra. A linha estimada resume associação, não prova que X causou Y.

Na regressão múltipla, acrescentam-se variáveis. O coeficiente de uma variável descreve sua associação com Y mantendo as demais variáveis incluídas constantes, conforme o modelo. Se duas variáveis forem muito parecidas, fica difícil separar seus efeitos (multicolinearidade). Se fatores importantes forem omitidos ou estiverem correlacionados com X, a estimativa pode ser enviesada (endogeneidade).

**R²** mede a proporção da variação amostral de Y explicada pelo modelo de acordo com o cálculo. R² alto não garante que os coeficientes sejam estáveis, que a relação seja causal ou que a previsão funcione no futuro. Um modelo complexo pode ajustar muito bem o passado e falhar em novos dados: é o sobreajuste.

## Exemplo aplicado: estimar sensibilidade a juros

Um analista pode relacionar o retorno mensal de um fundo de renda fixa à mudança da taxa de juros. Um coeficiente negativo sugere que, na amostra e sob a especificação, aumentos de juros vieram associados a retornos menores. Antes de usar isso para prever, verifique se o fundo mudou de carteira, se houve alterações de spread, inflação, crédito, janela amostral ou liquidez. A regressão não substitui decomposição financeira e leitura da carteira.

## Checklist de conta quantitativa

1. Qual variável estou calculando e qual é sua unidade?
2. Os períodos coincidem (mês com mês, ano com ano)?
3. Os pesos somam 1 ou 100%?
4. Estou usando dados de população ou amostra? Qual divisor de variância se aplica?
5. O resultado é uma associação, uma previsão ou uma relação causal? Não confunda.
6. Quais premissas poderiam tornar o cálculo enganoso?

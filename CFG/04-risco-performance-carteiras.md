# Risco, performance e construção de carteiras

## Retorno é resultado; risco é o caminho possível

Uma carteira não é boa apenas porque teve retorno alto em um período. O resultado pode ter vindo de exposição concentrada, sorte, alavancagem ou risco não percebido. Antes de calcular métricas, defina horizonte, frequência dos dados, moeda, retorno bruto ou líquido, inclusão de proventos, benchmark e tratamento de fluxos externos. Comparações só fazem sentido com convenções alinhadas.

## Diversificação e alocação

Retorno da carteira é média ponderada dos retornos. Risco depende de variâncias e covariâncias:

Se 60% da carteira rende 10% e 40% rende −5% no período, o retorno simples é $0{,}6(10\%)+0{,}4(-5\%)=4\%$. Para vários períodos, os retornos se acumulam multiplicativamente: dois anos de +10% e −10% resultam em $(1{,}10)(0{,}90)-1=-1\%$, não zero. Fluxos aportados ou retirados também alteram como medir desempenho: retorno ponderado pelo tempo avalia a gestão removendo o efeito do momento dos aportes; retorno ponderado pelo dinheiro reflete a experiência do investidor.

## Volatilidade, covariância e diversificação

Variância mede dispersão quadrática em torno da média; desvio-padrão é sua raiz e volta à unidade do retorno. Volatilidade histórica estima dispersão passada e costuma ser anualizada multiplicando o desvio-padrão diário por $\sqrt{252}$, sob convenção de 252 pregões e hipóteses que podem não se sustentar. Ela não descreve sozinha perdas extremas, assimetria nem risco de crédito.

Para dois ativos, a variância da carteira depende dos pesos e da covariância: $\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2Cov(R_1,R_2)$. Se dois ativos têm volatilidades de 10% e 20%, peso de 50% cada e correlação zero, a volatilidade calculada é aproximadamente 11,18%, abaixo da média ponderada de volatilidades (15%). Se correlação for 1, não há esse benefício de descorrelação. Correlações podem aumentar justamente em crises, quando a diversificação mais faz falta.

Diversificar significa combinar fontes de risco que não se comportam exatamente igual, não simplesmente acumular muitos nomes. Dez emissores expostos ao mesmo setor e à mesma taxa básica podem continuar concentrados. Analise fator econômico, emissor, setor, indexador, prazo, liquidez, contraparte e moeda.

## Sharpe e comparação ajustada ao risco

O índice de Sharpe é $S=(R_p-R_f)/\sigma_p$, em que $R_p$ é retorno da carteira no período, $R_f$ retorno livre de risco compatível e $\sigma_p$ a volatilidade da carteira no mesmo horizonte. Se carteira rendeu 14%, referência sem risco 8% e volatilidade 12%, Sharpe é 0,5. O número compara excesso de retorno por unidade de volatilidade, mas não mede se o retorno absoluto atende ao objetivo nem penaliza assimetria de modo adequado.

Sharpe só é comparável com períodos e metodologias consistentes. Pode ficar instável com amostra curta, retornos não normais, ativos ilíquidos com preços suavizados ou escolha inadequada da taxa livre de risco. Retorno passado não garante repetição. Para carteiras assimétricas, examine drawdown, perda em cenários, liquidez, tracking error e métricas condicionais junto com Sharpe.

## VaR e Expected Shortfall

VaR a 95% para um dia de R$ 1 milhão significa, sob modelo e dados escolhidos, que a perda não deve exceder esse valor em aproximadamente 95% dos dias modelados. Não informa o tamanho médio das perdas nos 5% piores dias. VaR histórico usa mudanças passadas; paramétrico pressupõe distribuição e parâmetros; simulação de Monte Carlo gera cenários segundo modelo. Cada método erra de forma diferente.

Expected Shortfall (ES) estima a perda média além do quantil do VaR, sujeito à definição e implementação. É mais informativo sobre a cauda, mas também depende de amostra/modelo e pode ser difícil de estimar. Exemplo intuitivo: duas carteiras têm VaR de R$ 1 milhão; uma perde em média R$ 1,1 milhão nos dias de cauda e a outra R$ 3 milhões. O mesmo VaR esconde gravidade muito diferente.

O VaR deve vir acompanhado de backtesting (quantas violações ocorreram), testes de estresse e cenários históricos ou hipotéticos. Violação acima do esperado pode sinalizar modelo inadequado, mudança de regime ou erro de dados. Um resultado matemático não elimina julgamento de risco.

## Drawdown, tracking error e atribuição

Drawdown é queda do pico até um vale antes de recuperar. Mostra a experiência de perdas acumuladas e o tempo de recuperação, útil para avaliar tolerância do cliente e liquidez. Tracking error é o desvio-padrão do retorno ativo (carteira menos benchmark); não mede a perda absoluta: uma carteira pode ter tracking error baixo e ainda cair muito quando o índice cai.

Atribuição de performance tenta explicar de onde veio o resultado: alocação entre classes, seleção de ativos, exposição a fatores, moeda, custo e timing. O modelo de atribuição deve corresponder ao processo de investimento; residual inexplicado é um sinal para investigar dados ou metodologia, não para inventar uma narrativa depois do fato.

$$\sigma_p^2=\sum_i w_i^2\sigma_i^2+2\sum_{i<j}w_iw_j\rho_{ij}\sigma_i\sigma_j.$$

Diversificar reduz risco específico quando ativos não se movem perfeitamente juntos. Em crise as correlações podem subir. Alocação estratégica traduz objetivos, horizonte, liquidez, restrições e tolerância a risco em faixas-alvo; tática expressa desvios temporários. Rebalanceamento controla drift e pode cristalizar perdas/ganhos, logo regras devem considerar custos, impostos e liquidez.

## Sharpe e medidas de performance

$$Sharpe=\frac{R_p-R_f}{\sigma_p}.$$

Excesso de retorno por unidade de volatilidade total. Compare períodos, taxas e convenções consistentes. Sharpe pode falhar com retornos assimétricos, caudas pesadas, ativos ilíquidos ou volatilidade suavizada. Informação ratio usa retorno ativo médio dividido pelo tracking error. Sortino troca volatilidade total por risco de queda definido; drawdown máximo mede pico-a-vale histórico, sem prever limite futuro.

## VaR e Expected Shortfall

VaR de 1 dia a 99% é quantil de perda: sob o modelo e horizonte, a perda não deve exceder VaR em 99% dos dias. Ele nada diz sobre tamanho das perdas além do quantil. ES/CVaR é perda média condicional na cauda além do VaR. Métodos: histórico, paramétrico e Monte Carlo. Premissas de distribuição, janela, volatilidades, correlações, liquidez e horizonte são críticas. Backtesting compara perdas realizadas com exceções; stress tests cobrem cenários severos e plausíveis.

## Suitability e dever de adequação

Suitability compara produto, serviço ou operação com objetivos, situação financeira e conhecimento/experiência do cliente. Requer informação atualizada e explicação clara de riscos, custos, liquidez e horizonte. Perfil não é apenas um rótulo; restrições específicas podem prevalecer. Na distribuição, documente processo e alertas; não transforme adequação em promessa de resultado.

## Risco operacional, liquidez e modelo

Risco operacional decorre de processos, pessoas, sistemas e eventos externos. Risco de liquidez inclui custo/tempo para monetizar posição e obrigações de fluxo de caixa. Risco de modelo vem de dados, especificação e implementação. Limites quantitativos precisam de proprietário, frequência de medição, escalonamento e trilha de auditoria.

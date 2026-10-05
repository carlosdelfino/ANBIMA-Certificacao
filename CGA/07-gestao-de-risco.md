# Tema 5 — Gestão de Risco

Este tema representa de 11% a 15% da prova. Para quem está mudando de carreira, risco não é apenas “chance de perder”: é a incerteza relevante para o objetivo, medida, limitada, monitorada e comunicada.

## 5.1 Fundamentos da gestão de risco

A gestão de risco protege o mandato e a continuidade do fundo sem eliminar toda incerteza. Ela identifica, mede, monitora, controla e reporta exposições, apoiando decisões antes e depois da negociação.

Principais tipos: **mercado, crédito, contraparte, liquidez, operacional, legal, regulatório, modelagem, concentração, sistêmico e ASG**. Um mesmo ativo pode reunir vários deles.

O desempenho ajustado ao risco compara retorno com volatilidade, beta, downside risk ou risco ativo. Sharpe, Treynor, alfa e Information Ratio evitam premiar retorno obtido apenas por assumir mais risco.

Na gestão integrada, os riscos são agregados entre mesas, fundos, fatores, emissores e cenários. Correlações podem aumentar em crises; por isso, somar medidas isoladas ou confiar apenas na diversificação histórica é insuficiente.

### Funcionamento da área

Uma área independente define metodologias, limites e alertas; valida modelos; acompanha enquadramento; produz relatórios; escala violações; e mantém trilha de auditoria. O gestor assume risco dentro do mandato; risco e compliance exercem controle e supervisão.

**Backtesting** compara perdas previstas pelo modelo com resultados observados. Exceções de VaR acima do esperado podem indicar parâmetros ruins, quebra de hipótese, dados inadequados ou mudança de regime. Backtesting valida o uso, não prova que o modelo nunca falhará.

## 5.2 Medidas de risco de mercado

A **variância** é a média dos desvios quadráticos em relação ao retorno médio; o **desvio-padrão** é sua raiz e está na mesma unidade do retorno. Volatilidade histórica depende de janela e frequência; implícita é extraída de preços de opções.

\[
\sigma^2=\frac{\sum(R_t-\bar R)^2}{n-1}, \qquad \sigma=\sqrt{\sigma^2}
\]

O **beta** mede sensibilidade ao mercado: `β = Cov(Rp,Rm) / Var(Rm)`. Beta 1,2 sugere oscilação sistemática 20% maior, mas não mede todo o risco nem permanece necessariamente estável.

### Value at Risk (VaR)

VaR estima a perda mínima que pode ser excedida em determinado horizonte e nível de confiança. “VaR diário de R$ 1 milhão a 99%” não significa perda máxima; em cerca de 1% dos dias, a perda pode ser maior.

- **Paramétrico/analítico:** usa distribuição, volatilidades e correlações; é rápido, mas depende de hipóteses e linearização.
- **Simulação histórica:** reaplica choques observados; captura não normalidade histórica, mas depende da janela e não cria choques inéditos.
- **Monte Carlo:** simula fatores e reprecifica posições; é flexível, porém caro e sujeito a risco de modelo.

Para posições não lineares, delta-normal pode ser insuficiente; reprecificação completa ou ajustes delta-gama tratam melhor opções. VaR deve ser acompanhado de stress testing e medidas de cauda, como Expected Shortfall.

**Benchmark VaR** compara o VaR da carteira ao da referência ou mede o VaR do retorno ativo. É útil para mandatos relativos: mostra risco assumido além do benchmark, não apenas risco absoluto.

## 5.3 Riscos em renda fixa

| Risco | Como aparece | Controle ou medida |
|---|---|---|
| Taxa de juros | Preço cai quando a taxa sobe | Duration, convexidade e cenários |
| Curva de juros | Mudanças de nível, inclinação e curvatura | Key-rate duration e choques por vértice |
| Resgate antecipado | Emissor exerce opção quando é vantajoso | Modelagem de opção e duration efetiva |
| Reinvestimento | Cupons são reinvestidos a taxa menor | Casamento de fluxos e imunização |
| Crédito | Spread abre ou emissor não paga | Rating, spread duration, PD e análise fundamentalista |
| Liquidez | Venda exige prazo ou desconto | Bid-ask, volume, dias para liquidar e stress |
| Câmbio | Moeda altera principal e rendimentos | Exposição líquida e hedge cambial |
| Inflação | Corrói retorno real ou muda indexadores | Duration real, breakeven e cenários |
| Volatilidade | Altera valor de opções embutidas | Volatilidade implícita e OAS |
| Evento | Fusão, fraude, desastre ou mudança contratual | Limites, covenants e cenários específicos |
| Soberano | Governo ou país afeta pagamento/conversão | Limites por país e análise fiscal/política |

Duration aproxima a variação: `ΔP/P ≈ −Duration modificada × Δy`. Convexidade melhora a estimativa para choques maiores. Em títulos com opção, fluxo futuro muda com a taxa e exige duration efetiva.

## 5.4 Risco de crédito

Risco de **contraparte** é a possibilidade de a outra parte não cumprir a obrigação. Exposição potencial futura, netting, margem, colateral, limites e central contraparte reduzem, mas não eliminam, o risco.

Default pode ser falta de pagamento, recuperação judicial, reestruturação coercitiva ou outro evento definido no contrato. As medidas centrais são:

- **PD:** probabilidade de default.
- **EAD:** exposição no momento do default.
- **LGD:** percentual perdido após recuperações e custos.
- **Recovery rate:** percentual recuperado; em simplificação, `LGD = 1 − recovery`.
- **Expected Loss:** `EL = PD × EAD × LGD`.

Perda esperada deve ser precificada e provisionada; perda inesperada exige capital e limites. Concentração, correlação de defaults e migração de rating também importam.

Derivativos de crédito, como **CDS**, transferem risco: o comprador paga prêmio e recebe proteção em evento de crédito; o vendedor assume exposição. Surgem riscos de contraparte, base, documentação, liquidez e definição do evento.

Fatores **ambientais, sociais e de governança (ASG)** podem elevar PD e LGD por multas, passivos, transição climática, acidentes, fraude ou governança fraca. Devem entrar na análise financeira, e não funcionar apenas como rótulo.

## 5.5 Riscos de derivativos

Derivativos introduzem alavancagem, margem e chamadas de caixa, contraparte, base, liquidez, rolagem, modelo e riscos não lineares. Opções envolvem delta, gama, vega e theta; pequenas variações podem alterar rapidamente a exposição.

Um hedge reduz um fator e pode criar outro. Monitore exposição bruta e líquida, nocional, valor de mercado, colateral, vencimentos e cenários de gap. Verifique documentação, elegibilidade e finalidade conforme o regulamento.

## 5.6 Riscos operacional, de modelagem, liquidação e sistemas

**Operacional** decorre de falhas de pessoas, processos, eventos externos ou controles: ordem errada, fraude, cadastro incorreto e indisponibilidade. Mitigue com segregação de funções, dupla checagem, reconciliação, limites, continuidade e registro de incidentes.

**Modelagem** inclui especificação, dados, parâmetros, implementação e uso inadequados. Exige validação independente, benchmark entre modelos, backtesting, análise de sensibilidade, documentação e governança de mudanças.

**Liquidação** ocorre quando dinheiro ou ativo não é entregue; principal risk surge quando uma ponta é paga antes da outra. DVP, câmaras, colateral e limites ajudam. **Sistemas** envolvem indisponibilidade, ciberataque, acesso indevido, integridade e integração de dados; requerem redundância, controle de acesso, testes e recuperação.

## 5.7 Gestão de investimentos e risco

A construção de carteiras combina retorno esperado, covariâncias, restrições, liquidez e horizonte. Diversificação depende de correlações e exposições econômicas, não da mera quantidade de ativos.

**VaR componente** estima quanto cada posição contribui ao VaR total; a soma das contribuições reconcilia o VaR quando a medida é homogênea. VaR marginal mostra a variação por pequeno aumento da posição. O **orçamento de risco** distribui limites entre fatores, estratégias ou gestores e compara risco planejado com realizado.

**Stress testing** aplica choques históricos ou hipotéticos severos, inclusive correlações quebradas e gaps. Stress reverso pergunta qual cenário tornaria a perda ou iliquidez intolerável.

Gestão de liquidez estima tempo e custo para vender, concentração de cotistas, resgates, caixa, margem e descasamento entre ativo e passivo. Cenários devem combinar queda de preço, haircut, volume menor e resgates maiores.

### Métodos de alocação

- **Média-variância:** otimiza retorno esperado para variância; é sensível às estimativas.
- **Black-Litterman:** combina equilíbrio de mercado com visões do gestor e seus graus de confiança.
- **Monte Carlo:** simula trajetórias e avalia distribuição dos resultados sob múltiplos cenários.
- **ALM:** casa ativos e passivos, considerando fluxos, duration, liquidez e restrições do investidor.

### Rebalanceamento

- **Buy-and-hold:** mantém quantidades; a composição varia com o mercado e não exige regra contrária ao movimento.
- **Constant mix:** retorna a pesos-alvo, vendendo após altas e comprando após quedas; perfil contrarian.
- **CPPI:** aloca em ativo de risco um múltiplo do colchão (`patrimônio − piso`); compra na alta e vende na queda, mas sofre risco de gap e custos.

A frequência deve equilibrar desvio do alvo, custos, impostos e liquidez. Bandas de tolerância evitam negociações excessivas.

## Dicas para a prova

- VaR não é perda máxima; sempre leia horizonte e confiança.
- Histórico usa choques observados; Monte Carlo cria cenários; analítico depende mais de distribuição e linearidade.
- Duration trata taxa; spread duration trata spread; key-rate duration localiza vértices da curva.
- `EL = PD × EAD × LGD`; recovery maior implica LGD menor.
- Backtesting compara previsão com realização; stress testa situações severas fora do comportamento usual.
- Constant mix é contrarian; CPPI é pró-cíclico e protege um piso apenas sem gaps relevantes.

## Checklist de estudo

- [ ] Distingo riscos de mercado, crédito, liquidez, operacional e modelagem.
- [ ] Calculo e interpreto variância, volatilidade, beta e VaR.
- [ ] Comparo VaR analítico, histórico e Monte Carlo.
- [ ] Reconheço todos os principais riscos de renda fixa.
- [ ] Relaciono PD, EAD, LGD, recovery e perda esperada.
- [ ] Identifico riscos de derivativos, liquidação e sistemas.
- [ ] Explico VaR componente, orçamento de risco, stress e liquidez.
- [ ] Comparo média-variância, Black-Litterman, Monte Carlo e ALM.
- [ ] Diferencio buy-and-hold, constant mix e CPPI.

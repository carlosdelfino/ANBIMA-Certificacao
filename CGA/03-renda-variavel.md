# Gestão de Carteiras — Renda Variável

## Escopo e importância na prova

Este guia cobre o Tema 1 de Renda Variável da CGA, que representa aproximadamente 18% a 22% do exame. O foco não é decorar nomes: é reconhecer objetivo, fonte de retorno, risco, custo e situação adequada de cada estratégia.

Para quem concluiu a CFG e está mudando de carreira, pense como gestor: primeiro entenda o mandato e o benchmark; depois escolha instrumentos, construa a carteira, controle riscos e avalie se o resultado veio de habilidade ou apenas de exposição ao mercado.

## 1.1 Estratégias passivas, ativas e agnósticas

**Estratégia passiva** busca acompanhar um índice, aceitando o retorno do mercado e minimizando custo e desvio em relação ao benchmark. Exemplo: fundo que replica o Ibovespa.

**Estratégia ativa** tenta superar um benchmark por seleção de ações, setores ou momentos de compra e venda. Exemplo: fundo que reduz bancos e aumenta empresas de energia esperando ganhar do Ibovespa.

**Estratégia agnóstica ou total return** busca retorno absoluto, sem depender de superar um índice de ações e, muitas vezes, com baixa exposição líquida ao mercado. Exemplo: comprar a ação A e vender a B, lucrando se A tiver desempenho relativo melhor.

| Aspecto | Passiva | Ativa | Agnóstica (total return) |
|---|---|---|---|
| Objetivo | Replicar benchmark | Superar benchmark | Gerar retorno absoluto |
| Principal decisão | Como replicar com eficiência | Quais riscos ativos assumir | Quais relações e eventos explorar |
| Exposição ao mercado | Próxima à do índice | Geralmente relevante e variável | Pode ser baixa, neutra ou vendida |
| Medida importante | Tracking error e diferença de retorno | Alfa, tracking error e information ratio | Retorno, volatilidade, drawdown e Sharpe |
| Custos típicos | Menores | Maiores por análise e giro | Podem ser altos por hedge, aluguel e giro |
| Risco central | Não replicar bem o índice | Escolhas ficarem atrás do benchmark | Modelo, alavancagem e perdas nas duas pontas |
| Exemplo | ETF de Ibovespa | Fundo long only de valor | Long-short market neutral |

**Atenção:** total return não significa retorno garantido. Significa que a referência principal é um objetivo absoluto, e não necessariamente um índice acionário.

## 1.2 Estratégias passivas
### Fundos indexados

Um fundo indexado compra ativos para reproduzir composição e desempenho de um índice. O investidor delega a replicação ao gestor e negocia cotas conforme as regras do fundo.

O resultado líquido pode ficar abaixo do índice por taxa de administração, custos, impostos, caixa não investido, rebalanceamentos e imperfeições de réplica. Essa diferença é o **tracking difference**; a instabilidade dessa diferença é capturada pelo **tracking error**.
### Futuros de ações e de índices

Contratos futuros permitem obter ou reduzir exposição acionária sem comprar todas as ações. Exemplo: um fundo com caixa a aplicar compra futuro de Ibovespa para manter exposição enquanto seleciona os papéis.

Vantagens: liquidez, rapidez e menor necessidade inicial de caixa. Riscos: ajustes diários, chamadas de margem, diferença entre futuro e carteira desejada, vencimento e rolagem dos contratos.
### Total return equity swaps

No swap de retorno total de ações, uma parte recebe o retorno total de uma ação ou índice — valorização mais proventos conforme contrato — e paga outra remuneração, geralmente ligada a juros.

Exemplo: o fundo recebe o retorno do Ibovespa e paga CDI mais spread. Obtém exposição sintética, mas assume risco de contraparte, garantias, liquidez e termos contratuais.
### ETFs e ETFs ASG

ETF é fundo com cotas negociadas em bolsa que normalmente acompanha um índice. Combina diversificação, transparência e negociação intradiária, mas seu preço pode apresentar prêmio ou desconto em relação ao valor patrimonial.

Um ETF ASG acompanha índice com critérios ambientais, sociais e de governança. Não basta o rótulo: examine metodologia, exclusões, pesos, qualidade dos dados e frequência de revisão para identificar concentração ou greenwashing.
### Métodos de replicação

| Método | Como funciona | Vantagem | Limitação |
|---|---|---|---|
| Full replication | Compra todos os ativos nos pesos do índice | Simplicidade e aderência | Cara ou inviável em índice amplo/ilíquido |
| Amostragem estratificada | Compra amostra que preserva setor, tamanho e fatores | Reduz custos e número de posições | Pode elevar tracking error |
| Otimização | Modelo escolhe carteira que minimiza desvio esperado | Equilibra custo, liquidez e aderência | Depende do modelo e de estimativas |

Exemplo: para replicar índice com 200 ações, full replication compra as 200; amostragem escolhe representantes de cada grupo; otimização escolhe combinação estatisticamente próxima, sujeita a limites.

## 1.3 Estratégias ativas e agnósticas
### Long-short e market neutral

Long-short combina posições compradas e vendidas. O ganho procurado é relativo: comprar empresa considerada barata e vender empresa semelhante considerada cara.

Market neutral procura neutralizar a exposição líquida ou o beta de mercado. Exposição financeira líquida zero não garante beta zero; sensibilidades, setores e fatores também precisam ser controlados.
### Long only e estilos

Long only mantém posições compradas e ganha principalmente com alta das ações. Pode reduzir caixa ou posições, mas normalmente não usa vendas a descoberto como fonte central de retorno.

- **Growth:** empresas com crescimento esperado elevado; risco de expectativas otimistas e múltiplos altos.
- **Value:** ações baratas frente a fundamentos; risco de “armadilha de valor”, quando o preço baixo reflete deterioração real.
- **Blend:** mistura growth e value para reduzir dependência de um estilo.
- **Large, mid e small caps:** empresas grandes tendem a ter mais liquidez; menores podem oferecer crescimento, mas com maior volatilidade e risco de saída.
- **High dividend yield:** busca dividendos altos e sustentáveis; yield alto pode resultar de queda do preço e não de qualidade.
### Investimentos socialmente responsáveis e ASG

Podem excluir atividades, selecionar líderes ASG, aplicar filtros positivos/negativos, exercer voto e engajamento ou integrar fatores ASG à análise financeira.

Exemplo: custo de descarbonização pode reduzir fluxo de caixa; governança fraca pode elevar desconto no valuation. Critério ASG não elimina risco nem assegura desempenho superior.
### Enhanced indexing

Parte de um índice, mas aceita pequenos desvios para tentar superá-lo com tracking error controlado. Exemplo: sobrepeso moderado em empresas com melhor qualidade e subpeso nas mais endividadas.
### Fundamental growth e fundamental value

O gestor growth projeta receitas, mercado endereçável, margens e reinvestimento para localizar crescimento ainda não refletido no preço. O gestor value compara preço com valor intrínseco e procura margem de segurança.

Ambos precisam de catalisador, horizonte e disciplina de venda. Uma ótima empresa pode ser investimento ruim se o preço já incorporar cenário perfeito.
### Sector rotation

Altera pesos setoriais conforme ciclo econômico, juros, inflação e lucros. Exemplo: aumentar setores cíclicos na recuperação e defensivos na desaceleração. O risco é errar fase e timing.
### Arbitragem quantitativa

Modelos procuram padrões de preço, fatores ou relações estatísticas e montam posições compradas e vendidas. Exemplo: negociar convergência entre ações historicamente relacionadas.

“Arbitragem” pode não ser sem risco: relações quebram, dados têm vieses, custos consomem o sinal e posições concorridas podem sofrer saída simultânea.
### Short bias

Mantém viés líquido vendido e tende a ganhar em quedas. Exige identificar fraudes, deterioração ou sobrevalorização. A perda em uma posição vendida é teoricamente ilimitada, além de haver custo e chamada do aluguel.
### Event driven

- **Activist:** compra participação para pressionar por mudanças operacionais, financeiras ou de governança.
- **Restructuring:** investe em empresas em reorganização, apostando na recuperação de valor; envolve risco jurídico e de insolvência.
- **Merger arbitrage:** compra a empresa-alvo e, quando aplicável, vende a adquirente para capturar o spread até o fechamento da operação.

No merger arbitrage, o spread remunera tempo, financiamento e risco de a operação não ocorrer. Quanto maior a incerteza regulatória ou financeira, maior tende a ser o spread — e a perda potencial.

## 1.4 Fundos de Fundos de Renda Variável

O FoF seleciona fundos e gestores em vez de escolher diretamente todas as ações. Avalie filosofia, equipe, processo, carteira, risco, capacidade, liquidez, custos, desempenho por ciclo e consistência com o mandato.

Na due diligence, separe análise **qualitativa** — pessoas, governança, controles e repetibilidade — da **quantitativa** — retorno, volatilidade, drawdown, beta, fatores, correlação e atribuição.

Verifique operações, administrador, custodiante, auditoria, precificação, compliance, conflitos, continuidade e tratamento de resgates. Retorno passado isolado pode refletir sorte, fator favorecido ou risco oculto.

Limitações: dupla camada de taxas, menor transparência, defasagem de posições, risco de sobreposição e liquidez incompatível. Cinco fundos diferentes podem possuir as mesmas ações e não diversificar de verdade.

Em FoFs ASG, compare políticas e evidências de cada fundo: integração no processo, métricas, voto, engajamento, controvérsias e coerência entre discurso e carteira.

## 1.5 Estruturação das áreas de análise

**Análise fundamentalista** estima valor com base em negócio, demonstrações financeiras, setor, gestão, riscos e fluxo de caixa. **Análise técnica** estuda preço e volume para identificar tendência, força e possíveis pontos de entrada ou saída.

Na abordagem **bottom up**, começa-se pela empresa: produto, vantagem competitiva, balanço, lucro e valuation. Na **top down**, começa-se por cenário global, macroeconomia e setores, chegando depois às ações.

Relatórios de corretoras, consultorias e provedores aceleram a pesquisa, mas são insumos de terceiros: valide premissas, conflitos, data, método e independência. A decisão e a responsabilidade continuam com o gestor.

Integração ASG no valuation significa traduzir temas materiais em receita, margem, CAPEX, custo de capital, probabilidade de eventos ou valor terminal. Exemplo: multa ambiental provável reduz caixa; boa governança pode reduzir risco, sem justificar prêmio automático.

Uma área robusta separa produção de tese, revisão crítica, decisão, execução e controle de risco, registra premissas e mantém barreiras para informação relevante ainda não pública.

## 1.6 Análise Técnica
### Premissas, vantagens e desafios

Premissas usuais: o preço desconta informações disponíveis; preços se movem em tendências; padrões de comportamento podem se repetir. São hipóteses de trabalho, não leis.

Vantagens: regras objetivas, leitura rápida de mercado, disciplina e aplicação a vários horizontes. Desafios: sinais falsos, atraso, excesso de ajuste ao passado, mudança de regime, custos e influência da liquidez.
### Indicadores de tendência

- **Médias móveis:** suavizam preços e mostram direção; preço acima da média ou média curta cruzando a longa sugere força de alta, com atraso.
- **MACD:** diferença entre médias exponenciais e sua linha de sinal; cruzamentos e divergências indicam mudança de momentum da tendência.
- **Envelopes:** faixas percentuais fixas ao redor de uma média; mostram afastamento do preço e possíveis extremos, mas não provam reversão.
- **Bandas de Bollinger:** faixas ajustadas pela volatilidade ao redor da média; alargamento indica maior volatilidade e estreitamento, compressão.
- **Movimento direcional (DI+/DI− e ADX):** DI indica direção dominante; ADX mede força da tendência, não se ela é de alta ou baixa.
### Indicadores de reversão

- **IFR/RSI:** oscilador de 0 a 100 que mede força recente; leituras altas/baixas sugerem sobrecompra/sobrevenda, não ordem automática de venda/compra.
- **Estocástico:** compara fechamento com a faixa recente; mostra momentum e possíveis extremos, sendo mais útil em mercados laterais.
- **SAR parabólico:** pontos mudam de lado em relação ao preço; ajudam a seguir tendência e definir stop, mas geram ruído em lateralização.
### Indicadores de volume

- **OBV:** soma volume em dias de alta e subtrai em dias de baixa; confirma acumulação/distribuição e divergências entre preço e volume.
- **Média móvel de volume:** compara volume atual com padrão recente; rompimento com volume acima da média tende a ter mais confirmação.

Nunca use indicador isolado como certeza. Combine contexto, tendência, volume, gestão de risco, liquidez e tamanho de posição.

## Dicas para a prova

1. Associe estratégia a objetivo: passiva replica, ativa supera benchmark, agnóstica busca retorno absoluto.
2. Diferencie tracking difference (diferença de retorno) de tracking error (variabilidade do desvio).
3. Lembre que market neutral exige neutralizar riscos, não apenas igualar valores comprados e vendidos.
4. Em ETF ASG e FoF ASG, procure metodologia e evidência, não apenas o rótulo.
5. Em venda a descoberto, destaque perda potencialmente ilimitada, aluguel e chamadas de margem.
6. ADX mede força; DI+/DI− ajudam a indicar direção. Bandas medem volatilidade, não previsão garantida.
7. Questões com “sempre”, “garantido” ou “sem risco” costumam esconder erro conceitual.
8. Compare desempenho líquido de custos, ajustado ao risco e em horizonte coerente com a estratégia.

## Checklist de estudo

- [ ] Consigo comparar passiva, ativa e agnóstica por objetivo, risco, custo e benchmark.
- [ ] Sei explicar fundos indexados, futuros, swaps e ETFs, incluindo riscos operacionais.
- [ ] Distingo full replication, amostragem estratificada e otimização.
- [ ] Reconheço estilos long only e estratégias long-short, quantitativas e event driven.
- [ ] Sei avaliar um FoF, fazer perguntas de due diligence e identificar dupla cobrança e sobreposição.
- [ ] Distingo análise técnica de fundamentalista e bottom up de top down.
- [ ] Consigo integrar um fator ASG a fluxo de caixa, custo de capital ou valor terminal.
- [ ] Explico, em uma frase, o que cada indicador técnico informa e sua principal limitação.
- [ ] Resolvo questões identificando objetivo, fonte de retorno, benchmark, risco e custo.
- [ ] Reviso erros e justifico por que cada alternativa incorreta está errada.

# FIDC — direitos creditórios e estrutura de tranches

## Uma carteira de recebíveis exige provar cada elo

FIDC compra direitos de receber valores no futuro. A análise começa antes da taxa: existe crédito válido, quem deve, quem cede, a cessão transfere o direito, o pagamento será identificado e direcionado corretamente? Uma carteira com taxa alta pode estar remunerando inadimplência, fraude, documentação fraca, concentração ou custo operacional elevado.

## Originação e lastro

Mapeie cedente, devedor, originador, agente de cobrança, custodiante/registradora e fluxo de cessão. Verifique elegibilidade, existência, titularidade, formalização, documentação, cadeia de cessões, duplicidade, registro, concentração e conciliação. O gestor deve estruturar e monitorar conforme responsabilidades da RCVM 175, Anexo II; prestadores têm deveres específicos. Leia o texto consolidado atualizado, inclusive alterações do Anexo II.

Dados mínimos por recebível: identificador pseudonimizado, valor, vencimento, taxa/indexador, status, devedor/originador, garantia, pagamento e eventos. Proteja dados pessoais e evidências. Uma prova criptográfica de integridade não prova validade jurídica nem qualidade do crédito.

Trace um recebível desde a venda ou serviço que o originou até o pagamento. Verifique contrato, nota fiscal, comprovante de entrega ou prestação, aceite, identificação do devedor, vencimento, cessões anteriores, gravames, disputa comercial e dados de liquidação. A documentação deve permitir demonstrar existência, titularidade e valor exigível. Arquivo recebido não equivale a crédito validado.

Faça reconciliação entre sistemas do cedente, registradora, custodiante, agente de cobrança e extrato bancário. Investigue divergências e atrasos. Teste duplicidade por identificadores e padrões, alteração de dados bancários e concentração inesperada. Controles automatizados reduzem trabalho repetitivo, mas exceções precisam de investigação humana e trilha de auditoria.

## Modelagem de crédito

\(EL=PD\times LGD\times EAD\) é aproximação. Modele curvas de atraso, default, recuperação, pré-pagamento, diluição, recompra, concentração, correlação e tempo de recuperação. Perda líquida e excesso de spread devem ser simulados por safra e cenário. Teste defasagem temporal entre cobrança e distribuição.

PD é probabilidade de default no horizonte; LGD é parcela perdida após recuperação; EAD é exposição no momento do default. Se PD = 3%, LGD = 60% e EAD = R$ 10 milhões, a perda esperada simplificada é R$ 180 mil. Essa média não informa perda em cenário severo nem o momento da perda. Estime por safra e perfil e considere a incerteza dos parâmetros.

Meça atraso por faixas, inadimplência, pré-pagamento, recuperação, recompra, diluição, cancelamento e concentração. Defina denominadores e coortes: inadimplência acumulada de uma safra não é comparável a atraso mensal se períodos e critérios diferem. Analise safras para separar deterioração recente de mudanças na composição da originação.

A taxa histórica pode parecer boa porque a carteira é jovem ou porque créditos problemáticos foram substituídos/recomprados. Observe perdas líquidas, tempo de recuperação, renegociações e critérios de baixa. Modele aumento de atrasos, queda de recuperação e concentração; não extrapole médias sem considerar mudanças de política e ciclo econômico.

## Classes e subordinação

Classes sênior, mezanino e subordinada têm ordem de absorção/distribuição definida nos documentos. Indicador de subordinação = saldo subordinado elegível / saldo total ou denominador contratual; siga definição exata. Gatilhos podem direcionar caixa para amortização, bloquear distribuições ou declarar evento. Avalie servicer backup, conta vinculada e continuidade operacional.

Em uma estrutura hipotética de R$ 100 milhões, R$ 70 milhões são sênior e R$ 30 milhões subordinados. Perdas elegíveis podem consumir primeiro a subordinação conforme a waterfall; depois, podem atingir outras classes. Subordinação de 30% não garante proteção absoluta de 30%: despesas, juros, amortizações, recuperações, correlação e regras contratuais alteram a cobertura. Simule a estrutura ao longo do tempo, não apenas no balanço inicial.

Um gatilho pode redirecionar recebimentos para amortizar sênior ou suspender distribuição subordinada se inadimplência ou cobertura ultrapassar limites. Leia definição, período de teste, fonte de dados, cura e consequência. A classe subordinada pode ter retorno esperado maior porque absorve perdas primeiro; esse retorno não é gratuito.

O agente de cobrança/servicer emite instruções, recebe, identifica, concilia e repassa valores. Falha operacional pode gerar desvio ou atraso mesmo que o devedor tenha pago. Examine segregação de contas, continuidade em substituição do prestador, conciliação, acessos, incidentes e evidências de repasse. Atraso na arrecadação pode produzir descasamento mesmo se o crédito vier a ser pago mais tarde.

Yield dos créditos não equivale à rentabilidade líquida da cota. Despesas, perdas, atrasos, caixa parado, subordinação e preço de aquisição afetam retorno. Compare taxa contratual, taxa esperada após perdas e retorno recebido. A cota subordinada pode perder grande parte do capital.

Antes do investimento, leia regulamento, política de crédito, critérios de elegibilidade, contratos de cessão, relatórios de carteira, testes de lastro, auditoria e eventos de desenquadramento. Após investir, monitore dados, concentração, prestadores e covenants. A análise é contínua, não uma diligência única.

## Covenants e monitoramento

Acompanhe inadimplência, atraso, pré-pagamento, concentração, diluição, recompra, saldo elegível, subordinação, caixa, excesso de spread, qualidade de dados e exceções de lastro. Valide cálculo independentemente; preserve trilha de alterações, lote, fonte e hora. Rating é insumo, não substituto da diligência.

## Riscos

Fraude de recebíveis, documentação inválida, cessão ineficaz, concentração, co-mingling, falha do servicer, risco de contraparte bancária, taxa/descasa, liquidez secundária, recuperação judicial, LGPD, cibersegurança e atualização regulatória. Estruture testes de continuidade e evento de substituição do prestador.

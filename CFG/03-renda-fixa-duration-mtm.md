# Renda fixa, duration e marcação a mercado

## O que significa “renda fixa”

O nome não quer dizer que o preço fica parado nem que o retorno é conhecido em qualquer horizonte. Em geral, significa que a regra de remuneração é definida por contrato: taxa prefixada, índice de preços mais spread ou taxa flutuante. O investidor ainda enfrenta risco de mercado, crédito, liquidez, reinvestimento e condições contratuais. O valor da posição pode oscilar todos os dias antes do vencimento.

## Preço e rendimento

O preço de um título é o valor presente dos fluxos prometidos, descontados por taxas coerentes com moeda, risco, prazo e liquidez:

## Como calcular e interpretar o preço

Para um título que paga cupons $C_t$ e principal $F$ no vencimento $n$, uma representação simplificada é $P=\sum_{t=1}^{n}C_t/(1+y)^t+F/(1+y)^n$. Se as taxas variam por vencimento, use a taxa apropriada a cada fluxo, ou uma curva de desconto coerente. Convenções de dias úteis, indexação e capitalização do contrato podem exigir cálculo diferente da fórmula didática.

Considere título hipotético com valor de face R$ 1.000, cupom anual de 8% (R$ 80) e vencimento em dois anos. Com taxa de mercado de 8% a.a., o preço é $80/1{,}08+1.080/1{,}08^2=R\$1.000$. Se a taxa exigida subir para 10%, o preço cai para aproximadamente R$ 965,29. Os pagamentos prometidos não mudaram; mudou o valor presente que o mercado atribui a eles.

Marcação a mercado registra a posição pelo valor que seria observado ou estimado na data, usando preços e curvas pertinentes. É necessária para medir patrimônio e risco de forma atual. A queda contábil não significa necessariamente que o emissor deixou de pagar, mas também não deve ser ignorada: pode afetar resgates, garantias, limites, rebalanceamento e o custo de oportunidade de manter o ativo.

## Duration e convexidade sem atalhos

Duration de Macaulay pondera as datas dos fluxos pelos valores presentes relativos. Um fluxo único que vence em cinco anos tem Macaulay igual a cinco anos; cupons recebidos antes reduzem a média. Duration modificada traduz essa média em sensibilidade aproximada do preço a mudanças pequenas na yield. Com capitalização anual, $D_{mod}=D_{Mac}/(1+y)$.

Se duration modificada for 3,5, uma alta de 1 ponto percentual na taxa sugere, numa aproximação linear, queda de cerca de 3,5% no preço. Para queda de taxa da mesma magnitude, a aproximação indica alta de 3,5%, mas a relação real é convexa: normalmente a alta de preço em uma queda de taxa excede a perda correspondente em uma alta de taxa. Uma forma de corrigir é $\Delta P/P\approx-D_{mod}\Delta y+\frac12 Conv(\Delta y)^2$.

Duration pressupõe que a mudança relevante pode ser resumida por uma variação da taxa. Curvas podem se inclinar, achatar ou mudar em pontos específicos. Para carteiras com cupons variáveis, opções, indexação ou crédito, medidas mais completas podem ser necessárias. Além disso, duration não é prazo de vencimento, não mede diretamente default nem iliquidez.

## Risco de crédito e spread

O spread é a remuneração acima de uma referência, e pode refletir risco de crédito, liquidez, prêmio por prazo, estrutura do instrumento e oferta e demanda. Para analisar crédito, pergunte: quem deve pagar? De que fonte virá o caixa? Qual prioridade de pagamento? Que garantias existem? Há subordinação, covenants, vencimentos concentrados ou risco de refinanciamento? Recuperação em caso de inadimplência pode ser muito menor que o valor contratado.

Rating resume opinião sobre risco de crédito em escala e metodologia determinadas; não é recomendação de compra, garantia de pagamento nem substituto da análise. Pode mudar com atraso e depende das informações disponíveis. Leia fatores positivos e negativos, horizonte, cenário de estresse e limitações do rating.

## Risco de reinvestimento, liquidez e carregamento

Um título com cupom devolve caixa antes do vencimento. O retorno realizado depende da taxa à qual esses cupons podem ser reinvestidos. Títulos longos sem cupom têm maior sensibilidade às taxas; títulos com cupom alto devolvem capital mais cedo, mas carregam maior incerteza de reinvestimento. O preço de venda também depende de compradores disponíveis e do tamanho negociado: spread indicativo não significa que toda posição possa ser liquidada naquele nível.

Ao comparar alternativas, decomponha retorno esperado em carregamento (cupom e passagem do tempo), mudança de curva, mudança de spread, reinvestimento e custos. Essa decomposição esclarece por que “taxa contratada” e “retorno da carteira” não são sinônimos.

$$P=\sum_{t=1}^{n}\frac{FC_t}{(1+y)^t}.$$

Se o cupom fixo é menor que a taxa de mercado, o título tende a negociar abaixo do par; se maior, acima. Para um título sem cupom, \(P=VN/(1+y)^n\). A relação preço–yield é inversa e convexa.

## Marcação a mercado (MtM)

MtM atualiza posições para preço justo/representativo na data de referência, incorporando curva de juros, spreads de crédito, indexadores, liquidez e características do instrumento. Ela não é “perda realizada”: uma venda antes do vencimento cristaliza o preço de saída; manter até o vencimento tampouco garante retorno contratual se houver default, custos, imposto ou venda antecipada. Marcação na curva usa apropriação do rendimento contratual em certos contextos permitidos, mas não deve esconder preço econômico, liquidez ou risco. Regime contábil e regra do fundo importam.

Uma alta na taxa de desconto reduz o valor presente de fluxos futuros. Para uma posição com valor presente \(P\), duration modificada \(D_{mod}\) aproxima:

$$\frac{\Delta P}{P}\approx-D_{mod}\Delta y.$$

Exemplo: duration 4,1 e choque paralelo +0,50 p.p. (=0,005) implicam perda aproximada de 2,05%. É aproximação local, pressupõe deslocamento pequeno e paralelo e ignora convexidade, spread e mudanças de fluxos.

## Duration de Macaulay e modificada

Duration de Macaulay é média ponderada dos prazos de recebimento, com pesos iguais ao valor presente de cada fluxo dividido pelo preço:

$$D_{Mac}=\sum_{t=1}^{n}t\,\frac{PV(FC_t)}{P};\quad D_{mod}=\frac{D_{Mac}}{1+y/m}.$$

Com pagamentos anuais, \(m=1\). Um título zero cupom tem duration igual ao vencimento. Cupom maior normalmente reduz duration; rendimento maior normalmente reduz duration, mantidos os demais fatores. Duration não é maturidade: é sensibilidade de primeira ordem ao yield.

## Convexidade

A aproximação de segunda ordem é:

$$\frac{\Delta P}{P}\approx-D_{mod}\Delta y+\frac{1}{2}C(\Delta y)^2.$$

Convexidade positiva melhora a estimativa para movimentos maiores em muitos títulos tradicionais. Opções embutidas podem gerar convexidade negativa (ex.: certos títulos resgatáveis), então não generalize.

## Risco de crédito e spread

Risco de crédito inclui probabilidade de inadimplência, perda dado default e exposição no default. Aproximação de perda esperada: \(EL=PD\times LGD\times EAD\). Spread compensa um conjunto de fatores: risco de crédito, liquidez, prêmio de risco, impostos e oferta/demanda; não é igual a probabilidade de default. Migração de rating pode afetar preço sem ocorrer default. Análise deve cobrir capacidade de pagamento, garantias, senioridade, covenants, concentração e recuperação.

Duration de spread mede sensibilidade a spread; duration de juros mede exposição à curva livre de risco. Em crédito privado, separar os dois fatores ajuda a explicar P&L.

## Curva, indexadores e riscos

Prefixado: exposição ao nível/forma da curva. Pós-fixado CDI/Selic: menor duration de taxa básica, mas pode carregar risco de spread, crédito e liquidez. IPCA+: exposição à taxa real e à inflação realizada/acumulada. Curvas não se movem sempre paralelas: use key-rate durations para nós específicos. Inclua basis risk entre indexadores e descasamento de datas.

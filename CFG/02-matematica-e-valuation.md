# Matemática financeira e valuation

## Como ler uma conta financeira

Uma fórmula financeira descreve dinheiro em datas diferentes. Antes de calcular, escreva: (1) qual valor é conhecido, (2) quando cada fluxo ocorre, (3) qual taxa remunera o risco e o tempo, (4) qual convenção de capitalização e unidade temporal está sendo usada. Se o fluxo é mensal, taxa anual precisa ser convertida; se há risco de crédito, a taxa de desconto precisa refletir a remuneração exigida para aquele risco, sem misturar prêmio já embutido duas vezes.

## Valor do dinheiro no tempo

Capitalização composta: \(VF=VP(1+i)^n\). Desconto: \(VP=VF/(1+i)^n\). Taxas só podem ser comparadas depois de compatibilizar período e regime. Taxa efetiva anual equivalente à mensal \(i_m\): \((1+i_m)^{12}-1\), não simplesmente \(12i_m\), salvo aproximação de juros simples.

Exemplo: R$ 1.000 aplicados a 1% ao mês por 12 meses resultam em $1.000(1{,}01)^{12}=R\$1.126{,}83$. A taxa efetiva anual correspondente é 12,68%. Dizer “12% ao ano” poderia significar taxa nominal com capitalização mensal ou taxa efetiva anual; por isso o contrato precisa deixar claro o regime. Em cálculos de prova, identifique período e convenção antes de substituir valores.

### Anuidade e fluxo irregular

Uma anuidade é uma sequência de pagamentos iguais em intervalos iguais. Para pagamentos ao fim do período, seu valor presente é $VP=PMT\,[1-(1+i)^{-n}]/i$. Se os pagamentos ocorrem no início, cada fluxo fica um período mais próximo e o valor presente da anuidade antecipada é maior por um fator $(1+i)$. A fórmula de anuidade não serve automaticamente para fluxos irregulares; nesses casos, desconte cada parcela: $VP=\sum_{t=1}^{n}FC_t/(1+i)^t$.

Exemplo: receber R$ 100 no fim de cada um dos próximos três anos, descontando a 10% a.a., vale aproximadamente R$ 248,69 hoje: $100/1{,}1+100/1{,}1^2+100/1{,}1^3$. O valor é menor que R$ 300 porque se abre mão de usar o dinheiro hoje e porque o risco é remunerado pela taxa assumida.

## Títulos e taxa interna de retorno

Preço e taxa de retorno de um título são conceitos ligados. Mantidos os fluxos prometidos, elevar a taxa de desconto reduz o valor presente; por isso preço e yield movem-se em sentidos opostos. A **yield to maturity** é a taxa que iguala o preço observado ao valor presente dos pagamentos prometidos, sob hipóteses de pagamento integral e reinvestimento dos cupons à mesma taxa. Ela não é promessa de retorno realizado: inadimplência, venda antes do vencimento, reinvestimento e custos mudam o resultado.

Para um título com preço de R$ 950 e recebimento único de R$ 1.000 em um ano, a yield anual efetiva é $1.000/950-1=5{,}26\%$. Se a taxa de mercado comparável subir, o preço desse fluxo fixo cai. Se o investidor levar ao vencimento e houver pagamento integral, o retorno depende do preço de compra e do fluxo efetivamente recebido, e não da cotação intermediária.

## VPL e TIR: critérios para projetos

O **Valor Presente Líquido (VPL)** soma o investimento inicial negativo e os fluxos futuros descontados por uma taxa que represente custo de capital e risco: $VPL=\sum_{t=0}^{n}FC_t/(1+k)^t$. VPL positivo indica que, dadas as premissas e taxa $k$, o projeto cria valor acima da remuneração requerida. Não garante que as premissas se realizarão. Faça sensibilidades para preço, volume, prazo, custo e taxa.

A **Taxa Interna de Retorno (TIR)** é a taxa que zera o VPL. Ela é intuitiva como percentual, mas pode gerar múltiplas soluções se os fluxos alternarem de sinal várias vezes e pode ordenar mal projetos mutuamente excludentes de escalas ou prazos distintos. Quando VPL e TIR entram em conflito, examine escala, duração, reinvestimento implícito e premissas; para criação de valor, VPL a uma taxa coerente costuma ser o critério mais direto.

Exemplo: projeto custa R$ 100 hoje e paga R$ 60 ao fim de cada um dos próximos dois anos. A 10% a.a., $VPL=-100+60/1{,}1+60/1{,}1^2=R\$4{,}13$. A TIR fica acima de 10% (aproximadamente 13,1%). Se o custo estimado subir ou os recebimentos atrasarem, o VPL pode ficar negativo. Mostre a sensibilidade em vez de reportar apenas um número central.

## Duração como sensibilidade de preço

Duration também aparece como conceito de prazo médio ponderado e como aproximação da sensibilidade do preço à taxa. Para variação pequena, $\Delta P/P\approx-D_{mod}\,\Delta y$, onde $D_{mod}$ é duration modificada e $\Delta y$ está em forma decimal. Se $D_{mod}=4$ e a taxa subir 0,50 ponto percentual, a aproximação aponta queda de cerca de 2% no preço. Convexidade corrige a aproximação para movimentos maiores. Duration não mede risco de crédito, liquidez nem garante que a curva se mova paralelamente.

## Erros que alteram a resposta

- Converter uma taxa nominal como se fosse efetiva ou misturar taxa mensal e anual.
- Usar o número do período sem verificar se a primeira parcela ocorre no início ou no fim.
- Descontar fluxo nominal por taxa real, ou vice-versa.
- Tratar TIR como retorno garantido e esquecer o calendário dos fluxos.
- Confundir taxa de cupom com yield: cupom é regra de pagamento; yield depende também do preço pago.
- Apresentar valor calculado sem explicar as premissas e a unidade.

Fluxo de caixa descontado:

$$VP=\sum_{t=1}^{n}\frac{FC_t}{(1+k)^t}.$$

Títulos com fluxos intermediários exigem desconto de cada pagamento. Em datas irregulares, use fração de período consistente com convenção de dias e contrato.

## VPL/NPV e TIR/IRR

\(VPL=\sum_{t=0}^{n}FC_t/(1+k)^t\). Aceita-se economicamente um projeto independente se VPL > 0, dadas premissas e taxa de desconto apropriadas. TIR é a taxa que zera o VPL. Pode haver múltiplas TIR quando os sinais dos fluxos alternam mais de uma vez; para projetos mutuamente exclusivos, VPL na taxa de oportunidade é critério mais robusto. TIR pressupõe reinvestimento implícito e pode distorcer comparação por escala ou timing.

## Retorno e estatística

Retorno simples \(R=P_1/P_0-1\). Retorno logarítmico \(\ln(P_1/P_0)\), aditivo no tempo. Média aritmética estima retorno de um período; geométrica descreve crescimento composto histórico. Variância mede dispersão quadrática; desvio-padrão é sua raiz. Correlação varia entre −1 e +1 e mede co-movimento linear, não causalidade nem proteção em todo cenário.

## Exemplo

Investimento de R$ 100 mil hoje e recebimento de R$ 60 mil em cada um dos próximos dois anos, taxa de 10% a.a.: \(VPL=-100+60/1{,}1+60/1{,}1^2=\) R$ 4,13 mil (aprox.). O projeto supera o hurdle rate nas premissas, mas ainda depende de risco, liquidez, impostos, custos e cenários.

## Erros comuns

Misturar taxa nominal e efetiva; descontar FCFF pelo custo do equity; usar taxa real com fluxo nominal; confundir retorno acumulado com anualizado; interpretar volatilidade passada como perda máxima possível. Documente moeda, periodicidade, datas, convenção de dias, impostos e premissas.

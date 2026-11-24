# Stablecoins: regulamentação e regras de transação no Brasil

## O que está sendo regulado

Stablecoin é um ativo virtual que busca manter valor estável por referência a outro ativo — tipicamente moeda fiduciária (USDT, USDC em dólar; projetos em real). A regulação brasileira não usa a palavra "stablecoin": a **Resolução BCB 521/2025** fala em **ativos virtuais referenciados em moeda fiduciária**, categoria que captura USDT e USDC sem depender de rótulo de mercado.

```text
Stablecoin
   │
   ├── referenciada em moeda fiduciária estrangeira (USDT, USDC)
   │        → BCB: tratada como operação de câmbio (Res. 521/2025)
   │
   ├── referenciada em real (BRL)
   │        → tende a moeda eletrônica → régua CMN/BCB de pagamentos
   │
   └── lastreada em outros ativos (commodity, cripto, algorítmica)
            → avaliação caso a caso; pode virar valor mobiliário (CVM)
```

## Base legal

- **Lei 14.478/2022** — marco legal dos criptoativos: define ativo virtual e prestadora de serviços de ativos virtuais, exige autorização e subordina a fiscalização ao órgão designado pelo Poder Executivo.
- **Decreto 11.563/2023** — designou o BCB como regulador das PSAVs e disciplinou a autorização.
- **Resoluções BCB 519, 520 e 521/2025** — arcabouço definitivo: autorização, funcionamento e enquadramento cambial das operações com ativos virtuais (detalhado em [07](07-orgaos-reguladores-e-normas.md)).
- **IN RFB 1.888/2019** — declaração obrigatória de operações com criptoativos; **Lei 14.754/2023** — tributação de aplicações no exterior, que alcança cripto mantido fora de corretoras nacionais.

## Como a Resolução BCB 521/2025 trata as stablecoins

A resolução alterou o mercado de câmbio (Resoluções BCB 277, 278 e 279) e passou a tratar como **operação de câmbio** quatro tipos de serviço com ativos virtuais:

| Operação | Tratamento |
|---|---|
| Pagamento ou transferência internacional com ativos virtuais | Câmbio |
| Transferência para obrigações de uso internacional de cartão ou outro meio eletrônico de pagamento | Câmbio |
| Transferência de/para **carteira autocustodiada**, mesmo sem pagamento internacional | Câmbio |
| **Compra, venda ou troca de ativos virtuais referenciados em moeda fiduciária** | Câmbio — é aqui que a stablecoin entra |

Consequência prática: comprar USDT com reais numa corretora brasileira deixou de ser "apenas uma troca de tokens" — é uma operação do mercado de câmbio, com a régua correspondente.

## Regras de transação

| Regra | Conteúdo |
|---|---|
| Quem pode operar | Bancos e CEF (como PSAVs), corretoras de câmbio, CTVM/DTVM, financeiras e SPSAVs autorizadas; instituição não autorizada não presta o serviço. |
| Limites por operação | Pagamento/transferência internacional com ativos virtuais cuja contraparte **não** é autorizada a operar em câmbio: até **US$ 100 mil** para SPSAV e até **US$ 500 mil** para bancos, corretoras de câmbio, CTVM/DTVM e financeiras (conforme a categoria da prestadora na Res. BCB 277 alterada). |
| Moeda em espécie | **Vedada** para SPSAVs, nacional ou estrangeira. |
| Pagamento em moeda estrangeira | Vedado comprar/vender ativos virtuais com pagamento ou recebimento em moeda estrangeira, inclusive em livro de negociação. |
| Carteiras autocustodiadas | Permitidas, mas a PSAV deve **identificar o titular** da carteira e monitorar origem e destino dos ativos (régua PLD/FT da Circular BCB 3.978/2020). |
| Reporte ao BCB | Obrigatório a partir de **4 de maio de 2026**; dados consolidados das operações até o dia 5 do mês seguinte, com finalidade e beneficiário. |
| Vigência | Entrada em vigor em **2 de fevereiro de 2026**; PSAVs já em atividade passam por autorização em duas fases (Res. 519). |

## Stablecoin em BRL e moeda eletrônica

Uma stablecoin denominada em real emitida com promessa de resgate à par tende ao conceito de **moeda eletrônica** da Lei 12.865/2013 — território do arranjo de pagamento, não do ativo virtual livre. Sob a Resolução BCB 520/2025, a *intermediária* de ativos virtuais pode emitir moeda eletrônica como atividade adicional, sujeita às regras do BCB e da CVM conforme a competência. Na prática:

- emissor de stablecoin BRL precisa ser instituição autorizada (IP emissora de moeda eletrônica ou SPSAV habilitada);
- lastro e resgate exigem segregação patrimonial e prova de reservas;
- integração com Pix/Drex é o caminho natural de liquidação — ver [DvP e liquidação](02-dvp-e-liquidacao.md).

## Transfronteiriço e autocustódia

Dois pontos mudam o desenho de produto:

1. **Remessas internacionais com stablecoin** são câmbio: exigem prestadora autorizada, identificação de ponta a ponta e observância dos limites quando a contraparte estrangeira não é autorizada. P2P puro fora de instituição regulada continua possível tecnicamente, mas sai do perímetro protegido e cria deveres de declaração (IN RFB 1.888) e tributários (Lei 14.754/2023) para o usuário.
2. **Wallet própria (self-custody)** não foi banida: a regra joga o ônus sobre a PSAV, que precisa saber quem controla o endereço de destino/origem — modelo parecido com a "travel rule" do GAFI/FATF.

## Checklist para um fluxo de stablecoin regulado

- [ ] Contraparte é PSAV/SPSAV autorizada ou instituição habilitada a prestar o serviço?
- [ ] A operação é câmbio (fiat-referenciada, internacional ou autocustódia)? Se sim, limites e reporte se aplicam.
- [ ] Titular da carteira de destino/origem identificado (inclusive autocustodiada)?
- [ ] Sem espécie e sem liquidação em moeda estrangeira na ponta brasileira?
- [ ] Segregação patrimonial e prova de reservas do custodiante/emissor verificadas?
- [ ] Obrigações acessórias (IN RFB 1.888, ganho de capital/Lei 14.754) endereçadas?

## Ligação com o restante da trilha

Stablecoin regulada é a **perna de caixa** do DvP brasileiro até que o Drex assuma esse papel: o estudo [02](02-dvp-e-liquidacao.md) modela a liquidação atômica e este documento define quem pode carregar o lado do dinheiro dentro da lei. Para o fundo tokenizado do estudo [04](04-fundo-infra-tokenizado.md), subscrição e resgate em stablecoin BRL exigem exatamente as peças acima: emissor autorizado, custódia segregada e reporte.

> Material educacional, consolidado até novembro de 2026. O regime é recente (vigência iniciada em fevereiro de 2026) e sujeito a instruções normativas e alterações posteriores: confirme sempre o texto vigente das Resoluções BCB 519, 520 e 521 e a orientação profissional antes de estruturar qualquer operação.

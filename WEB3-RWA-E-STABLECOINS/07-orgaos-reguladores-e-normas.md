# Órgãos reguladores e normas da tokenização e do mercado cripto

## Quem regula o quê

Três órgãos formam o núcleo regulatório da tokenização de investimentos no Brasil. Eles não concorrem entre si: cada um atua em uma camada diferente da pilha, e um mesmo produto tokenizado pode ser supervisionado pelos três ao mesmo tempo.

```text
        CMN (Conselho Monetário Nacional)
        │  define diretrizes e a política — não fiscaliza diretamente
        ▼
┌───────────────────┬───────────────────┐
│ BCB (Banco Central)│ CVM               │
│ moeda, pagamentos, │ valores           │
│ câmbio, IFs, PSAVs │ mobiliários,      │
│                    │ fundos, ofertas   │
└───────────────────┴───────────────────┘
        │                        │
        └────────┬───────────────┘
                 ▼
   RF (receita e obrigações acessórias)
   COAF (inteligência PLD/FT)
```

| Órgão | Natureza | Papel na tokenização |
|---|---|---|
| CMN | Conselho normativo do SFN (Lei 4.595/1964) | Fixa diretrizes de moeda, crédito, câmbio e capitais; edita resoluções que o BCB executa. |
| BCB (BaCen) | Autarquia executora e supervisora | Autoriza e supervisiona instituições; regula pagamentos, câmbio, moeda eletrônica, Drex e, desde a Lei 14.478/2022, as prestadoras de serviços de ativos virtuais. |
| CVM | Autarquia do mercado de valores mobiliários (Lei 6.385/1976) | Decide quando um token é valor mobiliário; regula ofertas, emissores, fundos, administradores, custodiantes e intermediários. |

A pergunta de enquadramento é sempre a mesma dos estudos anteriores: **o que o token representa juridicamente?** Se for valor mobiliário, a CVM manda na oferta e nos prestadores. Se for meio de pagamento, câmbio ou ativo virtual puro, o BCB manda. O CMN define a política que ambos executam.

## Linha do tempo regulatória

```text
1964  Lei 4.595 → cria CMN e estrutura do SFN
1976  Lei 6.385 → cria CVM e define valores mobiliários
1998  Lei 9.613 → crimes de lavagem de dinheiro (PLD)
2017  Lei 13.506 → processo administrativo sancionador de BCB e CVM
2019  IN RFB 1.888 → declaração de operações com criptoativos
2022  Lei 14.430 → registro de recebíveis e modernização dos fundos
2022  Lei 14.478 → marco legal dos criptoativos (VASPs)
2023  Decreto 11.563 → designa o BCB como regulador das PSAVs
2025  Resoluções BCB 519/520/521 → arcabouço definitivo das SPSAVs
2026  vigência do novo regime (fev/2026; reporte cambial em mai/2026)
```

## CMN — diretrizes e normas-mãe

O CMN não fiscaliza: edita **resoluções CMN** que orientam o BCB e definem limites prudenciais. Na tokenização, sua presença aparece em quatro frentes:

- **Moeda e meios de pagamento.** A competência sobre emissão de moeda eletrônica e arranjos de pagamento vem do CMN (Lei 4.595/1964; Lei 12.865/2013 para arranjos e instituições de pagamento). Stablecoin referenciada em real tende ao conceito de moeda eletrônica — território CMN/BCB.
- **Câmbio e capitais.** Resoluções CMN sobre mercado de câmbio são a base que a Resolução BCB 521/2025 estendeu para ativos virtuais (ver [Stablecoins](08-stablecoins-regulamentacao.md)).
- **Segurança cibernética.** A **Resolução CMN 4.658/2018** instituiu a política de segurança cibernética das IFs; foi **revogada e substituída pela Resolução CMN 4.893/2021**, que unificou segurança cibernética e contratação de serviços de nuvem e processamento de dados. Para plataformas de tokenização operadas por instituições reguladas, é a norma que governa cloud, DLT e provedores críticos.
- **Sandbox regulatório.** A **Resolução CMN 4.865/2020** estabeleceu diretrizes para o Ambiente Controlado de Testes de Inovações Financeiras e de Pagamento do BCB, operacionalizado pela **Resolução BCB 29/2020** (e pelos ciclos, a começar da Resolução BCB 50/2020, alterada pela 141/2021). Complementa, não revoga, o sandbox da CVM — cada um no seu perímetro.

Normas CMN/BCB relevantes por processo:

| Processo | Norma | Efeito |
|---|---|---|
| PLD/FT e KYC | Circular BCB 3.978/2020 | Consolidou a disciplina de prevenção à lavagem e ao financiamento do terrorismo para instituições autorizadas, **revogando** as Circulares 3.461/2009, 3.542/2012 e demais normas esparsas. Base do KYC/KYB on-chain do estudo [03](03-custodia-identidade-compliance.md). |
| Alerta sobre cripto | Comunicados BCB 25.306/2014 e 31.379/2017 | Declararam que moedas virtuais não são emitidas nem garantidas por autoridade monetária — marco de "regulação por aviso" antes da lei. |
| Moeda eletrônica | Resolução BCB 80/2021 | Requisitos das contas de pagamento e da emissão de moeda eletrônica pelas IPs — régua contra a qualquer stablecoin em BRL tende a ser medida. |
| Open Finance | Resolução Conjunta CMN/BCB 1/2020 | Compartilhamento de dados — relevante quando a plataforma tokenizada precisa agregar posição financeira do investidor. |
| Capital mínimo SPSAV | Resolução Conjunta CMN/BCB 14/2025 | Fixa requerimentos mínimos de capital e patrimônio líquido exigidos pela Resolução BCB 520/2025. **Complementa** o arcabouço 519/520/521. |

## BCB — execução, autorização e supervisão

O BCB executa a política do CMN e, desde o Decreto 11.563/2023, é o regulador das **prestadoras de serviços de ativos virtuais (PSAVs)** previstas na Lei 14.478/2022. O arcabouço definitivo chegou em novembro de 2025:

| Norma | Objeto | Vigência |
|---|---|---|
| Resolução BCB 519/2025 | Processos de **autorização** de SPSAVs (e de corretoras de câmbio, CTVM/DTVM): requisitos de controladores, origem lícita de recursos, capital, governança; autorização em duas fases para PSAVs já em atividade (art. 9º da Lei 14.478). | Fev/2026 |
| Resolução BCB 520/2025 | **Constituição e funcionamento** das SPSAVs: três modalidades — *intermediária*, *custodiante* e *corretora* (intermediação + custódia); segregação patrimonial, prova de reservas, auditoria; vedações (dar crédito a clientes, captar do público salvo ações, participar de outras IFs); prestação de serviços por bancos, CCF, CTVM/DTVM e corretoras de câmbio mediante comunicação + certificação técnica (Instrução Normativa BCB 701). | Fev/2026 |
| Resolução BCB 521/2025 | Enquadra serviços de ativos virtuais no **mercado de câmbio**: altera as Resoluções BCB 277, 278 e 279 e trata pagamentos internacionais, cartões, carteiras autocustodiadas e compra/venda de ativos referenciados em moeda fiduciária como operações de câmbio. | Fev/2026; reporte a partir de mai/2026 |

Pontos de atenção para o arquiteto:

- **Custódia de ativos virtuais virou atividade regulada.** O custodiante tem responsabilidade objetiva por perdas, prova de reservas e auditoria independente — o "not your keys, not your coins" agora tem tradução regulatória.
- **Autocustódia não foi proibida**, mas transferências de/para carteiras autocustodiadas entraram no perímetro cambial e exigem identificação do titular pela PSAV (ver detalhes em [08](08-stablecoins-regulamentacao.md)).
- **Drex.** O piloto do real digital e os testes de liquidação de ativos tokenizados com Drex correm sob o BCB, com regras caso a caso — infraestrutura candidata ao DvP do estudo [02](02-dvp-e-liquidacao.md).

## CVM — valores mobiliários, ofertas e fundos

A CVM decide quando um token é **valor mobiliário** pelo teste da substância econômica (captação pública + expectativa de rendimento pelo esforço de terceiros), critério consolidado no **Parecer de Orientação CVM nº 40/2022-CVM/SEP**. Sendo valor mobiliário, aplicam-se as normas de oferta, emissor, intermediários e fundos:

| Processo | Norma | Efeito e relações |
|---|---|---|
| Ofertas públicas | **Resolução CVM 160/2022** | Consolidou as regras de oferta pública de valores mobiliários e **revogou** as Instruções CVM 400/2003, 476/2009 (esforços restritos), 566/2015 e correlatas. Oferta de token-valor mobiliário ao público passa por ela — registro ou dispensa formal. |
| Crowdfunding | **Resolução CVM 88/2022** | Captação por plataforma eletrônica de investimento participativo; **revogou** a Instrução CVM 88/2017. Rota usual de ofertas tokenizadas de menor porte. |
| Fundos | **Resolução CVM 175/2022** | Reforma dos fundos; **substituiu progressivamente** a Instrução CVM 555/2014. Admite que FIFs invistam em criptoativos negociados em entidades autorizadas pelo BCB ou em jurisdição com supervisão equivalente; detalhada pelo Ofício Circular CVM/SSE nº 4/2023. Cotas tokenizadas de FII/FIDC/FIP continuam sob ela. |
| Administração e gestão | **Resolução CVM 21/2021** e **Resolução CVM 135/2022** | A 135/2022 disciplina administração de carteiras e **revogou** as Instruções CVM 306/1999 e 558/2015 — regime aplicável a administrador e gestor de fundo tokenizado. |
| Sandbox CVM | **Resolução CVM 29/2021** | Ambiente regulatório experimental de valores mobiliários; **revogou** a Instrução CVM 626/2020. Projetos como Distrito e Havan testaram emissão/registro de ativos tokenizados nesse regime. |
| Custódia e escrituração | Regras do depositário central e do escriturador (B3/registrador) | A custódia fungível de valores mobiliários segue nas entidades autorizadas; token não substitui depositário nem escriturador — reconcilia com eles (estudo [01](01-tokenizacao-rwa.md)). |

## Onde as normas se cruzam

```text
Token de cota de FIDC        → CVM 175 + CVM 160/88 (oferta) + BCB (cash leg / Drex?)
Token de recebível           → CVM 160 ou CVM 88 + Lei 14.430/2022 (registro de recebíveis)
Stablecoin em BRL            → Lei 14.478 + Res. BCB 519/520/521 + regra de moeda eletrônica
Fundos comprando BTC/ETH     → CVM 175 + ofício SSE 4/2023 + PSAV autorizada (BCB 520)
Custódia do token            → CVM (valor mobiliário) ou BCB 520 (custodiante de AV)
PLD/FT e reporte             → Lei 9.613 + Circular BCB 3.978 + IN RFB 1.888 + COAF
```

Regra prática: **mapear primeiro a natureza jurídica do token, depois o prestador**. A norma que manda no ativo (CVM) não é a mesma que manda no dinheiro e na contraparte regulada (BCB/CMN), e nenhuma dispensa as obrigações de PLD, tributárias e de proteção de dados.

## Erros comuns de leitura

- Tratar "a norma do BC sobre cripto" como única: são três resoluções com escopos distintos (autorização, funcionamento, câmbio) — citar a certa no processo certo.
- Assumir que a CVM "não regula cripto": ela regula **valor mobiliário em qualquer formato**, inclusive tokenizado.
- Confundir revogação com lacuna: RCVM 160 revogou a ICVM 400, mas consolidou — não liberou — a oferta pública.
- Esquecer o CMN: muitas exigências atribuídas "ao BC" são diretrizes CMN executadas pelo BCB.

> Material educacional e consolidado até novembro de 2026. Normas deste campo mudam rápido e podem ter sido alteradas ou revogadas após a redação: confirme sempre o texto vigente nos repositórios oficiais (normativos do BCB e legislação da CVM) e a orientação profissional aplicável antes de qualquer decisão de estruturação.

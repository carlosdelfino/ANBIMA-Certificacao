# Checklist do plano de 12 meses

Versão verificável do [plano de formação](../plano_12_meses_web3_mercado_capitais_fii_infraestrutura_rwa.md). Espelha a página **Trilha** do [Anbima Cert](https://anbima-cert.vercel.app/trilha), onde os mesmos itens podem ser marcados com persistência local.

## Competências esperadas ao final

- [ ] Entender a estrutura da indústria brasileira de fundos.
- [ ] Ler e interpretar os principais pontos da Resolução CVM 175.
- [ ] Diferenciar FII, FIP, FIP-IE, FI-Infra, FIDC e fundos tradicionais.
- [ ] Entender as funções de gestor, administrador fiduciário, custodiante, escriturador e distribuidor.
- [ ] Avaliar os fundamentos econômicos básicos de um FII.
- [ ] Interpretar indicadores como NOI, cap rate, vacância e WAULT.
- [ ] Construir modelos simples de fluxo de caixa descontado.
- [ ] Entender debêntures incentivadas e financiamento de infraestrutura.
- [ ] Calcular VPL, TIR, WACC e DSCR.
- [ ] Entender Project Finance.
- [ ] Compreender risco de crédito, duration, spreads e covenants.
- [ ] Preparar-se para a certificação CFG.
- [ ] Avaliar posteriormente CGE e/ou CGA conforme a especialização escolhida.
- [ ] Entender juridicamente a diferença entre token e valor mobiliário.
- [ ] Projetar arquiteturas de tokenização de RWA.
- [ ] Implementar mecanismos de whitelist e restrição de transferência.
- [ ] Implementar DvP — Delivery versus Payment.
- [ ] Implementar corporate actions on-chain.
- [ ] Criar uma arquitetura de fundo tokenizado experimental.
- [ ] Construir um portfólio técnico direcionado a assets, fintechs, securitizadoras e infraestrutura de mercado.

## Mês a mês

### Mês 1 — Estrutura do mercado financeiro brasileiro

- [ ] Sistema Financeiro Nacional, Banco Central, CVM, B3, ANBIMA;
- [ ] corretoras, bancos de investimento, assets;
- [ ] administradores fiduciários, custodiantes, escrituradores, distribuidores, securitizadoras;
- [ ] **Entrega:** `arquitetura-mercado-capitais.md` comparando a cadeia tradicional com a cadeia DLT.

### Mês 2 — Fundos de investimento e Resolução CVM 175

- [ ] Parte Geral, classes, subclasses, segregação patrimonial;
- [ ] prestadores de serviço, administrador fiduciário, gestor, regulamento, assembleias;
- [ ] divulgação de informações, patrimônio líquido, cotas;
- [ ] Anexo III (FII) e Anexo IV (FIP);
- [ ] **Entrega:** modelo conceitual `FundRegistry.sol` + contratos de responsabilidade.

### Mês 3 — Preparação formal para CFG

- [ ] Economia: inflação, juros, política monetária e fiscal, câmbio, PIB, ciclos;
- [ ] Matemática financeira: PV, FV, juros compostos, séries, equivalência de taxas;
- [ ] Estatística: média, variância, desvio, correlação, covariância, distribuições;
- [ ] Finanças: risco, retorno, CAPM, beta, diversificação;
- [ ] **Entrega:** `finance_math.ipynb` com fórmulas implementadas e validadas.

### Mês 4 — Fundos Imobiliários

- [ ] FII de tijolo, de papel, híbrido, desenvolvimento, FoF;
- [ ] CRI, LCI, securitização;
- [ ] Indicadores: NOI, cap rate, vacâncias, WAULT, P/VP, LTV, dividend yield, concentrações;
- [ ] **Entrega:** `fii-analyzer/` (Node + Python + React) com cadastro de FII, imóveis e locatários.

### Mês 5 — Valuation

- [ ] Valor do dinheiro no tempo, DCF, FCFF, FCFE, WACC, perpetuidade, múltiplos;
- [ ] Análise de sensibilidade; `Valor do imóvel ≈ NOI / Cap Rate`;
- [ ] Damodaran, *Investment Valuation* (seleção);
- [ ] **Entrega:** API `POST /valuation/dcf`, `/cap-rate`, `/sensitivity`.

### Mês 6 — Renda fixa e crédito privado

- [ ] Títulos prefixados, pós-fixados, IPCA+, CDI, curva de juros, MtM;
- [ ] Duration, convexidade, spread de crédito, rating, default, recovery;
- [ ] Debêntures: simples, conversíveis, incentivadas, garantias, covenants, agente fiduciário;
- [ ] **Entrega:** Bond Engine em Python + API Node (`bond_price`, `ytm`, `duration`, `convexity`, `credit_spread`).

### Mês 7 — Project Finance e infraestrutura

- [ ] SPE, concessões, PPP, non-recourse, limited recourse;
- [ ] CAPEX, OPEX, EBITDA, CFADS, DSCR, LLCR, covenants, garantias;
- [ ] Gatti, *Project Finance in Theory and Practice*;
- [ ] **Entrega:** Infrastructure Finance Simulator (NPV, IRR, DSCR, LLCR, payback, debt schedule).

### Mês 8 — FIP, FIP-IE e FI-Infra

- [ ] FIP-IE como equity → participação → SPE → projeto;
- [ ] FI-Infra como renda fixa → crédito → debêntures → infraestrutura;
- [ ] Tabela comparativa FIP-IE × FI-Infra;
- [ ] **Entrega:** Infrastructure Fund Digital Twin (oráculos, DSCR, covenants, alertas).

### Mês 9 — Tokenização de ativos reais

- [ ] Pilha jurídico → instrumento → registro → token → custódia → liquidação;
- [ ] ERC-20, 4626, 1400, 3643, 1155; EIP-712; ERC-4337;
- [ ] Whitelist, identity registry, transfer restrictions, corporate actions;
- [ ] **Entrega:** Permissioned RWA Token (ver [capítulo 1](01-tokenizacao-rwa.md)).

### Mês 10 — DvP, stablecoins e liquidação

- [ ] Atomic settlement, escrow, stablecoins, Drex/CBDC, BRL tokenizado;
- [ ] Oráculos, FX, finality, risco de contraparte;
- [ ] **Entrega:** DvP Engine com nonce, expiry, EIP-712, compliance, pause (ver [capítulo 2](02-dvp-e-liquidacao.md)).

### Mês 11 — Custódia, identidade, compliance e RegTech

- [ ] KYC, KYB, PLDFT, beneficial owner;
- [ ] Wallets custodiais/não custodiais, MPC, multisig, HSM, account abstraction;
- [ ] **Entrega:** Compliance Policy Engine (Node/TS/Postgres/Redis + PolicyRegistry.sol) (ver [capítulo 3](03-custodia-identidade-compliance.md)).

### Mês 12 — Projeto de portfólio profissional

- [ ] Tokenized Infrastructure Fund Sandbox integrando os meses anteriores;
- [ ] Dashboard com NAV, cotistas, DSCR, covenants, distribuição e auditoria on-chain;
- [ ] Estudo de caso: "Infraestrutura DLT para um Fundo de Infraestrutura Tokenizado";
- [ ] **Entrega:** repositório `tokenized-infrastructure-fund/` + documento de apresentação.

## Marcos de certificação por trimestre

| Trimestre | Marco |
|---|---|
| T1 | Iniciar preparação CFG; estudar edital vigente; fazer simulados. |
| T2 | Realizar CFG ao atingir desempenho consistente; iniciar aprofundamento de FII. |
| T3 | Escolher ênfase: CGE, CGA ou ambas em sequência. |
| T4 | Iniciar preparação da segunda certificação; consolidar projeto de portfólio. |

> Em julho de 2026 a ANBIMA prorrogou vencimentos de CFG, CGA e CGE previstos entre 2026 e 2029 para 02/01/2030 ([comunicado oficial](https://www.anbima.com.br/pt_br/autorregular/supervisao/comunicados-de-supervisao/integra/comunicado/aviso-de-prorrogacao-das-certificacoes-cfg-cga-e-cge/numero/2026-000007.htm)). Isso não elimina a necessidade de consultar o edital vigente antes da inscrição.

## Distribuição semanal sugerida (10 h)

| Área | Horas |
|---|---:|
| Certificação/finanças | 3h |
| Regulação CVM | 2h |
| FII/Infraestrutura | 2h |
| Implementação técnica | 2h |
| Revisão/anotações | 1h |

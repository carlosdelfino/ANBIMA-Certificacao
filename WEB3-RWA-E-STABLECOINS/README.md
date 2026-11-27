# WEB3-RWA-E-STABLECOINS — Infraestrutura digital, regulação e stablecoins para ativos reais tokenizados

Trilha técnica derivada do [plano de 12 meses](../plano_12_meses_web3_mercado_capitais_fii_infraestrutura_rwa.md) para a formação **Financial Infrastructure & Tokenization Architect**, na interseção entre engenharia de software, mercado de capitais, fundos de investimento, infraestrutura e tokenização de ativos do mundo real (RWA).

## Posição na formação

```text
                    MERCADO FINANCEIRO
                           │
                           ▼
                   Fundamentos / CFG
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       FUNDOS E IMÓVEIS          INFRAESTRUTURA
              │                         │
        FII / FIDC / FIP        FI-Infra / FIP-IE
              │                         │
        Valuation / NOI           Project Finance
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                    CVM / REGULAÇÃO
                           │
                           ▼
                     TOKENIZAÇÃO
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      Identidade       Smart Contracts    Settlement
      KYC/PLDFT        ERCs / RWA          DvP
          │                │                │
          └────────────────┼────────────────┘
                           ▼
               FINANCIAL INFRASTRUCTURE
                           │
                           ▼
              PORTFÓLIO PROFISSIONAL
```

Esta pasta corresponde aos meses 9 a 12 do plano: o ponto em que a formação de mercado ([CFG](../CFG/README.md), [CGE](../CGE/README.md), [CGA](../CGA/README.md)) converge para a implementação técnica.

## Roteiro de estudo

1. [Tokenização de ativos reais](01-tokenizacao-rwa.md) — pilha jurídico–registro–token, padrões ERC, restrições de transferência.
2. [DvP, stablecoins e liquidação](02-dvp-e-liquidacao.md) — entrega contra pagamento atômica, Drex, oráculos e finalidade.
3. [Custódia, identidade e compliance on-chain](03-custodia-identidade-compliance.md) — KYC/KYB/PLDFT, MPC, multisig, policy engine.
4. [Fundo de infraestrutura tokenizado](04-fundo-infra-tokenizado.md) — arquitetura do capstone, contratos, backend, dashboard.
5. [Segurança e invariantes financeiros](05-seguranca-e-invariantes.md) — checklist de segurança e testes da economia do sistema.
6. [Checklist do plano de 12 meses](06-checklist-plano-12-meses.md) — itens verificáveis por mês, marcos de certificação e rotina semanal.
7. [Órgãos reguladores e normas](07-orgaos-reguladores-e-normas.md) — CMN, BCB e CVM na tokenização e no mercado cripto, normas por processo, complementações e revogações.
8. [Stablecoins](08-stablecoins-regulamentacao.md) — regulamentação das stablecoins e regras de transação (Resoluções BCB 519/520/521, câmbio, autocustódia, moeda eletrônica).

## Método

Para cada conceito, percorra a sequência: conceito → regra financeira → regra regulatória → modelo de dados → API → smart contract → testes → documentação. Um exemplo do plano:

```text
Debênture
   ↓
Fluxo financeiro
   ↓
Covenants
   ↓
Contrato jurídico
   ↓
Representação digital
   ↓
Oracle
   ↓
Smart Contract
   ↓
Monitoring
```

> Material educacional e experimental. Nenhum conteúdo desta pasta constitui oferta de valor mobiliário, recomendação de investimento ou autorização regulatória. Padrões técnicos (ERCs) não substituem enquadramento jurídico; confirme sempre a norma consolidada da CVM, os documentos da oferta e a orientação profissional aplicável.

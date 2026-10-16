# Custódia, identidade e compliance on-chain

## Por que esta é uma área promissora para desenvolvedores

Custódia, identidade e prevenção a ilícitos são requisitos regulatórios que se traduzem diretamente em problemas de engenharia: gerenciamento de chaves, políticas de autorização, trilhas de auditoria e decisões de elegibilidade em tempo real. É onde a experiência de sistemas distribuídos mais agrega valor à infraestrutura financeira.

## O que estudar

- KYC (know your customer) e KYB (know your business);
- PLDFT — prevenção à lavagem de dinheiro e ao financiamento do terrorismo;
- beneficial owner: identificação do beneficiário final;
- wallets custodiais vs. não custodiais;
- MPC (multi-party computation) para assinatura distribuída de chaves;
- multisig para controle compartilhado de operações;
- HSM e módulos de segurança de hardware;
- account abstraction: contas inteligentes com políticas próprias;
- policy engine: motor que decide se uma operação pode ocorrer.

## Arquitetura de referência

```text
Transação
    │
    ▼
Policy Engine
    │
    ├── identidade
    ├── KYC
    ├── AML
    ├── jurisdição
    ├── limite
    ├── ativo
    ├── risco
    └── assinatura
    │
    ▼
Executor
```

O Policy Engine é o ponto único de decisão: recebe a intenção de transação, avalia cada dimensão e só então libera a execução. Separar decisão de execução permite auditar por que uma operação foi autorizada — ou por que foi recusada.

## Custódia: espectro de soluções

| Modelo | Quem controla a chave | Trade-off principal |
|---|---|---|
| Não custodial | O próprio titular | Autonomia total; perda da chave é perda do ativo. |
| Multisig | M de N signatários | Sem ponto único de falha; operação mais lenta. |
| MPC | Frações distribuídas da chave | Assinatura sem chave completa em nenhum lugar; complexidade criptográfica. |
| HSM | Hardware certificado | Alto custo; padrão em custodiantes institucionais. |
| Custodial | Prestador regulado | Dependência do custodiante; exigido em várias estruturas de fundos. |

Em fundos regulados, a custódia dos ativos é função de prestador habilitado — a wallet on-chain precisa compatibilizar-se com a custódia legal, e não o contrário.

## Projeto técnico — Compliance Policy Engine

Backend:

```text
Node.js
TypeScript
PostgreSQL
Redis
```

Smart contracts:

```text
PolicyRegistry.sol
TransferPolicy.sol
RoleRegistry.sol
```

Exemplo de política:

```json
{
  "asset": "FUND-A",
  "investorType": "QUALIFIED",
  "country": "BR",
  "kyc": true,
  "amlRisk": "LOW",
  "maxPosition": 1000000
}
```

## Trilha de auditoria

Compliance que não deixa registro não existe para o auditor. Registre decisão (permitida/recusada), política aplicada e versão, identificadores do investidor e do ativo, timestamp e referência da transação — sem expor dados pessoais ou payloads sensíveis nos logs nem nos eventos on-chain. Dados de identidade vivem off-chain; a cadeia recebe provas, hashes e referências, nunca o dossiê do investidor.

> Material educacional. Requisitos de KYC, PLDFT e custódia variam por jurisdição, tipo de investidor e veículo; confirme sempre a norma vigente da CVM, do Banco Central e os documentos do fundo.

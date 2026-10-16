# Tokenização de ativos reais

## Não pense apenas em ERC-20

Tokenização profissional mapeia uma pilha completa: o direito jurídico que existe fora da cadeia, o instrumento financeiro que o representa, o registro que comprova titularidade e, só então, o token. Ignorar qualquer elo da pilha produz um token sem lastro verificável ou sem validade operacional.

```text
Direito jurídico
        ↕
Instrumento financeiro
        ↕
Registro
        ↕
Token
        ↕
Titularidade
        ↕
Custódia
        ↕
Liquidação
```

A pergunta central de qualquer projeto de RWA é: qual camada detém a verdade jurídica sobre a titularidade? Se o registro oficial é o escriturador ou o depositário central, o token é uma representação que precisa reconciliar com essa fonte — não uma substituição automática dela.

## Conceitos a dominar

- RWA (real-world assets) e securities tokens;
- tokens permissionados e listas de acesso (whitelist);
- identity registry: vínculo entre endereço e investidor verificado;
- transfer restrictions: regras de elegibilidade executadas no momento da transferência;
- investor eligibility: qualificado, profissional, jurisdição, limites de posição;
- corporate actions: distribuição de rendimentos, amortizações, eventos societários refletidos on-chain;
- settlement: como a troca de ativo por pagamento é concluída (ver [DvP](02-dvp-e-liquidacao.md)).

## Padrões úteis para estudo

| Padrão | Uso típico |
|---|---|
| ERC-20 | Token fungível básico; ponto de partida, não solução regulatória. |
| ERC-4626 | Vaults tokenizados com depósito/resgate — análogo conceitual a cotas. |
| ERC-1400 | Security tokens com partições e controle de transferência. |
| ERC-3643 | Tokens permissionados com identidade on-chain (T-REX). |
| ERC-1155 | Múltiplos tipos de ativo em um só contrato (fungível e não fungível). |
| EIP-712 | Assinatura de dados tipados — base para autorizações e ordens off-chain. |
| ERC-4337 | Account abstraction — contas inteligentes, sessões e recuperação. |

Não trate a existência de um ERC como autorização regulatória. O padrão técnico e o enquadramento jurídico são problemas diferentes: um token pode implementar ERC-3643 perfeitamente e ainda assim representar uma oferta irregular de valor mobiliário.

## Arquitetura de referência

```text
Investor
   │
Wallet
   │
Identity Registry
   │
Compliance Engine
   │
Transfer Controller
   │
Security Token
   │
Asset Registry
```

Cada componente responde uma pergunta: **quem** é o investidor (Identity Registry), **se pode** transacionar (Compliance Engine), **como** a transferência é autorizada (Transfer Controller), **o que** circula (Security Token) e **sobre qual ativo** (Asset Registry).

## Projeto técnico — Permissioned RWA Token

Modelo mínimo de contratos para exercitar a arquitetura:

```text
IdentityRegistry.sol
Compliance.sol
TransferRules.sol
AssetToken.sol
CorporateActions.sol
```

Regras a implementar:

- somente investidores autorizados podem receber tokens;
- restrição por jurisdição e tipo de investidor;
- limite de investidores ou de posição por investidor;
- congelamento de conta e blacklist;
- pause global para incidentes;
- forced transfer administrativo somente em cenário explicitamente modelado (ex.: ordem judicial, sucessão);
- trilha de auditoria com eventos completos.

Para testes de segurança e invariantes econômicas desses contratos, ver [Segurança e invariantes financeiros](05-seguranca-e-invariantes.md).

## Ligação com a regulação brasileira

A classificação do token como valor mobiliário depende da substância econômica — expectativa de rendimento pelo esforço de terceiros, captação pública, fungibilidade — e não do rótulo técnico. Cotas de FII, FIP e FIDC já são valores mobiliários regulados pela [Resolução CVM 175](https://conteudo.cvm.gov.br/legislacao/resolucoes/resol175.html); tokenizar uma cota não muda sua natureza, muda o mecanismo de registro e transferência, que precisa ser aceito pelo administrador, escriturador e custodiante da estrutura.

> Material educacional. Tokenização de valores mobiliários exige análise jurídica caso a caso, prestadores regulados e, quando aplicável, registro ou dispensa formal perante a CVM.

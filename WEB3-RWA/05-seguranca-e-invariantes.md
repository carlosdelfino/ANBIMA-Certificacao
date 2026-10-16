# Segurança e invariantes financeiros

## Segurança como parte da arquitetura

Em aplicações financeiras, segurança não é camada adicionada no fim: ela condiciona o desenho desde o modelo de dados. O checklist abaixo cobre os pontos mínimos a revisar em qualquer contrato do sandbox.

Checklist:

- [ ] CEI — checks-effects-interactions;
- [ ] reentrancy;
- [ ] access control;
- [ ] multisig;
- [ ] timelock;
- [ ] pause;
- [ ] upgradeability;
- [ ] storage layout;
- [ ] oracle manipulation;
- [ ] flash loans;
- [ ] front-running;
- [ ] MEV;
- [ ] signature replay;
- [ ] nonce;
- [ ] EIP-712;
- [ ] fuzzing;
- [ ] invariant testing;
- [ ] análise estática;
- [ ] trilha de auditoria.

## Teste a economia do sistema

Não teste apenas o código — teste as propriedades financeiras que devem valer em qualquer estado alcançável. Exemplos de invariantes:

```text
NAV nunca pode ficar inconsistente
```

```text
totalAssets >= liabilities
```

```text
tokenSupply deve reconciliar com registro
```

```text
DvP não pode entregar somente um dos lados
```

```text
investidor bloqueado não pode receber token
```

```text
distribution <= distributableCash
```

```text
redemption não pode ultrapassar liquidez disponível
```

Cada invariante acima é um teste: no Foundry, `invariant_` functions com fuzzing exercitam sequências arbitrárias de chamadas e falham se a propriedade quebrar — mesmo em caminhos que um teste unitário manual nunca escreveria. Combine com análise estática (Slither), fuzzing direcionado (Echidna) e revisão humana.

## Onde cada risco mora

| Risco | Superfície típica | Mitigação de desenho |
|---|---|---|
| Reentrancy | `settle`, `redeem`, `distribute` | CEI, guards, liquidação atômica. |
| Replay de assinatura | Ordens EIP-712 | nonce por operação, expiry, chain id no domínio. |
| Manipulação de oráculo | NAV, DSCR, preço | fontes múltiplas, mediana, circuit breaker, timelock. |
| Privilégio excessivo | pause, forced transfer, upgrade | multisig + timelock + eventos + justificativa auditável. |
| Elegibilidade vencida | transfer, settlement | revalidação de compliance no momento da execução. |
| Estado contábil divergente | supply vs. registro | reconciliação on/off-chain com reconciler dedicado. |

## Princípio estrutural

Toda operação com efeito financeiro deve ter: autorização explícita (quem pode), precondição verificável (o que precisa valer antes), atomicidade (ou tudo ou nada), registro (evento e log auditável) e pós-condição (invariante que continua valendo). Quando uma dessas cinco partes falta, o defeito não é de implementação — é de desenho.

> Material educacional. Auditoria de contratos reais exige revisão independente, ferramentas e, em produção, processos formais de security review; este capítulo forma a base para conduzir essas revisões, não a substitui.

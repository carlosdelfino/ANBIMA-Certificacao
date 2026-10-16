# DvP, stablecoins e liquidação

## Conceito central

**Delivery versus Payment (DvP)** é o princípio de que a entrega do ativo e o pagamento ocorrem juntos: ou os dois lados liquidam, ou nenhum liquida. É o mesmo princípio que a infraestrutura tradicional aplica em sistemas de liquidação — em blockchain, a atomicidade pode ser garantida por um único contrato executado em uma só transação.

```text
Comprador
   │
   │ dinheiro
   ▼
Settlement Contract
   ▲
   │ ativo
   │
Vendedor
```

A operação deve ser:

```text
ATÔMICA
```

ou:

```text
entrega + pagamento
```

ou:

```text
nenhum dos dois
```

Se a implementação permitir que um lado execute sem o outro, o contrato recria o risco de principal que o DvP existe para eliminar.

## O que estudar

- atomic settlement e escrow;
- stablecoins e moedas de liquidação on-chain;
- tokenized deposits (depósitos bancários tokenizados);
- CBDC e Drex — a moeda digital do Banco Central brasileiro;
- BRL tokenizado e emissores privados de moeda estável;
- USDC e stablecoins em USD em operações internacionais;
- oráculos de preço e FX;
- finality: quando uma transação deixa de ser reversível;
- risco de contraparte entre assinatura e liquidação.

## Contrato experimental

Assinatura mínima de uma função de liquidação:

```solidity
settle(
    address buyer,
    address seller,
    address asset,
    address paymentToken,
    uint256 assetAmount,
    uint256 paymentAmount
)
```

Em produção conceitual, `settle` é chamado pelo próprio engine após validar autorizações assinadas dos dois lados — não por uma das partes sem prova da contraparte.

## Projeto técnico — DvP Engine

```text
                 DvP Engine
              ┌──────┴──────┐
              │             │
       Asset Registry   Cash Token
              │             │
              └──────┬──────┘
                     │
                 Settlement
                     │
                  Receipt
```

Requisitos a adicionar sobre o esqueleto:

- nonce por operação, para impedir reexecução;
- expiry: autorizações expiram — uma ordem assinada não deve ser válida para sempre;
- EIP-712: dados tipados assinados fora da cadeia, verificados dentro dela;
- verificação de assinatura de comprador e vendedor antes de mover qualquer ativo;
- compliance: ambas as partes precisam continuar elegíveis no momento da liquidação, não apenas na assinatura;
- replay protection: o mesmo par de assinaturas não pode liquidar duas vezes;
- emergency pause com governança definida.

## Finalidade e risco de contraparte

Na infraestrutura tradicional, finalidade é definida por regra do sistema de liquidação e pode envolver prazo (D+1, D+2) e intermediários. Em uma DLT com consenso determinístico, a finalidade tende a ocorrer no bloco — mas forks, reorganizações e redes permissionadas têm regras próprias que precisam constar do desenho. Enquanto a operação não atinge finalidade, existe janela de risco de contraparte; enquanto existir dependência de oráculo, existe risco de preço defasado ou manipulado.

## Ligação com fundos

Subscrição e resgate de cotas tokenizadas são aplicações diretas de DvP: o investidor entrega o token de pagamento e recebe a cota na mesma transação, ou a operação inteira reverte. O mesmo motor liquida distribuições em corporate actions quando combinado com o registro de titularidade — ver [Fundo de infraestrutura tokenizado](04-fundo-infra-tokenizado.md).

> Material educacional. Modelos com ativos e moedas fictícias em testnet; integração com pagamento real, Drex ou stablecoins reguladas exige participação de instituições autorizadas e infraestrutura aprovada.

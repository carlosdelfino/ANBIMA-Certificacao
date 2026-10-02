# Projeto 1 — FII tokenizado (simulação)

**Objetivo:** modelar token representativo didático de cotas, whitelist e evento de distribuição em testnet/local chain.

## Entregas

- `contracts/FiiShareToken.sol`: token ERC-20 didático com emissão restrita e pause/roles.
- `src/`: serviço Node.js para ingestão de posição e cálculo de distribuição fictícia.
- `docs/`: arquitetura, modelo de ameaça, eventos e reconciliação.

## Regras de domínio

Fonte oficial de titularidade/registro é simulada. A cadeia demonstra lógica; não substitui escrituração, depositário, administrador ou registro legal. Só dados sintéticos. Requisitos: autorização de emissão e supply, KYC fora da cadeia com atestado mínimo, prevenção a transferência não autorizada, conciliação de eventos e plano de chave comprometida.

## Aceite

Simular emissão, bloqueio de endereço, transferência autorizada, snapshot e cálculo proporcional de distribuição; mostrar divergência entre ledger e registro de referência e reconciliar via trilha auditável.

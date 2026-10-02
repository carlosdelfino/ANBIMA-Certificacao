# Projetos práticos — arquitetura para mercado de capitais tokenizado

Exercícios educacionais com ativos e dados fictícios. Use somente testnet/local chain; nenhum projeto está autorizado a emitir, ofertar ou negociar valor mobiliário real. Cada etapa entrega especificação de negócio, modelo de dados, contrato mínimo, serviço Node.js, testes locais e ameaça/controle documentados. Integração real exige autorização, prestadores regulados, análise jurídica, governança e infraestrutura adequada.

## Sequência

1. [FII tokenizado](01-fii-tokenizado/README.md) — registro referencial, distribuição simulada e eventos.
2. [FI-Infra](02-fi-infra/README.md) — posições de debêntures fictícias, duration e covenants.
3. [FIP-IE](03-fip-ie/README.md) — capital calls, participadas e waterfall de projeto.
4. [FIDC RWA](04-fidc-rwa/README.md) — recebíveis sintéticos, elegibilidade e subordinação.
5. [Plataforma de tokenização](05-plataforma-tokenizacao/README.md) — identidade, limites, reconciliação e audit trail.
6. [Site de simulados CFG/CGE/CGA](simulador-certificacoes/README.md) — frontend React adaptativo, histórico local, SEO e publicação estática na Vercel.

Stack sugerida: Solidity 0.8.x, Node.js LTS, Hardhat/Foundry, TypeScript, SQLite/PostgreSQL e provedores de dados simulados. Consulte documentação oficial atual de cada biblioteca antes de implementação; estes exercícios não fixam versões.

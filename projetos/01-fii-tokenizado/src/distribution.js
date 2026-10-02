// Dados exclusivamente fictícios; valores em unidades monetárias inteiras.
export function allocateDistribution(holders, totalAmount) {
  const supply = holders.reduce((sum, holder) => sum + BigInt(holder.units), 0n);
  if (supply <= 0n) throw new Error("supply must be positive");
  let allocated = 0n;
  const rows = holders.map((holder, index) => {
    const amount = index === holders.length - 1
      ? BigInt(totalAmount) - allocated
      : BigInt(totalAmount) * BigInt(holder.units) / supply;
    allocated += amount;
    return { account: holder.account, amount: amount.toString() };
  });
  return rows;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const holders = [{ account: "0xDemo1", units: "60" }, { account: "0xDemo2", units: "40" }];
  process.stdout.write(`${JSON.stringify(allocateDistribution(holders, "10000"), null, 2)}\n`);
}

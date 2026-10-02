export function reconcile(officialRows, chainRows) {
  const official = new Map(officialRows.map(row => [row.account.toLowerCase(), BigInt(row.units)]));
  const chain = new Map(chainRows.map(row => [row.account.toLowerCase(), BigInt(row.units)]));
  const accounts = new Set([...official.keys(), ...chain.keys()]);
  const breaks = [];
  for (const account of accounts) {
    const officialUnits = official.get(account) ?? 0n;
    const chainUnits = chain.get(account) ?? 0n;
    if (officialUnits !== chainUnits) breaks.push({ account, official: officialUnits.toString(), chain: chainUnits.toString() });
  }
  return { matched: breaks.length === 0, breaks };
}

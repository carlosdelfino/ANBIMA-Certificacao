export function projectMetrics({ equity, cashFlows, discountRate }) {
  const flows = [-Number(equity), ...cashFlows.map(Number)];
  const npv = flows.reduce((sum, amount, t) => sum + amount / (1 + discountRate) ** t, 0);
  const proceeds = cashFlows.reduce((sum, amount) => sum + Number(amount), 0);
  return { npv, moic: proceeds / Number(equity), cashFlows: flows };
}

export function dscrSeries(cfads, debtService) {
  if (cfads.length !== debtService.length) throw new Error("period arrays must match");
  return cfads.map((cash, i) => debtService[i] > 0 ? cash / debtService[i] : null);
}

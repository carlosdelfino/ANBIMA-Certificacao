export function estimateRatePnl(marketValue, modifiedDuration, shockBps) {
  return -Number(marketValue) * Number(modifiedDuration) * Number(shockBps) / 10_000;
}

export function dscr(cfads, debtService) {
  if (Number(debtService) <= 0) throw new Error("debt service must be positive");
  return Number(cfads) / Number(debtService);
}

export function pvCashflows(cashflows, discountRate) {
  return cashflows.reduce((pv, amount, i) => pv + Number(amount) / (1 + discountRate) ** (i + 1), 0);
}

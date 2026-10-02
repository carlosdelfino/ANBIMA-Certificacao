export function validateReceivable(row, seenIds = new Set()) {
  const errors = [];
  if (!row.id || seenIds.has(row.id)) errors.push("missing or duplicate id");
  if (!Number.isFinite(Number(row.balance)) || Number(row.balance) <= 0) errors.push("invalid balance");
  if (!row.dueDate || Number.isNaN(Date.parse(row.dueDate))) errors.push("invalid dueDate");
  if (!row.documentHash || !/^[a-f0-9]{64}$/i.test(row.documentHash)) errors.push("invalid document hash");
  return { eligible: errors.length === 0, errors };
}

export function subordinationRatio(subordinate, total) {
  if (Number(total) <= 0) throw new Error("total balance must be positive");
  return Number(subordinate) / Number(total);
}

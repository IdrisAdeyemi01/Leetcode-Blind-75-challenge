function maxProfit(prices: number[]): number {
  let mp = 0,
    lp = prices[0];
  for (let i = 1; i < prices.length; i++) {
    const diff = prices[i] - lp;

    if (diff > 0 && diff > mp) {
      mp = diff;
    }
    if (diff < 0) {
      lp = prices[i];
    }
  }
  return mp;
}

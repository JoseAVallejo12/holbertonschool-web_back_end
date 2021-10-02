function calculateNumber(type, a, b) {
  const aRound = Math.round(a);
  const bRound = Math.round(b);

  const obj = {
    SUM: () => aRound + bRound,
    SUBTRACT: () => aRound - bRound,
    DIVIDE: () => b > 0 ? aRound / bRound : 'Error',
  }
  return obj[type](a, b)
};

module.exports = calculateNumber;

function calculateNumber(type, a, b) {
  const aRound = Math.round(a);
  const bRound = Math.round(b);

  const operaciones = {
    SUM: () => aRound + bRound,
    SUBTRACT: () => aRound - bRound,
    DIVIDE: () => bRound > 0 ? aRound / bRound : 'Error',
  }
  return operaciones[type]()
};

module.exports = calculateNumber;

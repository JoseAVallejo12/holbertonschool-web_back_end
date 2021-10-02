const sum = require('./0-calcul');
const asserts = require('assert').strict;

describe('sum func', () => {
  asserts.equal(sum(1,2), 3)
})

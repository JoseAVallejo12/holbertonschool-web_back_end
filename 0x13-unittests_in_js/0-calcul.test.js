const asserts = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('result should be 4', function () {
    asserts.equal(calculateNumber(1, 3), 4);
  });

  it('result should be 5', () => {
    asserts.equal(calculateNumber(1, 3.7), 5);
  });

  it('result should be 5', () => {
    asserts.equal(calculateNumber(1.2, 3.7), 5);
  });

  it('result should be 6', () => {
    asserts.equal(calculateNumber(1.5, 3.7), 6);
  });
});

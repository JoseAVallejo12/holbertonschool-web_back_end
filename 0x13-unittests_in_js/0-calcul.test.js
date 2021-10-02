const asserts = require('assert');
const calculateNumber = require('./0-calcul');

// eslint-disable-next-line no-undef
describe('sum func', () => {
  // eslint-disable-next-line no-undef
  it('result should be 4', () => {
    const result = Math.round(calculateNumber(1, 3));

    asserts.equal(result, 4);
  });

  // eslint-disable-next-line no-undef
  it('result should be 5', () => {
    const result = Math.round(calculateNumber(1, 3.7));

    asserts.equal(result, 5);
  });

  // eslint-disable-next-line no-undef
  it('result should be 5', () => {
    const result = Math.round(calculateNumber(1.2, 3.7));

    asserts.equal(result, 5);
  });

  // eslint-disable-next-line no-undef
  it('result should be 6', () => {
    const result = Math.round(calculateNumber(1.5, 3.7));

    asserts.equal(result, 5);
  });
});

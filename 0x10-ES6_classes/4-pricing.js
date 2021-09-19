import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  set currency(value) {
    if (value instanceof Currency) this._currency = value;
  }

  get currency() {
    return this._currency;
  }

  set amount(value) {
    if (typeof value === 'number') this._amount = value;
  }

  get amount() {
    return this._amount;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}

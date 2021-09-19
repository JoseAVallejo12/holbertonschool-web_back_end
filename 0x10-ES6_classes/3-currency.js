export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  set code(value) {
    this._code = this.isString(value);
  }

  get code() {
    return this._code;
  }

  set name(value) {
    this._name = this.isString(value);
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }

  // eslint-disable-next-line class-methods-use-this
  isString(value) {
    if (typeof value === 'string') {
      return value;
    }
    throw new TypeError('Code must be a string');
  }
}

export default class Airport {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  set code(value) {
    if (typeof value === 'string') this._code = value;
  }

  get code() {
    return this._code;
  }

  set name(value) {
    if (typeof value === 'string') this._name = value;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }

  get [Symbol.toStringTag]() {
    return this._name;
  }
}

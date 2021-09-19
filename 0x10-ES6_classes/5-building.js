export default class Building {
  constructor(sqft) {
    console.log('🚀 ~ constructor ~ constructor', this.constructor);
    if (this.constructor.name !== 'Building' && typeof evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}

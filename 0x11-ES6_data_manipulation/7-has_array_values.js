export default function hasValuesFromArray(setArr, values = []) {
  for (const value of values) {
    if (!setArr.has(value)) return false;
  }
  return true;
}

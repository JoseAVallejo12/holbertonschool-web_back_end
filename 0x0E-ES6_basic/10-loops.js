export default function appendToEachArrayValue(array, appendString) {
  for (const value of array) {
    array.splice(array.indexOf(value), 1, `${appendString}${value}`);
  }

  return array;
}

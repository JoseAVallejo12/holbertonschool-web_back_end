export default function createIteratorObject(report) {
  const result = [];
  Object.values(report.allEmployees).map((arr) => result.push(...arr));
  return result;
}

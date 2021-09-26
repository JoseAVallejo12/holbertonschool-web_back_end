export default function getStudentIdsSum(students) {
  if (students instanceof Array) {
    return students.map((e) => e.id).reduce((preValue, currentValue) => preValue + currentValue);
  }
  return undefined;
}

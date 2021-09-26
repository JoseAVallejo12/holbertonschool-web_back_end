export default function updateStudentGradeByCity(students, city, newGrade = []) {
  if (students instanceof Array) {
    return students.filter((student) => student.location === city).map((student) => (
      {
        ...student,
        grade: { ...newGrade.find((obj) => obj.studentId === student.id) }.grade || 'N/A',
      }
    ));
  }
  return null;
}

const fs = require('fs');

function countStudents(pathFile) {
  try {
    const content = fs.readFileSync(pathFile, { encoding: 'utf-8' });
    const splitContent = content.trim().split('\n').filter((str) => str.length > 0);
    const result = {
      CS: [],
      SWE: [],
    };
    for (const value of splitContent) {
      const data = value.split(',');
      if (data.includes('CS')) result.CS.push(data[0]);
      if (data.includes('SWE')) result.SWE.push(data[0]);
    }
    console.log(`Number of students: ${result.CS.length + result.SWE.length}`);
    console.log(`Number of students in CS: ${result.CS.length}. List: ${result.CS.join(', ')}`);
    console.log(`Number of students in SWE: ${result.SWE.length}. List: ${result.SWE.join(', ')}`);
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;

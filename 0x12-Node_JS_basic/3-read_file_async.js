const fs = require('fs');

async function countStudents(pathFile) {
  return new Promise((resolve, reject) => {
    // eslint-disable-next-line consistent-return
    fs.readFile(pathFile, 'utf-8', (err, data) => {
      if (err) return reject(new Error('Cannot load the database'));
      const splitContent = data.trim().split('\n').filter((str) => str.length > 0);
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
      resolve();
    });
  });
}

module.exports = countStudents;

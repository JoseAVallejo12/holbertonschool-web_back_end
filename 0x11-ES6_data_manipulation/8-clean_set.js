export default function cleanSet(set, startString) {
  let res = '';
  if (startString) {
    set.forEach((element) => {
      const rexString = new RegExp(`^${startString}`);
      if (element.match(rexString)) {
        res += `${element.slice(startString.length, element[-1])}-`;
      }
    });
  }
  return res.slice(0, res.length - 1);
}

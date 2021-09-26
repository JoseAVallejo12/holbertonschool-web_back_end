export default function cleanSet(set, startString) {
  if (!startString || !startString.length) return '';
  let val = '';
  for (const el of set) {
    if (el && el.startsWith(startString)) {
      val += val.length === 0 ? el.replace(startString, '') : el.replace(startString, '-');
    }
  }
  return val;
}

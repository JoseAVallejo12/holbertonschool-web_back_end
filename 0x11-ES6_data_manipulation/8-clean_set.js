export default function cleanSet(set, startString) {
  set.forEach((element) => {
    element.startsWith(startString);
  });
}

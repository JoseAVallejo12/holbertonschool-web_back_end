export default function updateUniqueItems(mapObj) {
  for (const [key, value] of mapObj) {
    if (value === 1) mapObj.set(key, (value * 100));
  }
}

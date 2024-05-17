export function arrayToListItems(list) {
  let items = [];

  for (const item of list) {
    items.push({
      value: item,
      name: item
    });
  }

  return items;
}
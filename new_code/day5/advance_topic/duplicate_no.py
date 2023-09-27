def find_duplicates(elements):
  duplicates, seen =set(), set()
  for elements in elements:
        if elements in seen:
            duplicates.add(elements)
        seen.add(elements)
  return list (duplicates)

elements=[1,22,22,3,4,5,4,5]
duplicates=find_duplicates(elements)
print(duplicates)

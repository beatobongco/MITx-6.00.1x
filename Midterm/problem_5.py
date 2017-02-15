def dotProduct(listA, listB):
  '''
  listA: a list of numbers
  listB: a list of numbers of the same length as listA
  '''
  out = 0
  for x in range(0, len(listA)):
    out += listA[x] * listB[x]
  return out

assert dotProduct([1, 2, 3], [1, 1, 1]) == 6
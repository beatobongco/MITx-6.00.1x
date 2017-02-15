def deep_reverse(L):
  """ assumes L is a list of lists whose elements are ints
  Mutates L such that it reverses its elements and also
  reverses the order of the int elements in every element of L.
  It does not return anything.
  """
  L.reverse()
  for x in L:
    x.reverse()

L = [[1, 2], [3, 4], [5, 6, 7]]

deep_reverse(L)

assert L == [[7, 6, 5], [4, 3], [2, 1]]
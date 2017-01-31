def how_many(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: int, how many values are in the dictionary.
  '''
  count = 0
  for x in aDict.values():
    count += len(x)
  return count

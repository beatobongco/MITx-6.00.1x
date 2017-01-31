def biggest(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: The key with the largest number of values associated with it
  '''
  m = len(max(aDict.values()))
  for x in aDict:
    if len(aDict[x]) == m:
      return x

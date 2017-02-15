def flatten(aList):
  '''
  aList: a list
  Returns a copy of aList, which is a flattened version of aList
  '''
  r = []

  for x in aList:
    if type(x) == list:
      r = r + flatten(x)
    else:
      r.append(x)
  return r

assert flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]) == [1,'a','cat',2,3,'dog',4,5]
def oddTuples(aTup):
  '''
  aTup: a tuple

  returns: tuple, every other element of aTup.
  '''
  tup = ()
  for index, x in enumerate(aTup):
    if index % 2 == 0:
      tup = tup + (x, )

  return tup

assert oddTuples(('I', 'am', 'a', 'test', 'tuple')) == ('I', 'a', 'tuple')
def iterPower(base, exp):
  '''
  base: int or float.
  exp: int >= 0

  returns: int or float, base^exp
  '''
  if exp == 0:
    return 1
  result = base
  for x in range(exp - 1):
    result *= base

  return result
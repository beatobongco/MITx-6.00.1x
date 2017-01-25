def gcdIter(a, b):
  '''
  a, b: positive integers

  returns: a positive integer, the greatest common divisor of a & b.
  '''
  # Get smaller
  smaller = a

  if a > b:
    smaller = b

  for i in range(smaller, 0, -1):
    if a % i == 0 and b % i == 0:
      return i
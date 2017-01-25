def gcdRecur(a, b):
  '''
  a, b: positive integers

  returns: a positive integer, the greatest common divisor of a & b.
  '''
  # Your code here
  if b == 0:
    return a

  return gcdRecur(b, a % b)

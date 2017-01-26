def fib(n):
  """
    Input: an integer n
    Output: sum of fibonacci numbers
    This is really slow though
  """
  if n <= 1:
    return 1
  return fib(n - 1) + fib(n - 2)
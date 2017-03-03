def genFib():
  f1 = 1
  f2 = 0
  while True:
    # dont use next its reserved
    n = f1 + f2
    yield n
    f2 = f1
    f1 = n

# get nth fib number, non-zero indexed
def getNthFib(n):
  for i, x in enumerate(genFib()):
    if i == n:
      print("The {0} iteration of this gives {1}".format(i + 1, x))
      break

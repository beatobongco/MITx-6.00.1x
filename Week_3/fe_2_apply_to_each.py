def applyToEach(L, f):
  for i in range(len(L)):
    L[i] = f(L[i])

testList = [1, -4, 8, -9]
applyToEach(testList, abs)

assert testList == [1, 4, 8, 9]

testList = [1, -4, 8, -9]

def plus_one(x):
  return x + 1

applyToEach(testList, plus_one)

assert testList == [2, -3, 9, -8]

testList = [1, -4, 8, -9]

def times_self(x):
  return x * x

applyToEach(testList, times_self)

assert testList == [1, 16, 64, 81]
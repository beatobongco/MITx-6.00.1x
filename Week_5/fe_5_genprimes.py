def genPrimes():
  c = 2
  primes = set()
  while True:
    for p in primes:
      if c % p == 0:
        break
    else:
      primes.add(c)
      yield c
    c += 1

a = genPrimes()

assert a.__next__() == 2
assert a.__next__() == 3
assert a.__next__() == 5
assert a.__next__() == 7

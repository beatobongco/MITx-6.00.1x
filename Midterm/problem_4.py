def closest_power(base, num):
  '''
  base: base of the exponential, integer > 1
  num: number you want to be closest to, integer > 0
  Find the integer exponent such that base**exponent is closest to num.
  Note that the base**exponent may be either greater or smaller than num.
  In case of a tie, return the smaller value.
  Returns the exponent.
  '''
  n = 0
  tup_list = []

  while True:
    bn = base ** n
    diff = abs(num - bn)
    if bn == num:
      return n
    else:
      tup_list.append((diff, n))

    if diff > num:
      break

    n += 1
  return min(tup_list)[1]

assert closest_power(3,12) == 2
assert closest_power(4,12) == 2
assert closest_power(4,1) == 0
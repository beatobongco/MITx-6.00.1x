def general_poly(L):
  def f(n):
    _sum = 0
    c = len(L)
    for i in L:
      c -= 1
      _sum += i * n ** c
    return _sum
  return f

assert general_poly([1, 2, 3, 4])(10) == 1234

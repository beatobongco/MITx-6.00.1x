def f(a, b):
  return a + b

def dict_interdiff(d1, d2):
  '''
  d1, d2: dicts whose keys and values are integers
  Returns a tuple of dictionaries according to the instructions above
  '''
  d1_keys = set(d1.keys())
  d2_keys = set(d2.keys())

  inter_keys = d1_keys & d2_keys
  diff1_keys = d1_keys - d2_keys
  diff2_keys = d2_keys - d1_keys

  intersection = {}
  difference = {}

  for x in inter_keys:
    intersection[x] = f(d1[x], d2[x])

  for x in diff1_keys:
    difference[x] = d1[x]

  for x in diff2_keys:
    difference[x] = d2[x]

  return intersection, difference

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

assert dict_interdiff(d1, d2) == ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
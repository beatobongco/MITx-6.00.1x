def simple_divide(item, denom):
  try:
    return item / denom
  except ZeroDivisionError:
    return 0
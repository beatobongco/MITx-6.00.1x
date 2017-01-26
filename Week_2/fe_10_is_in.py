def isIn(char, aStr):
  '''
  char: a single character
  aStr: an alphabetized string

  returns: True if char is in aStr; False otherwise
  '''
  # Use bisection search
  mid_index = (len(aStr) - 1) // 2
  if mid_index == -1:
    return False
  elif char == aStr[mid_index]:
    return True
  elif char > aStr[mid_index]:
    return isIn(char, aStr[mid_index + 1:])
  elif char < aStr[mid_index]:
    return isIn(char, aStr[:mid_index])

assert isIn("a", "abcd") == True
assert isIn("z", "abcd") == False
def isPalindrome(s):
  if len(s) <= 1:
    return True

  # Get first and last and compare
  print(s[0], s[-1])
  if s[0] == s[-1]:
    print("Checking", s[1:-1])
    return isPalindrome(s[1:-1])
  else:
    return False

assert isPalindrome("racecar") == True
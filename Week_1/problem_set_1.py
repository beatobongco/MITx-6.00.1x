count = 0

for letter in s:
  if letter in ['a', 'e', 'i', 'o', 'u']:
    count += 1

print("Number of vowels:", count)
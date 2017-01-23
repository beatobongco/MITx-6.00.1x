temp = ""
counter = 0
for char in s:
  if char == "b":
    # Wait for "o" or check if prev is "o"
    if temp == "bo":
      temp = "b"
      counter += 1
    elif temp == "":
      temp += char
  elif char == "o":
    # only add "o" if prev was b
    if temp == "b":
      temp += char
    else:
      temp = ""
  else:
    temp = ""

print("Number of times bob occurs is:", counter)
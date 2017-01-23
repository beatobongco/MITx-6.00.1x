x = float(input("Enter a decimal number between 0 and 1: "))

p = 0 # power?
u = 0
while ((2**p) * x) % 1 != 0: # if unknown is not whole number keep on going
  # print(u)
  # print(u, int(u))
  # print("Remainder", (u) - int(u))
  p += 1 # Why are we adding 1 to p?
  u = (2**p) * x

# print("Final u", u)
# print("Final power", p)
num = int(x * (2**p)) # decimal x 2^ the high p resulting from making unknown into a whole number
# print("num", num)

# Old program

result = ''
if num == 0:
  result = "0"

while num > 0:
  result = str(num%2) + result
  num = num // 2

# print(result)

# End of old program

for i in range(p - len(result)):
  result = "0" + result # Why are we adding one zero per char in result? power

# print("initial result", result)
# r2 = "." + str(result)
result = result[0:-p] + "." + result[-p:] # Wouldn't it be the same as just adding . before ans?
print("Ans of", x, "is", result)
# print(r2)
# print(r2 == result)
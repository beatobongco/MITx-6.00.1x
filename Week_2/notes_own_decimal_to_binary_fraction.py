# Followed steps from http://sandbox.mc.edu/~bennet/cs110/flt/dtof.html

inp = input("Input a float: ")

out = ""
i_out = ""
f_out = ""
integral = int(inp.split(".")[0])
fractional = float("." + inp.split(".")[1])

if integral < 0:
  integral = abs(integral)
  out = "-"

# Get integral part
while True:
  i_out = str(integral % 2) + i_out
  integral = integral // 2
  if integral == 0:
    break

print("Integral:", i_out)

# Get fractional part, limit to 100
for i in range(100):
  fractional = str(fractional * 2)
  f_out += fractional[0] # Get the integral
  fractional = float(fractional[1:])
  if fractional == 0.0:
    break

out = out + i_out + "." + f_out
print("In binary:", out)

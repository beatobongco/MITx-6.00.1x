# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

def calculate_balance(balance, annual_interest_rate, monthly_payment_rate):
  remaining_balance = balance
  monthly_interest_rate = annual_interest_rate / 12

  for x in range(1, 13):
    minimum_monthly_payment = monthly_payment_rate * remaining_balance
    remaining_balance = remaining_balance - minimum_monthly_payment
    remaining_balance = remaining_balance + (monthly_interest_rate * remaining_balance)
    # print("Month {0} Remaining balance: {1}".format(x, round(remaining_balance, 2)))

  out = "Remaining balance: {0}".format(round(remaining_balance, 2))
  print(out)
  return out

# assert calculate_balance(balance, annualInterestRate, monthlyPaymentRate) == "Remaining balance: 31.38"

calculate_balance(balance, annualInterestRate, monthlyPaymentRate)
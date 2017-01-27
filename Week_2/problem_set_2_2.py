# balance = 3329
# annualInterestRate = 0.2

def calc_min_montly_payment(balance, annual_interest_rate):
  """
    balance -- positive float or int
    annual_interest_rate -- positive float
  """
  end_balance = balance
  lowest_payment = 0
  montly_ir = annual_interest_rate / 12
  # A good guess would be balance / 12 rounded to nearest 10, its the smallest possible for a annual interest rate of 0
  guess = round(balance / 12, -1)
  while True:
    for x in range(1, 13):
      end_balance = end_balance - guess
      end_balance = end_balance + (end_balance * montly_ir)
    if end_balance < 0:
      break
    guess += 10
    end_balance = balance
  out = "Lowest Payment: {0}".format(int(guess))
  print(out)
  return out

calc_min_montly_payment(balance, annualInterestRate)
# assert calc_min_montly_payment(balance, annualInterestRate) == "Lowest Payment: 310"
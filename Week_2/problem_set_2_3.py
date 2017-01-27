# balance = 320000
# annualInterestRate = 0.2

def calc_min_montly_payment(balance, annual_interest_rate):
  """
    balance -- positive float or int
    annual_interest_rate -- positive float
  """
  end_balance = balance
  lowest_payment = 0
  montly_ir = annual_interest_rate / 12

  guess_lb = balance / 12 # lower bound
  guess_ub = (balance * (1 + montly_ir)**12) / 12 # upper bound

  while True:
    guess = (guess_ub + guess_lb) / 2
    for x in range(1, 13):
      end_balance = end_balance - guess
      end_balance = end_balance + (end_balance * montly_ir)
    if end_balance < 0 and end_balance > -0.01:
      break
    elif end_balance > 0:
      # Guess too low, throw away anything lower
      guess_lb = guess
    elif end_balance < 0:
      # Guess too high, throw away anything higher
      guess_ub = guess
    end_balance = balance
  out = "Lowest Payment: {0}".format(round(guess, 2))
  print(out)
  return out

calc_min_montly_payment(balance, annualInterestRate)
# assert calc_min_montly_payment(balance, annualInterestRate) == "Lowest Payment: 29157.09"
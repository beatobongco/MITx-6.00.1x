trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
  '''
  us_num, a string representing a US number 0 to 99
  returns the string mandarin representation of us_num
  '''
  o = []
  tens = int(us_num) // 10
  if tens > 1:
    o.append(trans.get(str(tens)))
  if tens > 0:
    o.append(trans.get('10'))

  last = str(us_num)[-1]

  # Dont append last digit if 0 and greater than ten
  if not (tens > 0 and last == '0'):
    o.append(trans.get(last))

  return ' '.join(o)

assert convert_to_mandarin('36') == 'san shi liu'
assert convert_to_mandarin('20') == 'er shi'
assert convert_to_mandarin('16') == 'shi liu'
assert convert_to_mandarin('1') == 'yi'
assert convert_to_mandarin('0') == 'ling'

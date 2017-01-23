results = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
out = ''
for letter in s:
	old_index = alphabet.index(out[-1]) if len(out) > 0 else -2
	if len(out) == 0:
		out += letter
	elif alphabet.index(letter) >= old_index:
		out += letter
	else:
		out = letter
	results.append(out)
print(max(results, key=lambda r: len(r)))

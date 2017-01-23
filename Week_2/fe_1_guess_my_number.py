high = 100
low = 0
guess = None

print("Please think of a number between 0 and 100!")
while True:
	guess = (high + low) // 2
	print("Is your secret number " + str(guess) + "?")
	i = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	if i == "h":
		high = guess
	elif i == "l":
		low = guess
	elif i == "c":
		print("Game over. Your secret number was:", guess)
		break
	else:
		print("Sorry, I did not understand your input.")
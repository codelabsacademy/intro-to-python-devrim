import random 

random_number = random.randint(1, 100)
guessed_number = None

while True:
	guessed_number = int(input("Please enter a guess: "))

	if guessed_number == random_number:
		print("Congratulations, you found my number!")
		break
	elif guessed_number > random_number:
		print("Incorrect, my number is smaller!")
	elif guessed_number < random_number:
		print("Incorrect, my number is greater!")
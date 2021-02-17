from random import randint
#for name in range(1,21):
	#if name == 4 :
		#print(f"{name} is Unlucky")
	#elif name == 13:
		#print(f"{name} is Unlucky")
	#elif name % 2 == 0:
		#print(f"{name} is even")
	#elif name % 2 == 1:
		#print(f"{name} is odd")
Game_running = True
new_round = True
while Game_running == True:
	random_number = randint(1,10)
	number = int(input("Guess a number between 1 and 10: "))
	print(f"random number is: {random_number} and number is: {number}") 
	if number == random_number:
		print("You guessed it! You won!")
	elif number > random_number:
		print("Too high, try again!")
	elif number < random_number:
		print("Too low, try again!")

	if number == random_number:
		Game_running = False
playing = input("Do you want to keep playing (y/n) ")
while new_round == True:
	if playing == "y":
		random_number = randint(1,10)
		number = int(input("Guess a number between 1 and 10: "))
		print(f"random number is: {random_number} and number is: {number}") 
		if number == random_number:
			print("You guessed it! You won!")
		elif number > random_number:
			print("Too high, try again!")
		elif number < random_number:
			print("Too low, try again!")
	elif playing == "n":
		print("Thanks for playing. Bye!")
		break







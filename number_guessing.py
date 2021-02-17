# from  random module randint function was import
from random import randint

#condition for while loop
game_running =True

# while loop to repeat the game several times
while game_running == True:

# player score 
	player_score = 10

# print function to display player score 
	print(player_score)

# generate random number for computer
	Computer = randint(1,11)

# input function to wait for player enter number and int to casting it to number
	player = int(input("Guess The Number: "))

	print(f"Computer play:{Computer} player play: {player}")

# conditional statement for game
	if Computer == player:
		player_score += 1
		print(f"Player score: {player_score}")

	elif Computer != player:
		player_score -= 1
		print(f"Player score: {player_score}")

	if player_score == 0:
		game_running = False
from random import randint 

playing_game = True

while playing_game == True:
	dice_rolling = randint(1,7)
	print(f"player roll: {dice_rolling}")

	play_agin = input("Do you want to play again (y/n)")

	if play_agin == "y":
		playing_game = True

	elif play_agin == "n":
		playing_game = False


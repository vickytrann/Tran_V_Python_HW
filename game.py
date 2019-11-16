# import the random package so we can generate a random AI choice
from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

# let the AI make a choice
computer=choices[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player = False

while player is False:
	player=input("choose rock, paper or scissors: \n")
	 
	# start doing some logic and condition checking
	print("computer: ", computer, "player: ", player)

	# always check a breaking condition first
	if player == computer:
		#we have a tie, no point in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
		else:
			print("You won!", player, "smashes", computer, "\n")

	elif player == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			print("You won!", player, "covers", computer, "\n")

	elif player == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			print("You won!", player, "cuts", computer, "\n")
		

	player = False
	computer=choices[randint(0,2)]

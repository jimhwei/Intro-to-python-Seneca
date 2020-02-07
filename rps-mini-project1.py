#how can i shorten my code by making my if statements do 2 things at once? Zen of python?
#how do i shorten line 12?


import random

player_score = 0
computer_score = 0
player1 = 0


while player_score < 3 and computer_score < 3 and player1 != "quit" and player1 !="q":

    print("...rock...")
    print("...paper...")
    print("...scissors...")
    
    
    player1 = str.lower(input("Player 1, make your move: "))
    computer = random.choice(["rock","paper","scissors"])
    
    #print(player1)
    print("The computer plays:",computer)
    
    if player1 == computer:
    	print("It's a tie!")
    elif player1 == "rock":
    	if computer == "scissors":
    		print("player1 wins!") 
    	elif computer == "paper":
    		print("computer wins!") 
    elif player1 == "paper":
    	if computer == "rock":
    		print("player1 wins!") 
    	elif computer == "scissors":
    		print("computer wins!") 
    elif player1 == "scissors":
    	if computer == "paper":
    		print("player1 wins!") 
    	elif computer == "rock":
    		print("computer wins!")	
    else:
    	print("something went wrong")
        
    if player1 == computer:
    	print("It's a tie!")
    elif player1 == "rock":
    	if computer == "scissors":
    		player_score += 1 
    	elif computer == "paper":
    		computer_score += 1 
    elif player1 == "paper":
    	if computer == "rock":
    		player_score += 1
    	elif computer == "scissors":
    		computer_score += 1 
    elif player1 == "scissors":
    	if computer == "paper":
    		player_score += 1
    	elif computer == "rock":
    		computer_score += 1	
    else:
    	print("something went wrong")
        
    
    print(f"Player Score: {player_score} Computer Score: {computer_score}")
    print("-"*16)
    
if player_score > computer_score:
    print("CONGRATS, YOU WON!")
elif computer_score > player_score:
    print("OH NO :-( THE COMPUTER WON...")
else:
    print("NO WINNER, IT'S A TIE")
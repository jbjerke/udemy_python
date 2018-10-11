from random import randint

print("...rock...\n...paper...\n...scissors...")

player_one = input("(enter player one's choice): ").lower() #turns whatever letters typed into lower case

comp = randint(0,2);

if comp == 0:
    player_two = "rock"
elif comp == 1:
    player_two = "paper"
else:
    player_two = "scissors"

print("Player Two chose " + player_two)

if player_one == player_two:
    print("Draw!")
elif player_one == "rock":
    if player_two == "paper":
        print("Player Two Wins!")
    else:
        print("Player One Wins!")
elif player_one == "paper":
    if player_two == "rock":
        print("Player One Wins!")
    else:
        print("Player Two Wins!")
else:
    if player_two == "rock":
        print("Player Two Wins!")
    else:
        print("Player One Wins!")

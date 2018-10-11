print("...rock...\n...paper...\n...scissors...")

player_one = input("(enter player one's choice): ")
player_two = input("(enter player two's choice): ")

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

import random

def diceroll():
    dice = random.randint(1, 6)
    return dice

def pig():
    total_player_1 = 0
    total_player_2 = 0
    player = 1

    while True:
        turn_total = 0
        print(f"\nplayer {player}'s turn")
     
        roll = diceroll()

        while roll != 1:
            print(f"\nplayer {player} rolled a {roll}")
            turn_total += roll
            print(f"turn total: {turn_total}")
            if player == 1:
                print(f"player 1 total before current turn: {total_player_1}\n")
            elif player == 2:
                print(f"player 2 total before current turn: {total_player_2}\n")
            if turn_total >= 100:
                print(f"player {player} wins with a turn total of {turn_total}")
                return
            choice = input("do you want to hold or roll? hold/roll: ").strip().lower()
            if choice == "hold":
                break
            roll = diceroll()

        if roll == 1:
            print(f"\nplayer {player} rolled a 1, no points for this turn")
            turn_total = 0

        if player == 1:
            total_player_1 += turn_total
            print(f"\nplayer 1 total: {total_player_1}")
            if total_player_1 >= 100:
                print("player 1 wins")
                return
            player = 2
        else:
            total_player_2 += turn_total
            print(f"\nplayer 2 total: {total_player_2}")
            if total_player_2 >= 100:
                print("player 2 wins")
                return
            player = 1

pig()
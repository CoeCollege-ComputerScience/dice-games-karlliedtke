import random
def diceroll():
    dice = random.randint(1,6)
    return dice
result = diceroll()

def pig():
    total_player_1 = 0
    total_player_2 = 0
    player = 1

    while total_player_1 < 20 and total_player_2 < 20:
        turn_total = 0
        print (f"\nplayer {player}'s turn")
        roll = diceroll()

        while roll != 1:
            print(f"player {player} rolled a {roll}")
            turn_total += roll
            print(f"turn total: {turn_total}")
            choice = input("do you want to hold or roll? hold/roll: ").strip().lower()
            if choice == "hold":
                break
            roll = diceroll()

        if roll == 1:
            print(f"player {player} rolled a 1, no points for this turn")
            turn_total = 0      

        if player == 1:
            total_player_1 += turn_total
            print(f"player 1 total: {total_player_1}")
            player = 2
        else:
            total_player_2 += turn_total
            print(f"player 2 total: {total_player_2}")
            player = 1

        if total_player_1 >= 20:
            print("player 1 wins")
        else:
            print("player 2 wins")  

pig()
       

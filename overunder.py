import random

def rollDice():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def take_turn():
        turn_total = 0
        roll = rollDice()
        print(f"roll is: {roll}")
        while True:
            guess = input("\nwill next roll be over or under? over/under: ").strip().lower()
            if guess in ["over", "under"]:
                  break
            else:
                print("Invalid input, please enter 'over' or 'under'")
        roll_two = rollDice()
        print(f"\nsecond roll is: {roll_two}")
        if guess == "over" and roll_two > roll:
            turn_total += 1
            print()
        elif guess == "under" and roll_two < roll:
                turn_total += 1
                
        else:
            turn_total +=0

        return turn_total

player1points = 0
player2points = 0

while True:
    while True:
        switch = input("\nIt is now Player 1's turn to roll and player 2's to guess. enter yes to continue: ").strip().lower()
        if switch in ["yes"]:
                break
        else:
            print("Invalid input, please enter 'yes'")
    print(f"\nPlayer 1 is now rolling the dice")

    player2points += take_turn()
    print(f"player2points: {player2points}")
    if player2points ==2:
            print("Game over, player 1 wins")
            break
    
    while True:
        switch = input("\nIt is now Player 2's turn to roll and player 1's to guess. enter yes to continue: ").strip().lower()
        if switch in ["yes"]:
                break
        else:
            print("Invalid input, please enter 'yes'")
    print(f"\nPlayer 2 is now rolling the dice")

    player1points += take_turn()
    print(f"player1points: {player1points}")
    if player1points ==2:
            print("Game over, player 1 wins")
            break

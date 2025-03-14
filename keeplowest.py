import random

def rolldice(i):
    rolls = [random.randint(1,6) for i in range(i)]
    return rolls

def take_turn():
    turn_total = 0
    for i in range(5):
            results = (rolldice(5-i))
            print(f"\n{results}")
            lowest = (min(results))
            print(f"lowest roll: {lowest}")
            turn_total += lowest
    return turn_total
      

player1count = 0
player2count = 0

while True:
    while True:
        switch = input("It is now Player 1's turn. enter yes to continue: ").strip().lower()
        if switch in ["yes"]:
                break
        else:
            print("Invalid input, please enter 'yes'")
    print(f"\nPlayer 1 is now rolling the dice")
    
    
    player1count += take_turn()
    print(f"player1count: {player1count}")
    if player1count >= 20:
            print("Player 1 loses, player 2 wins")
            break
    
    while True:
            switch = input("It is now Player 2's turn. enter yes to continue: ").strip().lower()
            if switch in ["yes"]:
                break
            else:
                print("Invalid input, please enter 'yes'")
        
    print(f"\nPlayer 2 is now rolling the dice")
    
    player2count += take_turn()
    print(f"player2count: {player2count}")
    if player2count >= 20:
            print("Player 2 loses, player 1 wins")
            break
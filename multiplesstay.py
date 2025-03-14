import random
def diceroll(i):
    rolls = [random.randint(1,6) for i in range(i)]
    return rolls
for i in range(1):


    def MultiplesStay():
        player = 1
        rolls = diceroll(10)
        while rolls:
            
            print(f"The amount of remaining dice is {len(rolls)}")
            print(f"Player {player} rolls: {rolls}")

            multiples = [x for x in set(rolls) if rolls.count(x) > 1]
            if not multiples:
                print(f"Player {player} loses! No multiples rolled.")
                break
        
            eliminated = int(input(f"Player {player} choose a multiple to eliminate from {multiples}: "))
            while eliminated not in multiples:
                eliminated = int(input(f"Invalid choice. Player {player} choose a multiple to eliminate from {multiples}: "))
            print(f"Player {player} eliminates: {eliminated}")


            print()
            
            rolls = [x for x in rolls if x != eliminated]
            if not rolls:
                print(f"Player {player} wins! No dice left.")
                break
        
            player = 2 if player == 1 else 1

MultiplesStay()
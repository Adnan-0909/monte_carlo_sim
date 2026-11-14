import random
def rollDice():
    roll = random.randint(1, 100)
    if roll == 100:
        # print("You rolled a 100! You win!")
        return False
    elif roll <= 50:
        # print("You rolled a low number. Try again!")
        return False
    
    elif 100>roll > 50:
        # print("You rolled a high number. You win!")
        return True

def simple_bettor(funds,initial_bet, bet_count):
    value = funds
    bet = initial_bet
    current_bet_count = 0
    while current_bet_count < bet_count:
        if rollDice():
            value += bet
            # print(f"You won! Your new balance is: {value}")
        else:
            value -= bet
            # print(f"You lost! Your new balance is: {value}")
        current_bet_count += 1
    print(f"Final balance: {value}")

x=0 
while x<100:#checking for a 50 different bettors, that how well they performed
    simple_bettor(1000, 50, 1000)
    x+=1
# simple_bettor(1000, 50, 50)

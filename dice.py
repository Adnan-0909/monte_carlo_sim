import random
import matplotlib.pyplot as plt

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

    bX = []#list for the bets, on x-axis
    vY = []#list of the value, on y-axis
    current_bet_count = 1
    while current_bet_count <= bet_count:
        if rollDice():
            value += bet
            bX.append(current_bet_count)
            vY.append(value)
            # print(f"You won! Your new balance is: {value}")
        else:
            value -= bet
            # print(f"You lost! Your new balance is: {value}")
        current_bet_count += 1
    if value <= 0:
        value = 'broke'
    # print(f"Final balance: {value}")
    plt.plot(bX, vY)

x=0 
while x<100:#checking for a 50 different bettors, that how well they performed
    simple_bettor(10000, 100, 100)
    x+=1
# simple_bettor(1000, 50, 50)
plt.ylabel('Account Value')
plt.xlabel('Number of Bets')
plt.show()  
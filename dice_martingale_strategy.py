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

def doubler_bettor(funds,initial_bet,bet_count):
    value = funds
    global broke_count
    bet = initial_bet

    bX = []#list for the bets, on x-axis
    vY = []#list of the value, on y-axis
    current_bet_count = 1
    previous_bet = 'win'
    previous_bet_amount = initial_bet

    while current_bet_count <= bet_count:
        if previous_bet == 'win':
            bet = initial_bet
        elif previous_bet == 'loss':
            bet = previous_bet_amount * 2

        if rollDice():
            value += bet
            bX.append(current_bet_count)
            vY.append(value)
            previous_bet = 'win'
            previous_bet_amount = bet
            # print(f"You won! Your new balance is: {value}")
        else:
            value -= bet
            previous_bet = 'loss'
            previous_bet_amount = bet
            bX.append(current_bet_count)
            vY.append(value)
            if value <= 0:
                value = 'broke'
                broke_count += 1
                break
            # print(f"You lost! Your new balance is: {value}")
        current_bet_count += 1
    plt.plot(bX, vY)
x=0 
broke_count = 0
while x<100:#checking for a 50 different bettors, that how well they performed
    doubler_bettor(10000, 100, 100)
    x+=1
# # simple_bettor(1000, 50, 50)

# doubler_bettor(10000, 100, 1000)

plt.ylabel('Account Value')
plt.xlabel('Number of Bets')
print(f"Number of broke bettors: {broke_count/float(x)*100}%")
print(f"Survival rate: {(1-(broke_count/float(x)))*100}%")
plt.axhline(y=0, color='r', linestyle='-')
plt.show()  
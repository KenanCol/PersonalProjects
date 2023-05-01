import random

#These are constants that can be changed to change the game
MAX_LINES = 3
MAX_BET = 100

ROWS = 3
COLS = 3

#This is a dictionary that maps a symbol to a number
symbol_count = {
    "A": 2,
    "B": 6,
    "C": 4,
    "D": 8,
}

def deposit():
    while True:
        amount = input("What would you like to depsit? $")
        # Check if the amount is a digit
        if amount.isdigit():
            # Convert the amount to an integer
            amount = int(amount)
            # Check if the amount is greater than 0
            if amount > 0:
                break
            else:
                print("Invalid amount, amount must be greater than 0")
        else:
            print("Please enter a valid amount")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")# we make a concatenation to make sure that the user can only enter a number between 1 and 3
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("Invalid number of lines, number of lines must be between 1 and 3")
        else:
            print("Please enter a valid number of lines")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet ?")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0 and bet <= MAX_BET:
                break
            else:
                print(f"Invalid bet, bet must be between $1 and ${MAX_BET}")
        else:
            print("Please enter a valid bet")
    return bet

#We use the main function so that if we end our program, we can start it again
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print("You do not have enough money to make this bet, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

main()
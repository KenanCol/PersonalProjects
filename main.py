MAX_LINES = 3
MAX_BET = 5

def deposit():
    while True:
        amount = input("What would you like to depsit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid amount, amount must be greater than 0")
        else:
            print("Please enter a valid amount")
    return amount

def get_number_of_lines():
    while True:
        number_of_lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if number_of_lines > 0 and number_of_lines <= MAX_LINES:
                break
            else:
                print("Invalid number of lines, number of lines must be between 1 and 3")
        else:
            print("Please enter a valid number of lines")
    return number_of_lines

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

def main():
    balance = deposit()
    number_of_lines = get_number_of_lines()
    bet = get_bet()
    total_bet = number_of_lines * bet
    print(f"You are betting ${bet} on {number_of_lines} lines. Total bet is equal to ${total_bet}")

main()
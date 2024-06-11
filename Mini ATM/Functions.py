transaction_history = []

def checkbalance():
    balance = 5000
    print("Your current balance is:", balance)
    return balance

def get_withdrawal_limit(cardtype):
    if cardtype == "1" or cardtype == "Rupay":
        return 2000
    elif cardtype == "2" or cardtype == "Visa":
        return 5000
    elif cardtype == "3" or cardtype == "MasterCard":
        return 10000
    else:
        return 0

def withdraw_money(amount, cardtype):
    balance = checkbalance()
    withdrawal_limit = get_withdrawal_limit(cardtype)

    if amount > withdrawal_limit:
        print("Withdrawal amount exceeds the limit for your card type!")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance:", balance)
        add_transaction("Withdrawal", amount)

def deposit_money(amount):
    balance = checkbalance()
    balance += amount
    print("Deposit successful. Current balance:", balance)
    add_transaction("Deposit", amount)

def add_transaction(transaction_type, amount):
    transaction = f"{transaction_type}: {amount}"
    transaction_history.append(transaction)

def print_mini_statement():
    print("Last three transactions:")
    for i in range(-1, -4, -1):
        if abs(i) <= len(transaction_history):
            print(transaction_history[i])

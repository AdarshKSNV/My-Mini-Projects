from Functions import checkbalance, get_withdrawal_limit, withdraw_money, deposit_money, add_transaction, print_mini_statement

class Fun:
    def types(self):
        self.ATMBALANCE = 1000000
        print("Cash Available in the atm is:", self.ATMBALANCE)
        return self.cardtypes()

    def cardtypes(self):
        self.cardtype = input("Enter the card type you have ('1.Rupay','2.Visa','3.Mastercard'):")
        if self.cardtype in ["1", "Rupay", "2", "Visa", "3", "Mastercard"]:
            return self.auth()
        else:
            print("Card types not found")
            return self.cardtypes()

    def auth(self):
        self.username = input("Enter the Username:")
        self.password = input("Enter the Password:")
        if self.username == self.password:
            print("Successfully Login")
            option = input("Enter the option you need: (1.Balance, 2.Cash Withdrawal, 3.Cash Deposit, 4.Mini Statement, 5.Card Renewal)")
            if option == "1":
                checkbalance()
            elif option == "2":
                amount = int(input("Enter the amount to withdraw: "))
                withdraw_money(amount, self.cardtype)
            elif option == "3":
                amount = int(input("Enter the amount to deposit: "))
                deposit_money(amount)
            elif option == "4":
                print_mini_statement()
            elif option == "5":
                pass
        else:
            print("Invalid Credentials")
            self.auth()
        return obj.auth()

obj = Fun()
obj.types()

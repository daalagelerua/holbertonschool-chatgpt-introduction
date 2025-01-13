from decimal import Decimal, getcontext

class Checkbook:
    def __init__(self):
        self.balance = Decimal('0.00')

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        self.get_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            self.get_balance()

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_positive_amount(prompt):
    while True:
        try:
            amount = Decimal(input(prompt))
            if amount <= 0:
                print("Error: Amount must be positive.")
            else:
                return amount
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def main():
    getcontext().prec = 2  # Définir la précision décimale à 2 chiffres après la virgule
    cb = Checkbook()
    print("Welcome to the Checkbook App!")
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Thank you for using the Checkbook App. Goodbye!")
            break
        elif action == 'deposit':
            amount = get_positive_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_positive_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

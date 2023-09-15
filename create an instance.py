class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Invalid withdrawal amount. Amount should be greater than 0.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account1 = BankAccount("123456789", "John Doe", 1000.0)

    # Deposit and withdraw money
    account1.display_balance()
    account1.deposit(500.0)
    account1.withdraw(200.0)
    account1.withdraw(1500.0)  # This should print "Insufficient funds for withdrawal."
    account1.deposit(-100.0)    # This should print "Invalid deposit amount. Amount should be greater than 0."
    account1.display_balance()

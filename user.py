# Start of BankAccount Class

class BankAccount:
    bank_name = "Bank of Burbank"
    bank_location = "Burbank"

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            print("insufficient funds. charged $5 fee")
        return self

    def display_account_info(self):
        print(f"interest rate: {self.int_rate}\n balance: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        else:
            print("No money")
        return self

    @classmethod
    def display_bank_info(cls):
        print(f"Name: {cls.bank_name}\n Location: {cls.bank_location}")
# End of BankAccount class
        
# Start of User class
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = {}

    # Adds to the balance of the BankAccount class
    def make_deposit(self, amount):
        self.account[a1].deposit(amount)

    def make_withdrawal(self, amount):
        self.account[a1].withdraw(amount)

    def display_user_balance(self):
        print(f"balance: {self.account.balance}")

    def add_account(self, bank_account):
        account_name = input(f"What do you want to name this account?\n")
        self.account[account_name] = bank_account

    def transfer_money(self, amount, other_user):
        other_user.account[a1].deposit(amount)

    def display_info(self):
        print(f"\nUser Info:")
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        if self.gold_card_points > 0:
            print(self.gold_card_points)
        else:
            print("Not enough")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self
# End of User class



u1 = User("Yeshua", " Lopez", "lopez@email.com", 22)
u2 = User("Not", "Yeshua", "yeshua@email.com", 21)

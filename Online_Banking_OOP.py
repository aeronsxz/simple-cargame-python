# Simple banking system using OOP

# Parent Class - Users information
class UserInfo:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_info(self):
        print(f"Thank you for registering, here are your personal information. Name: {name.title()}, Age: {age},"
              f"Gender: {gender}")


# Child Class  -  Calculations Start
class Bank(UserInfo):
    total_deposit = 0
    total_withdraw = 0

    def __init__(self, name, age, gender, balance):
        super().__init__(name, age, gender)
        self.balance = balance   # Protected

    def show_info(self):
        return f"{self.name}, has a remaining balance of: ₱{round(self.balance, 2)}"

    def deposit(self):
        dp = float(input(f"Hello, {self.name.title()}. Please enter the amount you want to deposit: "))
        print('Thank you for depositing....')
        self.balance += dp
        self.total_deposit += 1
        return f"Account balance has been updated: ₱{round(self.balance, 2)}"

    def withdraw(self):
        wd = float(input(f"Hello, {self.name.title()}. Please enter the amount you want to withdraw: "))
        if wd > self.balance:
            print('Insufficient Balance | Balance Available: ', round(self.balance, 2))
        else:
            self.balance = self.balance - wd
            print('Account balance has been updated: ', round(self.balance, 2))
            self.total_withdraw += 1


def options(user_two):
    print("Thank you for creating your bank account! Here are the list of options that our banks offer. Please choose "
          "the number.")
    while True:
        option_select = int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraw\n5) See Total Deposit"
                                  "\n6) Quit\n"))

        if option_select == 1:
            print(user_one_bank.show_info())
            if option_select == 1 and user_two != None:
                print((user_two_bank.show_info()))

        elif option_select == 2:
            print(user_one_bank.withdraw())
            if option_select == 2 and user_two != None:
                wd = (input(f"Hello, {user_two.name.title()}. Would you like to withdraw? Yes | No "))
                if wd.lower() == 'yes':
                    print(user_two_bank.withdraw())

        elif option_select == 3:
            print(user_one_bank.deposit())
            if option_select == 3 and user_two != None:
                wd = (input(f"Hello, {user_two.name.title()}. Would you like to deposit? Yes | No "))
                if wd.lower() == 'yes':
                    print(user_two_bank.deposit())

        elif option_select == 4:
            print(f"There have been {user_one_bank.total_withdraw} withdraws.")
            if option_select == 4 and user_two != None:
                print(f"There have been {user_two_bank.total_withdraw} withdraws.")

        elif option_select == 5:
            print(f"Hello, {user_one.name.title()}. There have been {user_one_bank.total_deposit} deposits.")
            if option_select == 5 and user_two != None:
                print(f"Hello, {user_one.name.title()}. There have been {user_two_bank.total_deposit} deposits.")

        elif option_select == 6:
            print("Thank you for using Aeron's Bank!")
            return False
            break

        else:
            print('Please only select a number from the list below. Thank you!')


def bank_creation(name):
    balance = float(input(f"{name.title()}, how much money do you have? "))
    return balance

while True:
    print("Welcome to Aeron's Bank")
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    gender = input('Please enter your gender: ')
    user_one = UserInfo(name, age, gender)
    user_two = None
    new_user = input('Would you like to register a new person? Yes | No   Type "No" to create your account: ')
    if new_user.lower() == 'yes':
        name = input('Please enter the new person name: ')
        age = int(input('Please enter the new person age: '))
        gender = input('Please enter the new person gender: ')
        user_two = UserInfo(name, age, gender)
        print('Thankyou for registering another person')
        user_one_balance = bank_creation(user_one.name)
        user_two_balance = bank_creation(user_two.name)
        user_one_bank = Bank(user_one.name, user_one.age, user_one.gender, user_one_balance)
        user_two_bank = Bank(user_two.name, user_two.age, user_two.gender, user_two_balance)
        option_two = options(user_two)
        if option_two == False:
            break

    else:
        user_one_balance = bank_creation(user_one.name)
        user_one_bank = Bank(user_one.name, user_one.age, user_one.gender, user_one_balance)
        option_two = options(user_two)
        if option_two == False:
            break








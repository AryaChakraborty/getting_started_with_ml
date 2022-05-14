# created an ATM machine which helps an user to create a pin, withdraw, deposit and check balance from a bank.
class Atm() :
    def __init__(self) :
        self.pin = ""
        self.balance = 0.0
        self.menu()
    def menu(self) :
        x = int(input('''press the corresponding number :
                    1. set pin
                    2. check balance
                    3. deposit
                    4. withdraw
                    5. exit
                    '''))
        while(x != 5) :
            if(x == 1) :
                self.set_pin()
            elif(x == 2) :
                self.check_balance()
            elif(x == 3) :
                self.deposit()
            elif(x == 4) :
                self.withdraw()
            x = int(input('''press the corresponding number :
                    1. set pin
                    2. check balance
                    3. deposit
                    4. withdraw
                    5. exit
                    '''))
        print("bye.")
    def set_pin(self) :
        self.pin = int(input("give the pin "))
        print("pin set successfully")
    def check_balance(self) :
        user_input = int(input("give the pin "))
        if(user_input == self.pin) :
            print(self.balance)
        else :
            print("invalid pin")
    def deposit(self) :
        user_input = int(input("give the pin "))
        if(user_input == self.pin) :
            self.balance += int(input("give the amount "))
        else :
            print("invalid pin")
    def withdraw(self) :
        user_input = int(input("give the pin "))
        if(user_input == self.pin) :
            amount = int(input("give the amount "))
            if(amount <= self.balance) :
                self.balance -= amount
            else :
                print("not enough balance")
        else :
            print("invalid pin")
    
bank_name = Atm()

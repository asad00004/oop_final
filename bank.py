class Bank:
    def __init__(self, name, address, initial_principal) -> None:
        self.name = name 
        self.address = address
        self.__balance = initial_principal
        self.__loan_given = 0
        self.loan_available = True
        self.users = []
        self.admins = []

    def add_user(self, user):
        self.users.append(user)

    def add_admin(self, admin):
        self.admins.append(admin)

    def take_deposite(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount
        
    def grant_loan(self, amount):
        self.__balance -= amount
        self.__loan_given += amount

    @property
    def balance(self):
        return self.__balance
    
    @property
    def loan(self):
        return self.__loan_given

class Person:
    def __init__(self, name, address, phone, email) -> None:
        self.name = name 
        self.address = address
        self.phone = phone
        self.email = email

class User(Person):
    def __init__(self, name, address, phone, email, bank, initial_deposite) -> None:
        super().__init__(name, address, phone, email)
        self.__balance = initial_deposite
        self.__loan = 0
        self.transaction = [f'initial deposite: {initial_deposite}']
        bank.take_deposite(initial_deposite)

    def check_balance(self):
        print(f'name: {self.name}, balance: {self.__balance} BDT')

    def deposite(self, bank, amount):
        self.__balance += amount
        self.transaction.append(f'deposite: {amount}')
        bank.take_deposite(amount)

    def withdraw(self, bank, amount):
        if self.__balance < amount:
            print(f"Sorry! You don't have enough cash. Your balance is {self.__balance} BDT")
        elif bank.balance < amount:
            print(f"******** The {bank.name} is now bankcrupt ********")
        else:
            self.__balance -= amount
            self.transaction.append(f'withdrawal: {amount}')
            bank.withdraw(amount)
            print(f'Sir, here is your BDT {amount}')

    def transfer(self, other, amount):
        if self.__balance < amount:
            print(f"Sorry! Your don't have enough money. Your balance is {self.__balance} BDT")
        else:
            self.__balance -= amount
            self.transaction.append(f'Send money : {amount}')
            other.__balance += amount
            other.transaction.append(f'Received money : {amount}')

    def take_loan(self, bank, amount):
        if not bank.loan_available:
            print('Sorry! Our loan feature is currently unavailable.')
        elif (2 * self.__balance < amount):
            print(f'Sorry, you can have maximum BDT {2 * self.__balance} loan.')
        elif bank.balance < amount:
            print(f"******** Sorry! We do not have enough Fund at the moment ********") 
        else:
            self.__loan += amount
            self.transaction.append(f'loan: {amount}')  
            bank.grant_loan(amount)
            print(f'Sir, here is your loan BDT {amount}')

    def transaction_history(self):
        print('transaction history: ')
        for each in self.transaction:
            print(each)


class Admin(Person):
    def __init__(self, name, address, phone, email) -> None:
        super().__init__(name, address, phone, email)

    def check_total_balance(self, bank):
        print(f'Total balance: {bank.balance} BDT')

    def check_total_loan(self, bank):
        print(f'Total loan given: {bank.loan} BDT')
    
    def loan_feature(self, bank, status):
        bank.loan_available = status

# Creating a bank with sonme user and an admin
bank1 = Bank('Sonali Bank', 'Chandpur', 50000)
user1 = User('Mokbul', 'Chandpur', 1234, 'mokbul@gmail.com', bank1, 5000)
bank1.add_user(user1)
user2 = User('Rokibul', 'Chandpur', 1254, 'rokibul@gmail.com', bank1, 5000)
bank1.add_user(user2)
admin = Admin('Safayat', 'Foridpur', 1122, 'safayet@yahoo.com')
bank1.add_admin(admin)

user1.deposite(bank1, 10000)
user1.take_loan(bank1, 20000)

user2.deposite(bank1, 50000)
user1.check_balance()
user2.check_balance()
user2.transfer(user1, 50000)
user1.check_balance()
user2.check_balance()

user2.transaction_history()

admin.loan_feature(bank1, False)
user2.take_loan(bank1, 10000)
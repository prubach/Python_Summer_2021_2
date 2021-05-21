class Customer:
    last_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)

class Account:
    last_id = 0
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print('New deposit updated as: ' + str(self._balance))
        else:
            print('The amount is negative')

    def charge(self, amount):
        if amount > self._balance:
            raise NotEnoughBalanceException("You don't have enough Balance. Your Current Balance is " + str(self._balance))
        if amount <= 0:
            raise NegativeAmountException("The amount is negative. Please input the positive amount")
        else:
            self._balance -= amount
            print("Charge amount is: " + str(amount))
            print("New Balance updated as: " + str(self._balance))

    def __repr__(self):
        return 'Account[{},{},{}]'.format(self.id, self.customer.lastname, self._balance)


class SavingsAccount(Account):
    interest_rate = 0.01
    def calc_interest(self):
        self._balance += self.interest_rate * self._balance

class CheckingAccount(Account):
    pass

class BankException(Exception):
    pass

class NegativeAmountException(BankException):
    pass

class NotEnoughBalanceException(BankException):
    pass

class Bank:
    # Customer Factory
    def new_customer(self, first_name, last_name):
        c = Customer(first_name, last_name)
        #TODO add customer to a list

    # Add account factory to bank

    # Implement transfer
    def transfer(self, from_acc_id, to_acc_id):
        #TODO implement
        pass

c1 = Customer('John', 'Smith')
print(c1)
c2 = Customer('Anne', 'Brown')
print(c2)
del c2
c2 = Customer('Anne2', 'Brown')
print(c2)
a1 = SavingsAccount(c1)
a2 = CheckingAccount(c2)
print(a1)
a1.deposit(100)
a2.deposit(200)
a1.calc_interest()
print(a1)
print(a2)
try:
    a1._balance = 'abc'
    a1.calc_interest()
    a1.charge(-200)
    print('After charging')
    print(a1)
except NotEnoughBalanceException as nebe:
     print('Exception: ' + str(nebe))
except BankException as nebe:
 #except BankException as nebe:
     print('General Exception: ' + str(nebe))
# except NegativeAmountException as nae:
#     print('Exception: ' + str(nae))
print('running further')


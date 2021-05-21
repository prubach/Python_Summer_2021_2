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
        self.balance = 0

    def deposit(self, amount):
        #TODO
    def charge(self, amount):
        #TODO
    def __repr__(self):
        return 'Account[{},{},{}]'.format(self.id, self.customer.lastname, self.balance)


class SavingsAccount(Account):
    #TODO - interest_rate calculation
    pass

class CheckingAccount(Account):
    pass


c1 = Customer('John', 'Smith')
print(c1)
c2 = Customer('Anne', 'Brown')
print(c2)
a1 = Account(c1)
a2 = Account(c2)
print(a1)
print(a2)
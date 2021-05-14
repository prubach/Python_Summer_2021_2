class Customer:
    customer_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.customer_id += 1
        self.id = Customer.customer_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)



c1 = Customer('John', 'Smith')
print(c1)
c2 = Customer('Anne', 'Brown')
print(c2)
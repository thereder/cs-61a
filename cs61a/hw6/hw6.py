
# Q0.
# Q1.

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock is 0:
            return 'Machine is out of stock.'
        if self.balance < self.price:
            return 'You must deposit ${0} more.'.format(self.price - self.balance)
        else:
            temp = 'Here is your {0}'.format(self.item)
            self.stock -= 1
            if self.balance > self.price:
                temp += ' and ${0} change.'.format(self.balance - self.price)
            else:
                temp += '.'
            self.balance = 0
            return temp

    def restock(self, amount):
        self.stock += amount
        return 'Current {0} stock: {1}'.format(self.item, self.stock)

    def deposit(self, amount):
        if self.stock > 0:
            self.balance += amount
            return 'Current balance: ${0}'.format(self.balance)
        else:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)

# Q2.

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, object):
        self.methods = [method for method in dir(object)]
        self.object = object

    def ask(self, *args):
        string = args[0]
        if 'please' not in string:
            return 'You must learn to say please first.'
        else:
            found = None
            for m in self.methods:
                if str(m) in string:
                    found = 'self.object.{0}{1}'.format(m,args[1:])
            if found is not None:
                return eval(found)
            else:
                return 'Thanks for asking, but I know not how to'+str(string[6:])
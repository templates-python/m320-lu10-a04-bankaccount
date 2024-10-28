""" provides a class for a bank account """
from customer import Customer


class BankAccount:
    """
    A normal bank account

    Attributes:
    -----------
    - owner: Customer
      the owner of the bank account
    - balance: float
        the current balance of the bank account
    - interest: float
        the interest rate of the bank account
    - type: str
        the type of the bank account. 'Standard bank account' is the default
    """

    def __init__(self, owner, initial_balance, interest):
        """
        Initializes the object
        :param owner: The owner of the bank account
        :param initial_balance: The initial balance of the bank account
        :param interest: The interest rate
        """
        self._owner = owner
        self._balance = initial_balance
        self._interest = interest
        self._type = 'Standard bank account'
        owner.add_bank_account(self)

    def has_available(self, amount):
        """
        Checks if the account has enough money to withdraw the amount
        """
        return amount <= self._balance

    def deposit_money(self, amount):
        """
        Deposits money to the account
        :param amount: The amount to deposit
        """
        self._balance += amount

    def withdraw_money(self, amount):
        """
        Withdraws money from the account
        :param amount: The amount to withdraw
        """
        if self.has_available(amount):
            self._balance -= amount
            return amount
        else:
            print('Not enough money available')
            return 0

    @property
    def owner(self):
        """
        Returns the owner of the bank account
        :return: The owner of the bank account
        """
        return self._owner

    @property
    def balance(self):
        """
        Returns the balance of the bank account
        :return: The balance of the bank account
        """
        return self._balance

    @property
    def interest(self):
        """
        Returns the interest rate of the bank account
        :return: The interest rate of the bank account
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """
        Sets the interest rate of the bank account
        :param interest: The interest rate of the bank account
        """
        self._interest = interest

    @property
    def type(self):
        """
        Returns the type of the bank account
        :return: The type of the bank account
        """
        return self._type

    def __str__(self):
        output = '------------------------------------------------\n'
        output += f'Kunde    : {self.owner.name}' + '\n'
        output += f'Kontotyp : {self._type}' + '\n'
        output += f'\tSaldo: {self.balance}' + '\n'
        output += f'\tZins : {self.interest}'
        return output


# Test
if __name__ == '__main__':
    p = Customer('Pia', 24)
    ac = BankAccount(p, 3500.00, 1.75)
    print(ac)

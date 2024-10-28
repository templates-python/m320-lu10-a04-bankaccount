""" provides a class for a salary account """

from bankaccount import BankAccount
from customer import Customer

class SalaryAccount(BankAccount):
    """
    A salary account
    
    Attributes:
    -----------
    - owner: Customer
        the owner of the bank account
    - balance: float
        the current balance of the bank account
    - interest: float
        the interest rate of the bank account
    - overdraw: float
        the maximum amount that can be overdrawn
    - type: str
        the type of the bank account. 'Salary bank account' is the default
    """
    def __init__(self, owner, deposit, interest, overdraft):
        """
        Initializes the object
        :param owner: The owner of the bank account
        :param deposit: The initial balance of the bank account
        :param interest: The interest rate
        :param overdraft: The maximum amount that can be overdrawn
        
        """
        super().__init__(owner, deposit, interest)
        self.overdraft = overdraft
        self._type    = 'Salary bank account'

    def has_available(self, amount):
        """
        Checks if the account has enough money to withdraw the amount
        """
        return amount <= (self._balance + self._overdraft)

    @property
    def overdraft(self):
        """
        Returns the overdraft of the account
        :return: The overdraft of the
        """
        return self._overdraft

    @overdraft.setter
    def overdraft(self, overdraft):
        """
        Sets the overdraft of the account
        :param overdraft: The overdraft of the account
        """
        self._overdraft = overdraft


    def __str__(self):
        """
        Returns a string representation of the account
        """
        output = super().__str__() + '\n'
        output += f'\tÜberzug: {self.overdraft}'
        return output

#Test
if __name__ == '__main__':
    p  = Customer('Pia', 24)
    sc = SalaryAccount(p, 3500.00, 1.75, 1000.00)
    print(sc)
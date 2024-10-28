""" This module contains the class Customer.  """
from person import Person
from account_index_exception import AccountIndexException



class Customer(Person):
    """
    Defines a customer as a person who has one or more bank accounts.

    Attributes
    ----------
    - name: str
        The full name of the customer
    - age: int
        The age of the customer
    - accounts: list
        A list of bank accounts the customer has
    """

    def __init__(self, name, age):
        """
        Initializes the object
        :param name: Name of the customer
        :param age: The age of the customer
        """
        super().__init__(name, age)
        self._accounts = []

    def take_bank_account(self, index):
        """
        Returns the bank account at the given index
        :param index: The index of the bank account
        :return: The bank account at the given index
        :raises AccountIndexException: If the index is out of range
        """
        if index < self.number_of_accounts:
            return self._accounts[index]
        raise AccountIndexException(index, len(self._accounts))

    def add_bank_account(self, account):
        """
        Adds a bank account to the customer
        :param account: The bank account to add
        """
        self._accounts.append(account)

    @property
    def current_assets(self):
        """
        Returns the current assets of the customer
        :return: The current assets of the customer
        """
        asset = 0
        for account in self._accounts:
            asset += account.balance
        return asset


    def _str__(self):
        """
        Returns a string representation of the customer and his/her accounts
        """
        output = super().__str__() + '\n'
        for account in self._accounts:
            output += account + '\n'


if __name__ == '__main__':
    from bankaccount import BankAccount
    from salary_account import SalaryAccount
    c  = Customer('Pia', 34)
    bc = BankAccount(c, 1000.00, 1.5)
    sc = SalaryAccount(c, 5000.00, 2.25, 2500.0)
    print(c)
import pytest

from bankaccount import BankAccount
from customer import Customer

class TestBankAccount:

    @pytest.fixture
    def owner(self):
        return Customer('Ria', 1995)

    @pytest.fixture
    def bc(self, owner):
        return BankAccount(owner, 1000.0, 4.5)

    def test_bank_account_init(self, bc, owner):
        assert bc.owner == owner
        assert bc.balance == 1000.0
        assert bc.interest == 4.5
        assert bc.type == 'Standard bank account'

    def test_set_get_interest(self, bc):
        bc.interest = 4.5
        assert bc.interest == 4.5

    def test_pay_in_bank_account(self, bc):
        bc.pay_in_money(500.0)
        assert bc.balance == 1500.0

    def test_withdraw_bank_account_well(self, bc):
        assert bc.has_available(600.0) == True
        assert bc.balance == 400.0

    def test_withdraw_bank_account_empty(self, bc):
        assert bc.has_available(1000)
        assert bc.balance == 0

    def test_withdraw_bank_account_ugly(self, bc):
        assert bc.has_available(2000.0) == False

    def test_bank_account_print(self,bc, capsys):
        print(bc)
        captured = capsys.readouterr()
        assert captured.out == '------------------------------------------------\nKunde    : Ria\nKontotyp : Standard bank account\n\tSaldo: 1000.0\n\tZins : 4.5\n'
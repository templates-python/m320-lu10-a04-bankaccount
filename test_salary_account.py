import pytest

from salary_account import SalaryAccount
from customer import Customer


class TestSalaryAccount:

    @pytest.fixture
    def owner(self):
        return Customer('Ria', 1995)

    @pytest.fixture
    def bc(self, owner):
        return SalaryAccount(owner, 1000.0, 4.5, 500)

    def test_salary_account_init(self, bc, owner):
        assert bc.owner == owner
        assert bc.balance == 1000.0
        assert bc.interest == 4.5
        assert bc.overdraft == 500
        assert bc.type == 'Salary bank account'

    def test_set_get_overdraw(self, bc):
        bc.overdraft = 250
        assert bc.overdraft == 250

    def test_withdraw_salary_account_well(self, bc):
        assert bc.has_available(600.0) is True
        assert bc.withdraw_money(600.0) == 600.0
        assert bc.balance == 400.0

    def test_withdraw_salary_account_overdraw(self, bc):
        assert bc.has_available(1200.0) is True
        assert bc.withdraw_money(1200.0) == 1200.0
        assert bc.balance == -200.0

    def test_withdraw_salary_account_all(self, bc):
        assert bc.has_available(1500)
        assert bc.withdraw_money(1500.0) == 1500.0
        assert bc.balance == -500

    def test_withdraw_salary_account_ugly(self, bc):
        assert bc.has_available(1501.0) is False

    def test_salary_account_print(self, bc, capsys):
        print(bc)
        captured = capsys.readouterr()
        assert captured.out == \
               '------------------------------------------------\nKunde    : Ria\n' \
               'Kontotyp : Salary bank account\n\tSaldo: 1000.0\n\tZins : 4.5\n\tÜberzug: 500\n'
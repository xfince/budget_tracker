import pytest
from project import Income, user_income, user_expenses, generate_feedback

# Test for Income class
def test_add_income():
    budget = Income()
    budget.add_income(1000)
    assert budget._income == 1000

def test_add_expense():
    budget = Income()
    budget.add_expense("Rent", 500)
    assert budget._expenditure["Rent"] == 500
    budget.add_expense("Rent", 300)
    assert budget._expenditure["Rent"] == 800

def test_user_balance():
    budget = Income()
    budget.add_income(1000)
    budget.add_expense("Rent", 500)
    budget.add_expense("Food", 200)
    assert budget.user_balance() == 300

def test_generate_summary():
    budget = Income()
    budget.add_income(1000)
    budget.add_expense("Rent", 500)
    budget.add_expense("Food", 200)
    summary = budget.generate_summary()
    assert "Income: 1000$" in summary
    assert "Rent: 500$" in summary
    assert "Food: 200$" in summary
    assert "Balance: 300$" in summary

def test_list_entries():
    budget = Income()
    budget.add_income(1000)
    budget.add_expense("Rent", 500)
    entries = budget.list_entries()
    assert "Income: 1000$" in entries
    assert "Rent: 500$" in entries

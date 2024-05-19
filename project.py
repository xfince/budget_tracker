logo = """
                                       _   _               _            _     _                  _             
                                      | | | |             | |          | |   | |                | |            
 _ __   ___ _ __ ___  ___  _ __   __ _| | | |__  _   _  __| | __ _  ___| |_  | |_ _ __ __ _  ___| | _____ _ __ 
| '_ \ / _ \ '__/ __|/ _ \| '_ \ / _` | | | '_ \| | | |/ _` |/ _` |/ _ \ __| | __| '__/ _` |/ __| |/ / _ \ '__|
| |_) |  __/ |  \__ \ (_) | | | | (_| | | | |_) | |_| | (_| | (_| |  __/ |_  | |_| | | (_| | (__|   <  __/ |   
| .__/ \___|_|  |___/\___/|_| |_|\__,_|_| |_.__/ \__,_|\__,_|\__, |\___|\__|  \__|_|  \__,_|\___|_|\_\___|_|   
| |                                                           __/ |                                            
|_|                                                          |___/                                             
"""

print(logo)
class Income:
    """Class to hold the calculation of the person's budget."""
    def __init__(self):
        self._income = 0
        self._expenditure = {}

    def add_income(self, amount):
        """Adds income to the user's total income."""
        self._income += amount

    def add_expense(self, name, amount):
        """Adds an expense to the expenditure dictionary."""
        if name in self._expenditure:
            self._expenditure[name] += amount
        else:
            self._expenditure[name] = amount

    def user_balance(self):
        """Calculates and returns the balance."""
        total_expense = sum(self._expenditure.values())
        balance = self._income - total_expense
        return balance

    def generate_summary(self):
        """Generates and returns the summary of all entries."""
        summary = f"Income: {self._income}$\n"
        summary += "Expenses:\n"
        for name, amount in self._expenditure.items():
            summary += f"  {name}: {amount}$\n"
        summary += f"Balance: {self.user_balance()}$"
        return summary

    def list_entries(self):
        """Returns a list of all income and expense entries."""
        entries = f"Income: {self._income}$\n"
        entries += "Expenses:\n"
        for name, amount in self._expenditure.items():
            entries += f"  {name}: {amount}$\n"
        return entries


def main():
    """Contains the main functionality of all function and the Income class."""
    print("Hello! Welcome to Your Personal Budget Tracker")
    budget = Income()
    income_of_month = user_income()
    budget.add_income(income_of_month)
    user_expenses(budget)
    generate_feedback(budget)


def user_income():
    """Only gets the users income at the start of the program and no longer called."""
    while True:
        try:
            return int(input("Your monthly income please: "))
        except ValueError:
            print("The input was rejected. Please try again, probably due to a comma or mistyped values.")
            continue
        else:
            break


def user_expenses(budget):
    """Allow the user to input expenditure which adds to a dictionary."""
    print("\nPlease type the expenditure's name and hit enter, then how much you spent. Thank You.")
    print("Type STOP to move on in either of the slots.")
    while True:
        monthly_expenditure_expense = input("Name of the expenditure please: ")
        if monthly_expenditure_expense.lower() == "stop":
            print("Stopped")
            break
        try:
            monthly_expenditure = input("How much did you spend? ")
            if monthly_expenditure.lower() == "stop":
                print("Stopped")
                break
            monthly_expenditure = int(monthly_expenditure)
            budget.add_expense(monthly_expenditure_expense, monthly_expenditure)
        except ValueError:
            print("The input was rejected. Please try again, probably due to a comma or mistyped values.")
            continue


def generate_feedback(budget):
    """Allows the user to choose whether they want to print out the list of entries, 
    generate a summary report, or show the balance only."""
    print("\nThanks! I have all the information required. What do you want me to do?")
    print("Pick only the first letters of the following options to get your desired choice. \nPress any other character to leave the program successfully.")
    print("List your monthly entries.")
    print("Generate a summary report.")
    print("Balance only.")
    choice = input().strip().lower()

    if choice == 'l':
        print("\nHere are your monthly entries:")
        print(budget.list_entries())
    elif choice == 'g':
        print("\nHere is your summary report:")
        print(budget.generate_summary())
    elif choice == 'b':
        print("\nHere is your balance:")
        balance = budget.user_balance()
        if balance < 0:
            print("I'm afraid you probably ran into some debts with your expenditure.")
            debt = -balance
            print(f"Your debt is: {debt}$")
        elif balance == 0:
            print("Really balanced your expenditure there. Your balance is 0$.")
        else:
            print(f"Here is your balance: {balance}$")
    else:
        print("You have succesfully left the program.")


if __name__ == "__main__":
    main()

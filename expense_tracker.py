# Simple Expense Tracker in Python

expenses = []  # List to store all expenses

# Function to add a new expense
def add_expense():
    print("\n---- Add New Expense ----")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Bills, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    if not amount.replace('.', '', 1).isdigit():
        print("Invalid amount. Please enter a number.\n")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": float(amount),
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully.\n")

# Function to view all expenses
def view_expenses():
    print("\n---- All Expenses ----")
    if not expenses:
        print("No expenses recorded.\n")
        return

    for i, expense in enumerate(expenses):
        print(f"{i+1}. Date: {expense['date']} | Category: {expense['category']} | Amount: ${expense['amount']} | Description: {expense['description']}")
    print()

# Function to show total expenses by category
def total_by_category():
    print("\n---- Total Expenses by Category ----")
    cat = input("Enter category: ")
    total = 0

    for expense in expenses:
        if expense['category'].lower() == cat.lower():
            total += expense['amount']

    print(f"Total spent in '{cat}': ${total:.2f}\n")

# Function to delete an expense by number
def delete_expense():
    print("\n---- Delete Expense ----")
    view_expenses()
    entry = input("Enter expense number to delete: ")

    if entry.isdigit():
        entry = int(entry)
        if 0 < entry <= len(expenses):
            deleted = expenses.pop(entry - 1)
            print(f"Deleted: {deleted['description']} - ${deleted['amount']}\n")
        else:
            print("Invalid entry number.\n")
    else:
        print("Please enter a valid number.\n")

# Main menu
def main_menu():
    while True:
        print("======= Expense Tracker =======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the app
main_menu()

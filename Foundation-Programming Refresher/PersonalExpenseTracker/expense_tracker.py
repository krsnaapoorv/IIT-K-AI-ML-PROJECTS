# Personal Expense Tracker

import csv
import os

expenses = []
budget = 0
FILE_NAME = "expenses.csv"


# -------------------------------
# Load expenses from CSV and handle invalid entries befor displaying them
# -------------------------------
def load_expenses():
    global expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expense = {
                        'date': row['date'],
                        'category': row['category'],
                        'amount': float(row['amount']),
                        'description': row['description']
                    }
                    expenses.append(expense)
                except:
                    print("Skipping invalid row:", row)


# -------------------------------
# Save expenses to CSV as a dict and handle invalid entries before saving them
# -------------------------------
def save_expenses():
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

    print("Expenses saved successfully!")


# -------------------------------
# Add expense with date, category, amount, and description and handle invalid entries before adding them
# -------------------------------
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        if not date or not category or not description:
            print("All fields are required!")
            return

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount entered!")


# -------------------------------
# View expenses after looping through them and handling invalid entries before displaying them
# -------------------------------
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for i, exp in enumerate(expenses, start=1):
        if not all([exp.get('date'), exp.get('category'),
                    exp.get('amount'), exp.get('description')]):
            print(f"Skipping incomplete entry: {exp}")
            continue

        print(f"\nExpense {i}:")
        print(f"Date: {exp['date']}")
        print(f"Category: {exp['category']}")
        print(f"Amount: {exp['amount']}")
        print(f"Description: {exp['description']}")


# -------------------------------
# Set budget/ User can set a monthly budget and handle invalid entries before setting the budget
# -------------------------------
def set_budget():
    global budget
    try:
        budget = float(input("Enter monthly budget: "))
        print("Budget set successfully!")
    except ValueError:
        print("Invalid input!")


# -------------------------------
# Track budget and calculate total expenses and compare with the set budget, and handle invalid entries before tracking the budget
# -------------------------------
def track_budget():
    if budget == 0:
        print("Please set a budget first!")
        return

    total_expense = sum(exp['amount'] for exp in expenses)

    print(f"Total expenses: {total_expense}")
    print(f"Budget: {budget}")

    if total_expense > budget:
        print("⚠️ You have exceeded your budget!")
    else:
        print(f"✅ You have {budget - total_expense} left for the month.")


# -------------------------------
# Menu
# -------------------------------
def menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# -------------------------------
# Run Program
# -------------------------------
load_expenses()
menu()
from datetime import datetime

# -------------------------------
# Initial Expense Records
# -------------------------------

expenses = [
    {
        "Date": "01-09-2025",
        "Category": "Housing",
        "Amount": 3000,
        "Description": "Rent, mortgage, property tax, and insurance."
    },
    {
        "Date": "09-10-2025",
        "Category": "Transportation",
        "Amount": 10000,
        "Description": "Fuel, maintenance, and public transport."
    },
    {
        "Date": "20-05-2026",
        "Category": "Utilities",
        "Amount": 15000,
        "Description": "Electricity, water, gas, internet."
    },
    {
        "Date": "01-06-2026",
        "Category": "Healthcare",
        "Amount": 8000,
        "Description": "Medical insurance and doctor visits."
    },
    {
        "Date": "10-07-2026",
        "Category": "Housing",
        "Amount": 15000,
        "Description": "Monthly house rent."
    }
]

# -------------------------------
# Add Expense
# -------------------------------

def add_expense():

    date_format = "%d-%m-%Y"

    while True:
        date = input("Enter Date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, date_format)
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    category = input("Enter Category: ").strip().title()

    while True:
        try:
            amount = int(input("Enter Amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    description = input("Enter Description: ").strip()

    expenses.append({
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    })

    print("\nExpense added successfully!")

# -------------------------------
# View Expenses
# -------------------------------

def view_expenses():

    if not expenses:
        print("\nNo expense records available.")
        return

    print("\n" + "=" * 70)

    for expense in expenses:

        print(f"Date        : {expense['Date']}")
        print(f"Category    : {expense['Category']}")
        print(f"Amount      : ₹{expense['Amount']}")
        print(f"Description : {expense['Description']}")
        print("-" * 70)

# -------------------------------
# Total Expense
# -------------------------------

def total_expense():

    total = 0

    for expense in expenses:
        total += expense["Amount"]

    print(f"\nTotal Expense : ₹{total}")

# -------------------------------
# Search by Category
# -------------------------------

def search_category():

    category = input("Enter Category: ").strip().title()

    found = False

    print("\n" + "=" * 70)

    for expense in expenses:

        if expense["Category"] == category:

            found = True

            print(f"Date        : {expense['Date']}")
            print(f"Category    : {expense['Category']}")
            print(f"Amount      : ₹{expense['Amount']}")
            print(f"Description : {expense['Description']}")
            print("-" * 70)

    if not found:
        print("Expense record not found.")

# -------------------------------
# Delete Expense
# -------------------------------

def delete_expense():

    category = input("Enter Category: ").strip().title()

    found = False

    for expense in expenses[:]:

        if expense["Category"] == category:

            found = True
            expenses.remove(expense)

            print("\nExpense Deleted Successfully!")
            print(f"Date        : {expense['Date']}")
            print(f"Category    : {expense['Category']}")
            print(f"Amount      : ₹{expense['Amount']}")
            print(f"Description : {expense['Description']}")
            print("-" * 70)

    if not found:
        print("\nExpense record not found.")

# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n" + "=" * 50)
    print("           EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")
    print("=" * 50)

    try:

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            total_expense()

        elif choice == 4:
            search_category()

        elif choice == 5:
            delete_expense()

        elif choice == 6:
            print("\nThank You! 💕")
            break

        else:
            print("\nPlease enter a valid choice (1-6).")

    except ValueError:
        print("\nError: Please enter a valid integer.")
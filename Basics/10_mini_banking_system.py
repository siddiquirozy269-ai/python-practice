"""
============================================================
                 MINI BANKING SYSTEM
============================================================

A simple console-based banking system created using
Python fundamentals.

Features:
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Delete Account
6. Transfer Money
7. Exit

Concepts Used:
- Variables
- Input / Output
- Conditions
- for Loop
- while Loop
- Functions
- Lists
- Dictionaries
- Boolean Flags
- break
- return
- Exception Handling
- Basic Validation

Note:
No File Handling is used in this project.

Author   : Rozy
Language : Python
============================================================
"""


# ============================================================
#                     ACCOUNT DATA
# ============================================================

accounts = [
    {
        "account_number": 70112343,
        "name": "Rozy",
        "balance": 20000
    },
    {
        "account_number": 67345223,
        "name": "Alisha",
        "balance": 27000
    },
    {
        "account_number": 23432323,
        "name": "Gurleen",
        "balance": 60000
    },
    {
        "account_number": 89343422,
        "name": "Rashid",
        "balance": 10000
    },
    {
        "account_number": 43234322,
        "name": "Reema",
        "balance": 49000
    }
]


# ============================================================
#                    CREATE ACCOUNT
# ============================================================

def create_account():

    account_number = int(input("Enter the account number: "))
    name = input("Enter the name: ")
    balance = int(input("Enter the current balance: "))

    # Validate initial balance
    if balance <= 0:
        print("Balance must be greater than 0!")
        return

    # Check for duplicate account number
    duplicate = False

    for account in accounts:
        if account["account_number"] == account_number:
            duplicate = True
            break

    if duplicate:
        print("Duplicate account numbers are not allowed!")
        return

    # Create new account
    new_account = {
        "account_number": account_number,
        "name": name,
        "balance": balance
    }

    accounts.append(new_account)

    print("Account created successfully!")


# ============================================================
#                       DEPOSIT
# ============================================================

def deposit():

    amount = int(input("Enter the deposit amount: "))

    # Validate deposit amount
    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    account_number = int(input("Enter the account number: "))

    # Search for the account
    for account in accounts:

        if account["account_number"] == account_number:

            account["balance"] += amount

            print("Amount deposited successfully!")
            print(f"Current Balance: {account['balance']}")

            return

    print("Account number not found!")


# ============================================================
#                      WITHDRAW
# ============================================================

def withdraw():

    amount = int(input("Enter the withdrawal amount: "))

    # Validate withdrawal amount
    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    account_number = int(input("Enter the account number: "))

    # Search for the account
    for account in accounts:

        if account["account_number"] == account_number:

            # Check sufficient balance
            if account["balance"] >= amount:

                account["balance"] -= amount

                print("Amount withdrawn successfully!")
                print(f"Current Balance: {account['balance']}")

            else:
                print("Insufficient Balance!")

            return

    print("Account number not found!")


# ============================================================
#                    CHECK BALANCE
# ============================================================

def check_balance():

    account_number = int(input("Enter the account number: "))

    # Search for the account
    for account in accounts:

        if account["account_number"] == account_number:

            print(f"Account Holder: {account['name']}")
            print(f"Current Balance: {account['balance']}")

            return

    print("Account number not found!")


# ============================================================
#                    DELETE ACCOUNT
# ============================================================

def delete_account():

    account_number = int(input("Enter the account number: "))

    # Search for the account
    for account in accounts:

        if account["account_number"] == account_number:

            accounts.remove(account)

            print("Account deleted successfully!")

            return

    print("Account number not found!")


# ============================================================
#                    TRANSFER MONEY
# ============================================================

def transfer_money():

    sender_acc_num = int(
        input("Enter the sender's account number: ")
    )

    receiver_acc_num = int(
        input("Enter the receiver's account number: ")
    )

    transfer_amount = int(
        input("Enter the amount to transfer: ")
    )

    # Validate transfer amount
    if transfer_amount <= 0:
        print("Amount must be greater than 0!")
        return

    # Sender and receiver cannot be the same
    if sender_acc_num == receiver_acc_num:
        print("Transfer Rejected!")
        return

    found_sender = False
    found_receiver = False

    # Find sender account
    for account_sender in accounts:

        if sender_acc_num == account_sender["account_number"]:

            found_sender = True
            break

    if not found_sender:
        print("Sender's account not found!")
        return

    # Find receiver account
    for account_receiver in accounts:

        if receiver_acc_num == account_receiver["account_number"]:

            found_receiver = True
            break

    if not found_receiver:
        print("Receiver's account not found!")
        return

    # Check sender's balance
    if transfer_amount <= account_sender["balance"]:

        # Deduct amount from sender
        account_sender["balance"] -= transfer_amount

        # Add amount to receiver
        account_receiver["balance"] += transfer_amount

        print("Amount transferred successfully!")

    else:
        print("Insufficient Balance!")


# ============================================================
#                       MAIN MENU
# ============================================================

while True:

    print("\n" + "=" * 50)
    print("              MINI BANKING SYSTEM")
    print("=" * 50)

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Delete Account")
    print("6. Transfer Money")
    print("7. Exit")

    print("=" * 50)

    try:

        choice = int(
            input("Enter your choice (1-7): ")
        )

        if choice == 1:
            create_account()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            check_balance()

        elif choice == 5:
            delete_account()

        elif choice == 6:
            transfer_money()

        elif choice == 7:
            print("\nThank You for using the Mini Banking System!")
            print("Goodbye!")
            break

        else:
            print("Please enter a valid choice (1-7).")

    except ValueError:
        print("Error: Please enter a valid integer.")
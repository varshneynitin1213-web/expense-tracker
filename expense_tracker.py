import csv
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Description"])

# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!\n")
        return

    category = input("Enter category (Food/Travel/etc): ")
    description = input("Enter description: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])

    print("✅ Expense added successfully!\n")

# View expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No data found.\n")
        return

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        print("\n--- All Expenses ---")
        for row in reader:
            print(row)
    print()

# Calculate total expense
def total_expense():
    total = 0

    if not os.path.exists(FILE_NAME):
        print("No data found.\n")
        return

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header

        for row in reader:
            try:
                total += float(row[0])
            except:
                continue

    print(f"💰 Total Expense: {total}\n")

# Main menu
def main():
    initialize_file()

    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice, try again!\n")

# Run program
if __name__ == "__main__":
    main()
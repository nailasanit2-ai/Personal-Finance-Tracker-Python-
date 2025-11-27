import csv
from datetime import datetime

FILE_NAME = "data.csv"

def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            print("New data file created.")
    except FileExistsError:
        pass  

def add_expense():
    date = input("Enter date (DD-MM-YYYY) or leave blank for today: ")
    if date.strip() == "":
        date = datetime.now().strftime("%Y-%m-%d")

    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Transport, Bills, etc.): ")
    description = input("Description: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            print(row)

def main():
    initialize_file()

    while True:
        print("\n Yaya's Personal Expense Tracker ")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

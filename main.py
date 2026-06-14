from src.storage import load_expenses ,save_expenses
from src.tracker  import add_expense,show_summary

def main():
    expenses = load_expenses()

    while True:
        print("=== PERSONAL FINANCE TRACKER ===")
        print("1. Add expense")
        print("2. Show summary")
        print("3. Save & Exit")

        choice=input("Enter your choice (1-3):").strip()
        print()
        

        if choice=="1":
            add_expense(expenses)
        elif choice=="2":
            show_summary(expenses)
        elif choice=="3":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1,2 or 3.\n ")

if __name__=="__main__":
    main()

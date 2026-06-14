def add_expense(expenses_list):
    """Prompts user for input and adds an expense dictionary to the list."""
    try:
        amount=float(input("enter amount expense ($):"))

        if amount <=0:
            print("amount  must be greated than zero \n")
            return 
    except ValueError:
        print("Invalid input! Please enter a valid decimal number.\n")
        return 
    
    category=input("enter category (e.g Food, Transport ,Rent): ").strip().capitalize()
    if not category:
        category="uncategorized"

    expense ={
        "amount" : amount,
        "category":category,
    }
    expenses_list.append(expense)

    print(f"Added ${amount: .2f} under '{category}' successfully! \n")

def show_summary(expenses_list):
    """Iterates through the expenses list and prints a formatted summary."""
    if not expenses_list:
        print("No expenses recorded yet. \n")
        return 
    print("\n---- expenses summary ----\n")
    total_spent=0.0


    for item in expenses_list:
        print(f". ${item['amount'] : .2f} | category : {item['category']}")
        total_spent+=item['amount']

    print("-" * 25)
    print(f"total_spent :${total_spent: .2f}\n")

def create_expense(amount, category):
    """Creates a validated expense dictionary."""
    amount = float(amount)
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    category = str(category).strip().capitalize()
    if not category:
        category = "uncategorized"

    return {
        "amount": amount,
        "category": category,
    }


def get_summary(expenses_list):
    """Returns totals and category groups for expenses."""
    total_spent = 0.0
    categories = {}

    for item in expenses_list:
        amount = float(item["amount"])
        category = item["category"]
        total_spent += amount
        categories[category] = categories.get(category, 0.0) + amount

    return {
        "total_spent": total_spent,
        "categories": categories,
        "count": len(expenses_list),
    }


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
    expense = create_expense(amount, category)
    expenses_list.append(expense)

    print(f"Added ${amount: .2f} under '{expense['category']}' successfully! \n")

def show_summary(expenses_list):
    """Iterates through the expenses list and prints a formatted summary."""
    if not expenses_list:
        print("No expenses recorded yet. \n")
        return 
    print("\n---- expenses summary ----\n")
    summary = get_summary(expenses_list)


    for item in expenses_list:
        print(f". ${item['amount'] : .2f} | category : {item['category']}")

    print("-" * 25)
    print(f"total_spent :${summary['total_spent']: .2f}\n")

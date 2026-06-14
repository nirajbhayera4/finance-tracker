import os

DATA_FILE = "data/expenses.txt"

def load_expenses():
    """Reads data/expenses.txt and loads expenses back into a list."""
    expenses_list = []
    
    # Check if the file and directory exist before opening it
    if not os.path.exists(DATA_FILE):
        return expenses_list

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                # Remove whitespace and split by the delimiter
                line = line.strip()
                if line:
                    amount_str, category = line.split(",")
                    expenses_list.append({
                        "amount": float(amount_str),
                        "category": category
                    })
    except (FileNotFoundError, ValueError):
        print("⚠️ Warning: Could not parse saved data file. Starting fresh.")
        
    return expenses_list


def save_expenses(expenses_list):
    """Saves the current expenses list to data/expenses.txt."""
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w") as file:
        for item in expenses_list:
            # Write structured plain text: "amount,category"
            file.write(f"{item['amount']},{item['category']}\n")
    print("💾 Data saved safely to disk.")
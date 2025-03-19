import datetime

def login():
    """Handles user login."""
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if password == "3003":
            print("Login successful!")
            return True
        else:
            print("Incorrect password. Please try again.")

def milk_deposit():
    """Handles milk deposit records."""
    name = input("Enter milk deposit name: ")
    animal_type = input("Enter animal type (cow, goat, etc.): ")
    quantity = float(input("Enter milk quantity (liters): "))
    print(f"Milk deposit recorded: Name={name}, Animal={animal_type}, Quantity={quantity} liters.")

def animal_meal():
    """Handles animal meal selection and cost calculation."""
    meal_prices = {
        "Hay (Good)": 10,
        "Hay (Average)": 8,
        "Grain Mix (High)": 15,
        "Grain Mix (Medium)": 12,
    }
    selected_meals = {}
    while True:
        print("\nAvailable Animal Meal Products:")
        for meal, price in meal_prices.items():
            print(f"- {meal}: ${price} per unit")
        meal_choice = input("Enter meal name (or 'done' to finish): ")
        if meal_choice.lower() == "done":
            break
        if meal_choice in meal_prices:
            quantity = int(input(f"Enter quantity for {meal_choice}: "))
            selected_meals[meal_choice] = quantity
        else:
            print("Invalid meal choice. Please try again.")

    total_cost = 0
    print("\nSelected Meals:")
    for meal, quantity in selected_meals.items():
        price = meal_prices[meal]
        cost = price * quantity
        total_cost += cost
        print(f"- {meal}: {quantity} units, Cost: ${cost}")
    print(f"Total cost: ${total_cost}")

def loan_application():
    """Handles loan application."""
    loan_types = ["Car Loan", "Home Loan", "Agricultural Loan"]
    print("\nLoan Application:")
    for i, loan_type in enumerate(loan_types):
        print(f"{i + 1}. {loan_type}")
    try:
        choice = int(input("Select loan type (1-3): "))
        if 1 <= choice <= len(loan_types):
            print(f"Loan application for {loan_types[choice - 1]} submitted.")
        else:
            print("Invalid loan type selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def dairy_info():
    """Provides information about dairy farming."""
    print("\nDairy Farming Information:")
    print("Establishment: Dairy farming requires careful planning and investment in infrastructure.")
    print("Running: Regular feeding, milking, and health checks are essential for efficient operation.")
    print("Profits: Profits depend on milk yield, quality, and market prices.")
    print("Risks: Risks include disease outbreaks, feed shortages, and price fluctuations.")
    print("Risk Management: Implement bio security measures, secure feed supplies, and diversify income sources.")
    print("Quality Control: Regular testing of milk, hygiene of equipment and proper storage of milk are necessary.")
    print("Customer Satisfaction: Consistent quality and timely delivery of milk are crucial for customer satisfaction.")
    print("Timely Delivery: Proper planning of milk collection and transportation is essential for timely delivery.")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        now = datetime.datetime.now()
        print("\n--- Dairy Farm Management System ---")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("1. Manage Milk Deposits")
        print("2. Animal Meal")
        print("3. Loan Application")
        print("4. Dairy Information")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                milk_deposit()
            elif choice == 2:
                animal_meal()
            elif choice == 3:
                loan_application()
            elif choice == 4:
                dairy_info()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    if login():
        main_menu()
print("exercise2: Cinemax #2")

def calculate_user_tickets():
    user_family = {}
    total_cost = 0 
    print("Enter family members' names and ages (type quit for name to finish).")
    while True:
        # Get the family member's name
        name_input = input("Enter name: ").strip()
        if name_input.lower() == 'quit':
            break

        # Get the family member's age
        while True:
            try:
                age_input = int(input(f"Enter age for {name_input.title()}: "))
                if age_input >= 0:
                    user_family[name_input] = age_input
                    break
                else:
                    print("Age must be non-negative.")
            except ValueError:
                print("Invalid input. Please enter a whole number for age.")

    if not user_family:
        print("No family members entered. Exiting.")
        return

    print("-" * 28)
    # Loop through the user's family dictionary
    for name, age in user_family.items():
        ticket_price = 0

        # Apply the ticket pricing rules
        if age < 3:
            ticket_price = 0
        elif age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15

        print(f"**{name.title()}** (Age: {age}): ${ticket_price}")
        total_cost += ticket_price

    print("-" * 28)
    print(f"**Total family ticket cost: ${total_cost}**")


calculate_user_tickets()


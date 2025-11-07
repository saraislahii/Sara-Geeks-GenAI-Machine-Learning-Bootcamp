

print(" Exercise 9: Cinemax Tickets ")


ages_list = []
ticket_cost = 0

print("Please enter the age of each person in the family (enter 'done' when finished):")

while True:
    age = input("Enter age: ").strip()
    
    if age.lower() == 'done':
        break
        
    try:
        age_list = int(age)
        if age_list < 0:
            print("Age must be non-negative. Please try again.")
            continue
        ages_list.append(age_list)
        
        # Calculate individual ticket price
        if age_list < 3:
            price = 0
            print(f"  -> Age {age_list}: Free")
        elif 3 <= age_list <= 12:
            price = 10
            print(f"  -> Age {age_list}: $10")
        else: # age > 12
            price = 15
            print(f"  -> Age {age_list}: $15")
            
        ticket_cost += price

    except ValueError:
        # Catch non-integer input (like "hello" or "5.5")
        print("Invalid input. Please enter a whole number or 'done'.")
        

print(f" Total Ticket Cost: ${ticket_cost}")





print("Exercise 6: While Loop ")

# Use a while True loop to run indefinitely until a 'break' condition is met
while True:
    user_name = input("Enter your name: ").strip() # strip() is used in case the user enters only spaces.
    
    
    if user_name.isdigit():
        print("Give the correct name: Name cannot consist only of digits.")
        continue # Restart the loop
    
    # Check if the name is too short (less than 3 letters)
    elif len(user_name) < 3:
        print("Give the correct name: Name must be at least 3 letters long.")
        continue # Restart the loop
        
    # If both checks pass, the input is correct
    else:
        print(f"Thank you")
        break # Exit the loop
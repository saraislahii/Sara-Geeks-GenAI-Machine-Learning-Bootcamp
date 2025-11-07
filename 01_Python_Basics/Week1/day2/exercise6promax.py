while True:
    user_name = input("Enter your name: ").strip()
    #1. check lenth
    if len(user_name) < 3:
        print("Give the correct name: Name must be at least 3 letters long.")
        continue
    

    # 2.isdigit()  check every character:
    if any(char.isdigit() for char in user_name) is True:
        print("Error: Name cannot contain digits.")
        continue
    
    # 4. A supplementary check: confirm everything else is a letter.
    if not user_name.isalpha():
        print("Error: Name can only contain letters and spaces (no symbols).")
        continue

    # 5. If all checks pass, the input is valid.
    print(f"Thank you")
    break # Exit the loop

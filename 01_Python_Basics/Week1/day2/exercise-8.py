print("exercise8")
# Initialize an empty list
topping_list = []

print("Enter a topping. Type quite when finished.")

# Loop indefinitely until a 'break' condition is met
while True:
    topping = input("Add an topping : ").strip().lower()

    if topping == 'quit':
        break  # Exit the while loop
    elif topping:
        print(f"adding {topping} to your pizza")
        topping_list.append(topping)
    else:
        print("Empty input ignored. Please enter an item or 'done'.")
totale=len(topping_list)*2.5+20
print(f"your total is {totale} USD" )

print("exercise 6: Magicians...")
# Step 1: Create a List of Magician Names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Step 2: Create a Function to Display Magicians
def show_magicians(names):
    """Iterates through a list of names and prints each one."""
    print("\nOriginal Magicians:")
    for name in names:
        print(name)

# Step 3: Create a Function to Modify the List
def make_great(names):
    """Adds 'The Great' before each magician's name in the list."""
    # Note: Modifying the list in place
    for i in range(len(names)):
        names[i] = names[i]+ " The Great " 
    return 

# Step 4: Call the Functions

# Call 1: Modify the list
make_great(magician_names)

# Call 2: Display the modified list
show_magicians(magician_names)


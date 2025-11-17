print("Exercise 2 :: Dogs")



# Step 1: Create the Dog Class
class Dog:
  
    def __init__(self, name, height):
        # Initialize attributes
        self.name = name
        self.height = height

    def bark(self):
        
        print(f"{self.name} goes woof!")

    def jump(self):
      
        jump_height = self.height * 2
        print(f"{self.name} jumps{jump_height} cm high!")


# Step 2: Create Dog Objects

print("--- Dog Object Instantiation ---")
davids_dog = Dog("Ranger", 60) 
sarahs_dog = Dog("Lucy", 35)   
print(f"Created two dogs: {davids_dog.name} ({davids_dog.height}cm) and {sarahs_dog.name} ({sarahs_dog.height}cm).")


# Step 3: Print Dog Details and Call Methods


print("\n--- Ranger's Actions ---")
print(f"Name: {davids_dog.name}, Height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print("\n--- Lucy's Actions ---")
print(f"Name: {sarahs_dog.name}, Height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()


# Step 4: Compare Dog Sizes


print("\n--- Comparing Dog Heights ---")

if davids_dog.height > sarahs_dog.height:
    print(f"Comparison Result: {davids_dog.name}is taller than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"Comparison Result: {sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"Comparison Result: {davids_dog.name} and {sarahs_dog.name} are the same height!")


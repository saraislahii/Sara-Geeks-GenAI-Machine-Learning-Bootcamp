
# Step 1: Create the Dog Class



class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age 
        self.weight = weight 

    def bark(self):
        
        return f"{self.name} is barking!"

    def run_speed(self):
        speed = (self.weight / self.age) * 10
        return round(speed, 2)

    def fight(self, other_dog):
        
        # Calculate power for the current dog (self)
        self_power = self.run_speed() * self.weight
        
        # Calculate power for the opponent (other_dog)
        other_power = other_dog.run_speed() * other_dog.weight

        print(f"\n--- {self.name} vs. {other_dog.name} ---")
        print(f"{self.name}'s Power: {round(self_power, 2)}")
        print(f"{other_dog.name}'s Power: {round(other_power, 2)}")

        if self_power > other_power:
            return f"**WINNER**: {self.name} won the fight! ({self.name} is bigger and faster)"
        elif other_power > self_power:
            return f"**WINNER**: {other_dog.name} won the fight! ({other_dog.name} is bigger and faster)"
        else:
            return "It's a tie! Both dogs have equal fighting power."

# Step 2: Create Dog Instances

# Dog 1: Young and heavy (High Speed/Power)
dog1 = Dog(name="Max", age=2, weight=40) 

# Dog 2: Older and lighter (Lower Speed/Power)
dog2 = Dog(name="Rocky", age=8, weight=25) 

# Dog 3: Middle age, mid weight
dog3 = Dog(name="Bella", age=4, weight=30) 


# Step 3: Test Dog Methods


# Test Bark
print("\n--- Test 1: Barking ---")
print(dog1.bark())
print(dog3.bark())


# Test Fights
print("\n--- Test 2: run speed ---")
print(dog1.run_speed())
print(dog2.run_speed())
# Fight 1: Young/Heavy (Max) vs. Old/Light (Rocky)
print(dog1.fight(dog2))

# Fight 2: Middle (Bella) vs. Old/Light (Rocky)
print(dog3.fight(dog2))
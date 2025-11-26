
# Base Classes Provided in the Exercise

class Pets:
    """Manages a collection of animals and provides common methods."""
    def __init__(self, animals):

        self.animals = animals

    def walk(self):
        """
        Calls the walk() method on every animal in the list.
        This demonstrates Polymorphism.
        """
        print("\n--- Taking all pets for a walk ---")
        for animal in self.animals:
            # Polymorphism: The same method call produces different results
            # based on the object's actual class (Cat, Bengal, Chartreux, Siamese).
            print(animal.walk())

class Cat:
    """The base class for all cat breeds."""
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        #Default walk behavior for a cat.
        return f'Cat {self.name} (Age: {self.age}) is just strolling around.'

class Bengal(Cat):
    #Specific Cat breed demonstrating inheritance.
    def sing(self, sounds):
        return f'Bengal {self.name} says {sounds}'

class Chartreux(Cat):
    #Specific Cat breed demonstrating inheritance.
    def sing(self, sounds):
        return f'Chartreux {self.name} says {sounds}'


# Step 1: Create the Siamese Class (Inherits from Cat)

class Siamese(Cat):

    # Overriding the parent's walk() method to show Polymorphism
    def walk(self):
        return f'Siamese {self.name} (Age: {self.age}) is sprinting and looking regal!'


# Step 2: Create a List of Cat Instances

print("Instantiating individual cats...")

bengal_obj = Bengal(name="Mochi", age=3)
chartreux_obj = Chartreux(name="Smokey", age=7)
siamese_obj = Siamese(name="Princess", age=2) # Using the new Siamese class

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

print(f"Created a list containing {len(all_cats)} cats.")


# Step 3: Create a Pets Instance

sara_pets = Pets(all_cats)
print(f"Created a Pets instance for Sara, managing the cat collection.")


# Step 4: Take Cats for a Walk (Demonstrates Polymorphism)

sara_pets.walk()
print("exercise 4 : family and person classes".capitalize())
# Step 1: Create the Person Class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""   # starts empty as required

    def is_18(self):
        return self.age >= 18


# Step 2: Create the Family Class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  # list of Person objects

    def born(self, first_name, age):
        # Create a new Person
        new_person = Person(first_name, age)
        # Assign family last name
        new_person.last_name = self.last_name
        # Add to members list
        self.members.append(new_person)

    def check_majority(self, first_name):
        # Search for the person by first name
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"{person.first_name}, You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print(f" Sorry  {person.first_name}, you are not allowed to go out with your friends.")
                return
        
        print("Person not found in the family.")

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for person in self.members:
            print(f"- {person.first_name}, {person.age} years old")
# Step 3: Test the Classes
fam = Family("Smith")

fam.born("Alice", 17)
fam.born("Bob", 20)

fam.family_presentation()

fam.check_majority("Bob")
fam.check_majority("Alice")

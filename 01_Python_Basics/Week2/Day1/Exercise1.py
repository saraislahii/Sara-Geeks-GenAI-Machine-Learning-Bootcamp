print("Exercise 1 :Cats")

##   Class Definition

class Cat:
  def __init__(self, cat_name, cat_age):
    self.name = cat_name
    self.age = cat_age

  def __str__(self):
    
    return f"Cat(Name: {self.name}, Age: {self.age})"



## 🐾 Step 1: Create Cat Objects


cat1 = Cat("Whiskers", 5)
cat2 = Cat("Mittens", 12)
cat3 = Cat("Shadow", 7)

print("Created Cats:")
print(f"Cat 1: {cat1}")
print(f"Cat 2: {cat2}")
print(f"Cat 3: {cat3}")



## 🧐 Step 2: Create a Function to Find the Oldest Cat

def find_oldest_cat(c1, c2, c3):
   
    # Start by assuming the first cat is the oldest
    oldest = c1
    
    # Compare against the second cat
    if c2.age > oldest.age:
        oldest = c2
        
    # Compare against the third cat
    if c3.age > oldest.age:
        oldest = c3
        
    return oldest

##  Step 3: Print the Oldest Cat’s 
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Print the required formatted string

print(f"The oldest cat is : {oldest_cat.name}, and is :{oldest_cat.age} years old.")
print("exercise1: favorite numbers".title())

# 1. Create a set called my_fav_numbers

my_fav_numbers = {5, -6, 90, -2, 2} 

print("Initial Set:", my_fav_numbers)

# 2. Add two new numbers to the set
my_fav_numbers.add(-42)
my_fav_numbers.add(17)

print("After adding two numbers:", my_fav_numbers)

# 3. Remove the last number i added to the set 
my_fav_numbers.remove(17)

print("After removing the last number i added :", my_fav_numbers)

# 4. Create another set called friend_fav_numbers and populate it 
friend_fav_numbers = {1, -42, 3, 4, 90}

print("Friend's Set:", friend_fav_numbers)

# 5. Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("Combined Set :", our_fav_numbers)
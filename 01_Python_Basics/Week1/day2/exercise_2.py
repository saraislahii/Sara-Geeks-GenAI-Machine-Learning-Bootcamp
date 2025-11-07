print("exercise2: tuple".title())


# Given tuple of integers
tuple_of_int = (10, 20, 30)

print(f"Tuple of integers: {tuple_of_int}")

# Instructions: try to add more integers to the tuple.
try:
    # Attempt 1: Trying to use a List method like append()
    tuple_of_int.append(40)
except AttributeError as e:
    print(f"Attempt 1 Failed: {e}")

try:
    # Attempt 2: Trying to change an element by index
    tuple_of_int[0] = 5
except TypeError as e:
    print(f"Attempt 2 Failed: {e}")



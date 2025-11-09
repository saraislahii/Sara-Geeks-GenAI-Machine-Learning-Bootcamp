print("exercise 4:Random")
import random

def compare_numbers(number):
    
    random_number = random.randint(1, 100)

    print(f"The number you entered is: {number}")
    print(f"The random number generated is: {random_number}")

    if number == random_number:
      print("Success! The numbers are the same.")
    else:
      print("Fail! The numbers are different.")


compare_numbers(30)



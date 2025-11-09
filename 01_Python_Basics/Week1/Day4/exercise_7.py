print("exercise 7: Temperature Advice")
import random

# Step 1: Create the get_random_temp() Function
def get_random_temp():
    return random.randint(-10, 40)

# the main() Function 
def main():
    
    # Get the random temperature
    temperature = get_random_temp()

    # Print the temperature
    print(f"The temperature right now is {temperature} degrees Celsius.")

    # Provide Temperature-Based Advice
    if temperature < 0:
        # Below 0°C
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 10:
        # 0°C to 9°C
        print("It's quite cold. A warm jacket would be a good idea.")
    elif temperature < 20:
        # 10°C to 19°C
        print("It's mild out. You might need a light coat or sweater.")
    elif temperature < 30:
        # 20°C to 29°C
        print("The weather is nice! Enjoy the warmth.")
    else:
        # 30°C and above
        print("It's hot! Stay hydrated and seek shade.")

# Call the main function 
main()


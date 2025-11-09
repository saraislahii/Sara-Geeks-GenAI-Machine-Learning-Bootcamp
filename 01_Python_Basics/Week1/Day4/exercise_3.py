
print("exercise 3: Some Geography ")
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Call 1: With both city and country
describe_city("Reykjavik", "Iceland")

# Call 2: With only the city 
describe_city("Paris")

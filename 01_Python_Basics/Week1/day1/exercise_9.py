print("exercise 9: tall enough to wride a roller coaster ".title())
#step 1 ask for thr hight 

try:
  height= int(input("what is your height in centimeters"))
  # feedback
  if height>=145 :
    print("You are tall enough to wride")
  else:
    print("You need to grow some more to wride")
except ValueError:
  print(" Invalid input! Please enter ONLY a whole number (e.g., 150) for your height.")

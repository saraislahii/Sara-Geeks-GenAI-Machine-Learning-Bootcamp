print("exercise 7: odd or even ".title())
# step2:ask the user for a number 
try: 
    a=int(input("enter a number "))

  # step 2: determin wheither its odd or even 
    if a%2==0 :
      print(f"{a} is even")
    else :
      print(f"{a} is  odd")
except ValueError:
  print(" Invalid input! Please enter ONLY a whole number ")

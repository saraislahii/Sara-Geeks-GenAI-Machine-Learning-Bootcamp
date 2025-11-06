
print("exercise 3: what is the output ".title())
print("1: ",bool(3 > 5))#false
print("2: ",bool(3==3))#true
print("3: ",bool(3=="3"))#false
try:
    
    print("4: ", "3" > 3 ) 
    
except TypeError as _:

    print("4: ERROR DETECTED and SKIPPED.| Reason:",_)

# The code continues running normally here 
print("5: ",bool("Hello"=="hello"))#false


#Observation: A Python script stops running instantly at the very first line that produces a fatal error (like a TypeError or SyntaxError). No code below the crashing line will execute.

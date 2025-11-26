from OOP.Week2.Day2.Exercise2 import Dog
import random
print("Exercise 3 : dog domisticated ")
class PetDog(Dog):
    def __init__(self, name, age, weight): 
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        
        print(self.bark())#returns the output of bark method in the dog class 
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]
        
        for dog in args:
            
            dog_names.append(dog.name)
            
        
        names_str = ", ".join(dog_names)
        
        print(f"{names_str} all play together!")

    def do_a_trick(self): 
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()



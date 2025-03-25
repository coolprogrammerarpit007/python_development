# class Dog:
#     species = "Canis familiaris"

#     def __init__(self,name,age,breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def __str__(self):
#         return f"{self.name} is {self.age} year\'s old."
    
#     def speak(self,sound):
#         return f"{self.name} says {sound}"
    

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))
# print(jack.speak("Woof"))


# Passing a string to every call to .speak() is repetitive and inconvenient. Moreover, the .breed attribute should determine the string representing the sound that each Dog instance makes, but here you have to manually pass the correct string to .speak() every time you call it.

# You can simplify the experience of working with the Dog class by creating a child class for each breed of dog. This allows you to extend the functionality that each child class inherits, including specifying a default argument for .speak().

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} barks {sound}"
    

# class JackRussellTerrier(Dog):
#     # To override a method in a child class
#     def speak(self,sound="Yap"):
#         return super().speak(sound)

# class Dachshund(Dog):
#     pass

# class BullDog(Dog):
#     pass

# miles = JackRussellTerrier("Miles",4)
# buddy = Dachshund("Buddy",6)
# jack = BullDog("Jack",7)
# jim = BullDog("Jim",8)

# print(miles.speak())

# Challange

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self,sound = "Bark"):
        return super().speak(sound)



entertainment = GoldenRetriever("Entertaintment",10)
# print(entertainment)

print(entertainment.speak("BO BO"))


# To override a method from the 
# parent class
# , you can redefine it in the 
# child class
# . If you want to use the original method as well, then you can call the method of the 
# parent class
#  using the super() function.


#  you can check if an object is an instance of a specific class in Python using isinstance() method.






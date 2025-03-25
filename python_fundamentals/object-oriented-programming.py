# Object Oriented Programming In Python

class Dog:
    species = "Canis familiaris"  # Class Attributes
    def __init__(self,name,age):
            # Instance Attributes
        self.name = name
        self.age = age


    # Instance Methods

    def description(self):
        return f"{self.name} is {self.age} year\'s old."
    
    def sound(self,sound):
        return f"{self.name} makes {sound} sound."
    
    def __str__(self):
        return f"{self.name} is {self.age} year's old!"

miles = Dog("Miles",4)   # Instance of class / Objects
buddy = Dog("buddy",6)

# print(miles.species)


# miles.species = "German Shephard"
# print(miles.species) # Output: German Shephard
# print(buddy.species) # Output: Canis familiaris

# print(miles.description())
# print(miles.sound("bo bo bo"))
# print(miles)


# Careate a Car Class

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        print(f"The {self.color} car has {self.mileage} miles.")


car1 = Car("blue","20,000")
car2 = Car("red","30,000")

# car1.description()
# car2.description()


# Inheritance

# Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that you derive child classes from are called parent classes.

# You inherit from a parent class by creating a new class and putting the name of the parent class into parentheses:

class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"  # overridden the property 
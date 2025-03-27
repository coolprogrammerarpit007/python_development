# @property :- Decorator used to define a method as property (it can be acessed like an attribute)
#              Benafit :- Add additional logic when read,write and delete attributes.
# Gives you getter,setter and deletor method.

class Rectangle:
    def __init__(self,width,height):
        self._width = width  # Telling other developers that these properties are protected.
        self._height = height


    @property   # used to get the attribute 
    def width(self):
        return f"{self._width:.1f} cm "

    @property
    def height(self):
        return f"{self._height:.1f} cm "
    
    # setting the attribute of the object.

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width

        else:
            print(" Must be greater than ZERO.")

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print(" Must be greater than ZERO.")


# to delete a property
    @width.deleter
    def width(self):
        del self._width
        print("width has been deleated!")


rectangle = Rectangle(25,12)

# print(rectangle.width)
# print(rectangle.height)

# rectangle.width = 50
# print(rectangle.width)
# rectangle.height = -500
# del rectangle.width


#decorators in python

# Decorator:- A function that extends the behaviour of the another function w/o modifying the base function we pass the base function as argument to the decorator.

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("Sprinkles added to your Icecream.")
        func(*args,**kwargs)

    return wrapper

def add_chocolate(func):
    def wrapper(*args,**kwargs):
        print("Chocolate added to your Icecream.")
        func(*args,**kwargs)

    return wrapper

@add_sprinkles
@add_chocolate
def get_my_ice_cream(flavour):
    print(f"Here is your's {flavour} flovoured Ice cream.")

# get_my_ice_cream("Chocolate")


# Exception Handling In Python

# .try , except and finally

try:
    pass
except:
    pass
finally:
    pass


# try:
#     number = int(input("Enter number"))
#     print(number + " is a number")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Invalid input")
# finally:
#     print("DO some cleanup here!")


# File Detection In Python
import os

file_path = "test.txt"
if os.path.exists(file_path):
    print("FILE EXISTS")
else:
    print("NOT EXIST!")



# os.path.isfile() -> to check if the given path is file or not.
# os.path.isdir() -> to check whether path is directory or not.


txt_data = "I like pizza."
# fhand = open("example.txt","wb")
# fhand.write(txt_data.encode())
# fhand.close()

file_path = "output.txt"
with open(file_path,"w") as file:
    file.write(txt_data)
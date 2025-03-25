# Dictionary Comprehensions

likes = {
    "color":"Blue",
    "fruit":"apple",
    "pet":"Dog"
}

# Dictionary Comprehension Syntax

# {key: value for member in iterable [if condition]}

power_of_two = {integer:2 ** integer for integer in range(1,10)}
# print(power_of_two)

fruits = ["apple", "banana", "cherry"]

upper_dict = {fruit.upper():len(fruit) for fruit in fruits}


# web-scrapping in python


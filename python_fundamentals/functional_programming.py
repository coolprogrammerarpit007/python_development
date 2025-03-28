from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def square(num):
    return num * 2

# squared_numbers = list(map(square,numbers))
squared_numbers = list(map(lambda num:num * 2,numbers))
# print(squared_numbers)

even_numbers = list(filter(lambda num:num % 2 == 0,numbers))
# print(even_numbers)


total = reduce(lambda x,y:x+y,numbers)
# print(total)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = dict(zip(a, b))
# print(x)
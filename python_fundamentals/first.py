import sys
# print("Python For Everybody!")

# Celcius to Farhenite Temperature Converter.

# degree_celcius = float(input("Enter Temperature in Celcius: "))
# degree_farhenite = degree_celcius * (9/5) + 32

# print(f"Temperature From degree celcius: {degree_celcius} to degree farhenite is: {degree_farhenite}")


# score = float(input("Enter Score: "))

# if(score < 0.0 or score > 1.0):
#     print("score is out of range")
    
# elif(score >= 0.9 and score < 1.0):
#     print("A")
    
# elif(score >= 0.8 and score < 0.9):
#     print("B")
    
# elif(score >= 0.7 and score < 0.8):
#     print("C")

# elif(score >= 0.6 and score < 0.7):
#     print("D")

# else:
#     print("F")




# Work Pay Calculator 

# hrs = input("Enter working hours: ")
# rate = input("Enter rate: ")

# try:
#     hrs = float(hrs)
#     rate = float(rate)
#     overtime = 0
#     pay = 0
#     if hrs > 40:
#         overtime = hrs - 40
#         pay = ((hrs - overtime) * rate) + (overtime * 1.5 * rate)

#     else:
#         pay = hrs * rate

#     print(f"Pay: {pay}")


# except:
#     print("Error,please enter numeric input")


# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()


# repeat_lyrics()

largest = None
smallest = None
while True:
    num = input("Enter number: ")
    if(num == 'done'):
        break
    
    try:
        num = float(num)
        if(largest is None or num > largest):
            largest = num
        if(smallest is None or smallest > num):
            smallest = num
    except:
        print("Invalid input")
        continue
        

print("Maximum", largest)
print("Minimum",smallest)
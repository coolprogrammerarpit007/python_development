# Open a fil, extract numbers from text and find average of it.
# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
import sys
# file_name = input("Enter the file name: ")
# fh = open(file_name)
# sum = 0
# avg = 0
# count = 0

# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     index = line.find(" ")
#     num = float(line[index+1:])
#     sum += num
#     count += 1

# avg = sum/count
# print(f"Average spam confidence: {avg}")

# Data-Structures in python

# Lists in python

# a = 'apple'
# b = 'apple'

# b = 'banana'
# result = a is b
# print(result)
# print(a)
# print(b)


# when a list is passed as argument to the function, function gets refrence of the list so if it modifies the list the original sender also get changes.

# def update_list(num):
#     num.append(5)
#     return num


# numbers = [1,2,3,4]
# new_numbers_list = update_list(numbers)
# print(numbers)
# print(new_numbers_list)

# file_name = input("Enter file name: ")
# fhand = open(file_name)

# unique_words = []

# for line in fhand:
#     line = line.rstrip()
#     words = line.split()
#     for word in words:
#         if word in unique_words:
#             continue
#         unique_words.append(word)

# unique_words.sort()
# print(unique_words)


# file_name = input("Enter the file: ")
# fhand = open(file_name)
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith("From "):
#         continue
#     words = line.split()
#     count += 1
#     print(words[1])


    
# print(f"There were {count} lines in the file with From as the first word")


# Dictionaries 


# The reason why the output string does not contain the character 'g' is due to how str.maketrans() handles the deletestr parameter. Let's break down the process step by step:

# Translation Table Creation:

# fromstr = "abc"

# tostr = "ghi"

# deletestr = "b"

# When creating the translation table, Python maps each character in fromstr to the corresponding character in tostr. However, any character in deletestr is marked for deletion.

# Character Mapping:

# a → g

# b → delete (because b is in deletestr)

# c → i

# Translation Process:

# Original string: "abcdef"

# Translate:

# a → g

# b → delete

# c → i

# d, e, f remain unchanged because they are not in the translation table.

# Result:

# After translating, the string becomes "gidef".

# However, in your example, the output is shown as "idef", which seems incorrect based on the translation rules. The correct output should indeed include the 'g' because 'a' is mapped to 'g'.

# So, the correct sequence should be:

# a → g

# b → delete

# c → i

# Result: "gidef"

# If you are seeing "idef" instead, there might be a misunderstanding or an error in the code execution. The correct Python code should produce "gidef":


# Define the strings for translation
# fromstr = "abc"
# tostr = "ghi"
# deletestr = "b"

# # Create a translation table
# translation_table = str.maketrans(fromstr, tostr, deletestr)

# # Original string
# string = "abcdef"

# # Translate the string
# result = string.translate(translation_table)
# print(result)  # Correct Output: gidef



# count who has send the most mails

# file_name = input("Enter File Name: ")
# f_hand = open(file_name)
# max_key = None
# max_value = None

# mail_dict = dict()

# for line in f_hand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     mail_sender = words[1]
#     mail_dict[mail_sender] = mail_dict.get(mail_sender,0) + 1

# # print(mail_dict.items())

# for key,value in mail_dict.items():
#     if max_value is None or value > max_value:
#         max_key = key
#         max_value = value
#         print(f"Maximum Key: {max_key} And Maximum Value: {max_value}")


# Data Type: Tuples

# str_list = ['abc','def','ghi','jkl']
# t1 = tuple(str_list)
# print(t1)

# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)
# # print(t)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)
# Swap Two Variables using the tuple
a = 5
b = 10

# print(a)
# print(b)
# a,b = b,a
# print(a)
# print(b)

# Dictonaries have a method called items(), which converts dict into list of tuples.
# Using tuples as keys in dictionaries

# Because tuples are hashable and lists are not, if we want to create a composite key to use in a dictionary we must use a tuple as the key.
# directory[last,first] = numbers

# for last, first in directory:
#     print(first, last, directory[last,first])


# List comprehension
# Sometimes you want to create a sequence by using data from another sequence. You can achieve this by writing a for loop and appending one item at a time. For example, if you wanted to convert a list of strings – each string storing digits – into numbers that you can sum up, you would write:

# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = []
# for x in list_of_ints_in_strings:
#     list_of_ints.append(int(x))

# print(sum(list_of_ints))
# With list comprehension, the above code can be written in a more compact manner:

# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = [ int(x) for x in list_of_ints_in_strings ]
# print(sum(list_of_ints))


# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# file_name = input("Enter File: ")
# f_hand = open(file_name)
# time = []
# hours_count = dict()

# for line in f_hand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()[5]
#     time.append(words)


# # print(time)
# for clock_hr in time:
#     index = clock_hr.index(":")
#     # print(index)
#     hrs = clock_hr[0:index]
#     # print(hrs)
#     hours_count[hrs] = hours_count.get(hrs,0) + 1


# sorted_hrs_dict = list(hours_count.items())
# sorted_hrs_dict.sort()
# # print(sorted_hrs_dict)

# for hrs,count in sorted_hrs_dict:
#     print(hrs,count)


x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(type(y))
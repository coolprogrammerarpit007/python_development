# Regular Expressions

# Regular Expression Characters

# ^ Matches the beginning of the line.

# $ Matches the end of the line.

# . Matches any character (a wildcard).

# \s Matches a whitespace character.

# \S Matches a non-whitespace character (opposite of \s).

# * Applies to the immediately preceding character(s) and indicates to match zero or more times.

# *? Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.

# + Applies to the immediately preceding character(s) and indicates to match one or more times.

# +? Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.

# ? Applies to the immediately preceding character(s) and indicates to match zero or one time.

# ?? Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.

# [aeiou] Matches a single character as long as that character is in the specified set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.

# [a-z0-9] You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.

# [^A-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.

# ( ) When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().

# \b Matches the empty string, but only at the start or end of a word.

# \B Matches the empty string, but not at the start or end of a word.

# \d Matches any decimal digit; equivalent to the set [0-9].

# \D Matches any non-digit character; equivalent to the set [^0-9].

# search() -> to find the string which matches the pattern.'
# findall() -> to extract the matched pattern.

# using regular expressions to extract numbers from file and find the total of it.

import re
# import sys
# numbers = []
# total = 0
# file_name = input("Enter File Name: ")
# f_hand = open(file_name)
# for line in f_hand:
#     line = line.rstrip()
#     number = re.findall('[0-9]+',line)
#     if len(number) > 0:
#         numbers.append(number)



# for num in numbers:
#     for n in num:
#         total += int(n)

# print(f"Total: {total}")

# str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


# pattern_string = re.findall("[A-Za-z0-9]+",str)
# print(pattern_string)

# regex_pattern = input("Enter a regular expression: ")
# file_name = input("Enter File Name: ")
# f_hand = open(file_name)
# count = 0

# for line in f_hand:
#     line = line.rstrip()
#     match_pattern = re.findall("^Author",line)

#     if len(match_pattern) > 0:
#         count += 1

# # print(f"There are {count} lines that matched {regex_pattern}")
# print(f"There are {count} lines that are matched")
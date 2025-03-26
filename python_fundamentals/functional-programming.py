# Normal Function

def identity(x):
    return x

# lambda Functions

lambda x : x # Syxtax for the lambda functions

# (lambda x: x + 1)(2)

add_one = lambda x:x+1
# print(add_one(9))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')
# 'Full name: Guido Van Rossum'

add = lambda x,y:x+y
print(add(5,7)) # 12
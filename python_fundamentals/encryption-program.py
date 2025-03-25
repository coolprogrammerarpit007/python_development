# Encryption Program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars: {chars}")
# print(f"key: {key}")

# Encryption Of Message

def encrypt(msg):
    encrypted_msg = ""

    for letter in msg:
        index = chars.index(letter)
        encrypted_msg += key[index]

    return encrypted_msg


# Decryption

def decrypt_msg(message):
    decrypted_msg = ""

    for letter in message:
        index = key.index(letter)
        decrypted_msg += chars[index]


    return decrypted_msg


message = input("Enter your message which need to be encrypted!")
encrypted_message = encrypt(message)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

message_to_be_decrypted = input("Enter Message to be decrypted: ")
if len(message_to_be_decrypted) > 1:
    decrypted_message = decrypt_msg(message_to_be_decrypted)
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")






# In Python, variables that are defined outside of a function are considered global variables. These variables are accessible from within any function, but they can only be read, not modified, unless explicitly declared as global using the global keyword.

# In your code, chars and key are global variables because they are defined outside of any function. The functions encrypt and decrypt_msg can access these variables without needing the global keyword because they are only reading from them, not modifying them.

# Here's why this works:

# Reading Global Variables: When a function reads a global variable, Python looks for the variable in the local scope first. If it doesn't find it there, it then looks in the global scope. Since chars and key are not defined locally within the functions, Python finds them in the global scope and uses them.

# Modifying Global Variables: If you were to modify chars or key within a function (e.g., by assigning a new value to them), Python would treat them as local variables unless you explicitly declare them as global using the global keyword. This is because Python assumes that any variable assigned a value within a function is local unless told otherwise.
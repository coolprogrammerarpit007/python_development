# print('Chai aur Python')

# def chai(num):
#     print(num)
   

# chai(10)
# chai(20)

# Data Types In Python

# 1. Number
# 2. String
# 3. Boolean
# 4. List -> [1,2,3]
# 5. Tuple -> (1,2,3)
# 6. Dictionaries = {'key1':1,'key'2:2,'key3':3}
#7. Sets -> only stores unique values -> {'a','b','c'}
# 8. File -> open('file.txt')
# 9. None : None
# 10. Functions
# 11. Modules
# 12. Classes
# 13. Advance Types -> Generators,Decorators,Iterators,Comprehensions,MetaProgramming

import subprocess
import platform
import sys
import ctypes

def run_command(command):
    """Run a system command and return the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

# Detect the operating system
os_name = platform.system()

if os_name == "Windows":
    # Command for Windows
    command = ["netsh", "wlan", "show", "networks"]
elif os_name == "Linux":
    # Command for Linux
    command = ["nmcli", "device", "wifi", "list"]
else:
    print("Unsupported OS")
    exit()

# Check if running on Windows and if we need admin privileges
if os_name == "Windows":
    # Check if the script is running with admin privileges
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("This script requires administrative privileges. Please run as an administrator.")
        sys.exit(1)

# Execute the command and capture the output
output = run_command(command)
if output:
    print(output)

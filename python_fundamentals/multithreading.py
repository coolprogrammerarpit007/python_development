# Multithreading :- Used to perform multiple tasks concurrently (multitasking)
# Multithreading is used to improve the performance of a program by executing multiple threads or flows of execution
# Good for I/O bound tasks like reading files or fetching data from APIs 
# threading.thread(target=my_function)


import threading
import time


def walk_dog(name):
    time.sleep(10)
    print(f"Walking my dog {name} to the park.....")

def throw_trash():
    time.sleep(5)
    print("Throwing the trash!")


def get_mail():
    time.sleep(3)
    print("Get your mail")



#  this code will be executed in the main threads
# walk_dog()
# throw_trash()
# get_mail()


# to run these multiple tasks simultaneously , need to be created multiple tasks.

thread1 = threading.Thread(target=walk_dog,args=("Ricky Ponting",))
thread1.start()

thread2 = threading.Thread(target=throw_trash)
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()

thread1.join()
thread2.join()
thread3.join()   # After all these join methods are completed then the print statment -> All chores are completed got printed!
print("All chores are completed!")
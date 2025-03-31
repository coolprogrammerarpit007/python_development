# Genious Python Features.


# context managers.

# with open("context.txt","w") as file:
#     file.write("Hello, world!")



# Generators In Python

# Python generators are a powerful feature that allow lazy iteration through a sequence of values.

# They produce items one at a time and only when needed, which makes them the best choice for working with large datasets or streams of data where it would be inefficient and impractical to load everything into memory at once.


# def simple_generator(num):
#     i = 0
#     while i < num:
#         yield i
#         i += 1


# gen = simple_generator(25)
# for num in gen:
#     print(num)


# The advantages of generators

# 1. Memory Optimization.
# 2. Enhanced Performance.


# Asynchronous Programming

# Asynchronous programming techniques allow your programs to take advantage of relatively slow IO processes by freeing the CPU to do other work.


import asyncio

async def asynchtonous_function():
    print("This will run after 5 seconds.")
    await asyncio.sleep(5)


# asyncio.run(asynchtonous_function())


# async def your_coronotous(time_delay):
#     print(f"This function will run after {time_delay} seconds at the most.")
#     await asyncio.sleep(time_delay)
#     print(f"this function runed after the {time_delay} seconds.")


# async def main():
#     await asyncio.gather(*[your_coronotous(_) for _ in range(5)])


# asyncio.run(main())


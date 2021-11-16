"""
Python Crash Course.
"""

# In Python order matters; function definition goes before the actual call.


# We use snake_case for names and variables. Also, we can specify the expected type of the parameter and the return with this notation.
def days_to_seconds(given_days: int) -> int:
    # Every function requires a docstring.
    """
    Returns the number of seconds for the amount of days given.
    """
    return given_days*24*60*60


days = int(input("Specify the amount of days to convert to seconds:"))
print(f"{days} days are {days_to_seconds(days)} seconds.")

counter = int(input("Specify the amount of iterations:"))
while counter > 0:  # Java: while (counter-- > 0) { ... }
    print(f"{counter} iteration(s) left")
    # In Python there's no '--' or '++' operator, so we use '-=' or '+=' instead.
    counter -= 1

# Ternary operator example in Python: <true> if <condition> else <false> -> Java: <condition> ? <true> : <false>
for i in range(int(input("Specify the amount of iterations:")), 0, -1):  # range(start, end, step)
    print(f"{i} iteration(s) left (even)" if i %
          2 == 0 else f"{i} iteration(s) left (uneven)")

# Normal if example plus try, except & finally blocks:
try:
    for i in range(int(input("Specify the amount of iterations:")), 0, -1):
        if i % 2 == 0:
            print(f"{i} iteration(s) left (even)")
        else:
            print(f"{i} iteration(s) left (uneven)")
except ValueError:
    print("Invalid input.")
# finally:
    # print("Finally block executed.") -> finally block gets executed regardless of the try block's outcome. We can also use it as a callback function if what we executed in the try block was meant to be a bucle.

numbers = []
user_input = ""
while user_input != "0":
    user_input = input(
        "Type the number you want to add or 0 to finish adding:\n")
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Invalid value.")
numbers.remove(0)
numbers.sort()
print(numbers)

numbers.clear()
user_input = input("Type the numbers you want to add sepatared by commas:\n")
for each_number in user_input.split(","):
    try:
        numbers.append(int(each_number))
    except ValueError:
        print("Invalid value.")
numbers.sort()
print(numbers)

repeated_numbers = [1, 1, 2, 2, 3, 4, 5]
print(set(repeated_numbers))
# set() is a built-in function that returns a set with the unique elements of the list.
for each_unique_element in set(repeated_numbers):
    print(each_unique_element)

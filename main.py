"""
Python Crash Course.
"""

# In Python order matters; function definition goes before the actual call.


# We use snake_case for names and variables. Also, we can specify the expected type of the parameter and the return with this notation.
def days_to_seconds(days: int) -> int:
    # Every function requires a docstring.
    """
    Returns the number of seconds for the amount of days given.
    """
    return days*24*60*60


days = int(input("Specify the amount of days to convert to seconds:"))
print(f"{days} days are {days_to_seconds(days)} seconds.")

counter = int(input("Specify the amount of iterations:"))
while counter > 0:  # Java: while (counter-- > 0) { ... }
    print(f"{counter} iteration(s) left")
    # In Python there's no '--' or '++' operator, so we use '-=' or '+=' instead.
    counter -= 1

# Ternary operator example in Python: <true> if <condition> else <false> -> Java: <condition> ? <true> : <false>
for i in range(int(input("Specify the amount of iterations:")), 0, -1):  # range(start, end, step)
    print(f"{i} iteration(s) left (even)") if i % 2 == 0 else print(
        f"{i} iteration(s) left (uneven)")

# Normal if example
for i in range(int(input("Specify the amount of iterations:")), 0, -1):
    if i % 2 == 0:
        print(f"{i} iteration(s) left (even)")
    else:
        print(f"{i} iteration(s) left (uneven)")

"""
Python Crash Course.
"""

# We can import external modules and/or specific variables/functions from them, using the following notations:
# import <library> -> import <library> as <alias> -> from <library> import <function> -> from <library> import <function> as <alias>
# worst way to do it: from <library> import *

# We import 'error' from 'logging' module to use it in the 'except' block.
from logging import error
from functools import reduce
from requests import get
from father import Father
from child import Child


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
    error("Invalid input.")
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
        error("Invalid value.")
numbers.remove(0)
numbers.sort()
print(numbers)

numbers.clear()
user_input = input("Type the numbers you want to add sepatared by commas:\n")
for each_number in user_input.split(","):
    try:
        numbers.append(int(each_number))
    except ValueError:
        error("Invalid value.")
numbers.sort()
print(numbers)

repeated_numbers = [1, 1, 2, 2, 3, 4, 5]
print(set(repeated_numbers))
# set() is a built-in function that returns a set with the unique elements of the list.
for each_unique_element in set(repeated_numbers):
    print(each_unique_element)

# We can set the key-value pairs in the definition of the dictionary.
my_dictionary = {"key1": "value1"}
# We can add new key-value pairs if we specify new key and asign a value.
my_dictionary["key2"] = "value2"
# We can also use the built-in function 'update' to add new key-value pairs, update existing ones or add another dictionary to the current one.
my_dictionary.update({"key3": "value3"})
my_second_dictionary = {"key4": "value4"}
my_dictionary.update(my_second_dictionary)
print(my_dictionary)

# 'items' returns key-value tuples. We can access each index of the tuple with the 'each_item[0]' and 'each_item[1]' notation.
for each_item in my_dictionary.items():
    print(each_item, each_item[0], each_item[1])

# 'keys' returns only the keys. There's no need to specify 'keys' as it's the default behavior.
for each_key in my_dictionary:
    print(each_key)

for each_value in my_dictionary.values():  # 'values' returns only the values.
    print(each_value)


class User:
    """
    Python class example
    """

    # '__init__' is a constructor.
    def __init__(self, name: str, age: int):
        self._name = name  # '_' means protected (we use it as private).
        self._age = age  # '_' means protected (we use it as private).

    # There's no real private attributes in Python, but we can use the '__' notation to hide them. Although, they would still be accessible using _object._attribute notation.
    # The convention is to use single '_' as private attribute representation to point out that those attributes shouldn't be accessed directly and use property() or decorators to define access.

    # '__str__' returns a string representation of the object.
    def __str__(self):
        return f"User: {self._name} - {self._age} years old"

    @property
    def name(self):
        """
        _name getter
        """
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        """
        _age getter
        """
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    @age.deleter
    def age(self):
        del self._age


# To create an instance of User class, we use the 'User' class name and pass the arguments to the constructor.
my_user = User("Alex", 35)

# Python follows the Uniform Access Principle (UAP), so that we can access or modify the attributes of the class using the '.' notation directly instead of getters and setters syntax.
# That allows us to make the code more readable like:
my_user.age += 1
# Which equals to my_user.set_age(my_user.get_age() + 1) with traditional getters and setters.


# Python way to mimic Java streams: mapping, filtering and collecting all at once.
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = [
    each_number for each_number in random_list if each_number % 2 == 0]
print(filtered_list)

# We can also use 'reduce' same way we do in Java 8+. Since it's not a built-in function, we need to import it from 'functools'.
pair_sum = reduce(lambda a, b: a + b, filtered_list)
# We used lambda notation to define the behavior of 'reduce': for each pair of elements return its sum.
# Still missing, or haven't found yet, a way to mimic the option of functional interface as shortcut to specify the behavior instead of using lambda notation.
# reduce(sum::add, filtered_list) or something like that.
print(pair_sum)

# All of the above printed directly as a one liner:
print(reduce(lambda a, b: a + b,
      [each_number for each_number in random_list if each_number % 2 == 0]))

# The 'each_number' to the left of the 'for' acts as a placeholder in these examples, but we could've done other needed operations.

# Testing the access to GitHub API with 'requests' external library.
# pip install requests
my_repos = get("https://api.github.com/users/mezdelex/repos").json()

for repo in my_repos:
    print(f"{repo['name']} - {repo['description']}\n{repo['git_url']}\n")


Daniel = Father("Brown", "White")
Alex = Child("Brown", "White")
print(f"{Alex.eyes_color} & {Daniel.eyes_color}")

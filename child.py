"""
Child class module
"""
from father import Father


# We don't need any special keyword to inherit in Python, we just pass the class we want to inherit from as argument.
# In Python there's multiple inheritance, so we can inherit from multiple classes.
class Child(Father):
    """
    Child class
    """
    # We don't need to specify the __init__ constructor here, because it's already inherited from Father.
    # If we wanted to add specific attributes to the Child class constructor, we would need to user super().__init__(...) to call the Father's constructor
    # inside Child's constructor and set whatever we want to.

# To override a method, if there was any, we simply write the method we want to override in the child class.
# Python doesn't require any special @override decorator that specifies that the method is being overriden.
# To allow method chaining, just return self at the end of the method.

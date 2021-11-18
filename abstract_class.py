"""
Abstract class example
"""

from abc import ABC, abstractmethod

# In Python there's no dedicated 'Interface', so basically we inherit from ABC (Abstract Base Class) and use at least ONE @abstractmethod decorator
# to prevent the class from being instantiated. The ABC inheritance by itself is not enough to prevent the class from being instantiated without decorator.
# Classes naming convention in Python is PascalCase.


class MyAbstractClass(ABC):
    """
    My abstract class
    """
    @abstractmethod
    def my_abstract_method(self):
        """
        The required abstract method that needs to be implemented in the child class.
        """
        # We don't need to specify 'pass' here, because the docstring acts as a placeholder. If there's no docstring, which is not going to happen
        # if we follow 'pylint' rules anyway, we would've used 'pass' as a placeholder.

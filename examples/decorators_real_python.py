"""
Real Python: Python's instance, class, and static methods demystified
---------------------------------------------------------------------
https://realpython.com/instance-class-and-static-methods-demystified/
I was asked about decorators in a job interview. This tutorial was helpful.
"""
import math


class MyClass:
    def method(self):
        """Class instance method
        ---
        - Class instance methods accept `self` as an argument.
        - Can access the class itself (the original class object definition).
        """
        return "instance method called", self

    @classmethod
    def class_method(cls):
        """Class method
        ---
        - `@classmethod` accepts `cls`, but not `self`.
        - Can modify class state (applies to other instances of the class)
        - Cannot modify object/instance state (the original class object definition).
        """
        return "class method called", cls

    @staticmethod
    def static_method():
        """Static method
        ---
        - `@staticmethod` can't accept `self` or `cls`, but can accept other arguments.
        - Can't modify either class or instance state.
        - Mostly useful for namespacing methods (defining methods within a class)
        - If you don't use `self` or `cls` in the method, it can be a static method.
        """
        return "static method called"


class Pizza:
    def __init__(self, ingredients, radius):
        self.ingredients = list(ingredients)
        self.radius = radius

    def __repr__(self):
        return f"Pizza({self.radius}, {self.ingredients!r})"

    @property
    def area(self):
        """Calculate the area of the pizza.
        ---
        A medium pizza is 12" in diameter.
        """
        return self.circle_area(self.radius)

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"], 6)

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"], 6)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


def fun_with_methods():
    """Fun with class methods
    ---
    These commands are based on the Real Python REPL examples.
    """
    obj = MyClass()
    print(MyClass.method(obj))
    print(obj.class_method())
    print(obj.static_method())
    print(Pizza.prosciutto().area)
    print(Pizza.circle_area(6))


if __name__ == "__main__":
    fun_with_methods()

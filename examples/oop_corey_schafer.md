# Python OOP

[Corey Schafer Python Object-Oriented Programming tutorials YouTube playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

## Table of Contents <!-- omit in toc -->

- [Background](#background)
- [1 classes and instances](#1-classes-and-instances)
- [2 class variables](#2-class-variables)
- [3 classmethods and staticmethods](#3-classmethods-and-staticmethods)
  - [classmethods](#classmethods)
  - [staticmethods](#staticmethods)
- [4 inheritance](#4-inheritance)
- [5 special methods](#5-special-methods)
- [6 property decorators](#6-property-decorators)

## Background

- [Corey Schafer Python Programming Beginner Tutorials YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)

  - [Python Tutorial for Beginners 8: Functions](https://youtu.be/9Os0o3wzS_I)

    - 0.00.30: `pass`. Use `pass` to indicate that you will work on a function later. Python won't throw errors if a function is blank.
    - 0.04.30 `return`
    - 0.07.00 function arguments

      ```py
      def hello_func(greeting):
          return f"{greeting} Function."

      print(hello_func("Hi"))

      ```

    - 0.10.30 `args` and `kwargs`

- Other Corey Schafer Python tutorials
  - [Variable scope](https://youtu.be/QVdf0LgmICw)
  - [Decorators](https://www.youtube.com/watch?v=FsAPt_9Bf3U)

## 1 classes and instances

- _Why should we use classes?_ Classes are blueprints that group code for easy reuse.
- Instance variables contain data unique to each instance.
- Class methods always take the instance name as the first argument.
- Class names are typically in `PascalCase`. See [Python 3 tutorial - classes](https://docs.python.org/3/tutorial/classes.html).
- Instances can be named whatever you want, but it's best to use the conventional `self`.

```py
class Employee:
    """Class constructor for employee data."""

    def __init__(self, first, last, pay):
        """Sets employee attributes."""
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email.com"
        self.pay = pay

    def fullname(self):
        """Constructs employee full name."""
        return f"{self.first} {self.last}"


def class_example():
    """Instantiate the classes from the module with example information.
    ---
    """
    emp_1 = Employee("Corey", "Schafer", 50000)
    emp_2 = Employee("Test", "User", 60000)
    emps = [emp_1, emp_2]
    for emp in emps:
        print(f"Employee {emp.fullname()} email {emp.email}")


if __name__ == "__main__":
    class_example()

```

## 2 class variables

- Variables shared among all instances of a class.
- While instance variables can be unique for each class instance, class variables should be the same.
- With our employee example, a class variable might be a fixed raise amount given to all employees annually.
- **For scaling and efficiency, the employees could be stored as a list (array) instead of two objects.**
- I wanted to output the `raise_amount` as a percentage, like `4%`.
  - It took a little while to figure this out. The [PyFormat](https://pyformat.info/) site doesn't really explain how to format output strings as percentages. After figuring it out, I considered submitting a pull request to the [GitHub repo](https://github.com/ulope/pyformat.info), but they're in the middle of creating v2 with Lektor, so it's probably best to wait.
  - I used `{:.0%}` in the string formatting to indicate a percentage with zero decimal places.
  - I changed the raise from `1.04` to `0.04` so the percentage would output as `4%` instead of `104%`.
  - I then had to correct the raise calculation in `apply_raise(self)`. The previous `apply_raise(self)` function was only calculating the amount of the raise, not the new salary with the raise included.
  - The `pay` object also needed to be set as an integer. Otherwise, when the `from_string` classmethod was used, `pay` would be stored as a string, and `apply_raise(self)` would return an error.

## 3 classmethods and staticmethods

### classmethods

- In addition to class variables, class constructors can also include `classmethods`.
- Class methods are created by adding an `@` decorator to a class.
- Class methods take the class as implicit first argument, which can also be indicated with `cls` (not `class`, which is used to declare a class).
- Class methods can also be used as _alternative constructors_, meaning they offer other ways of creating objects. In this example, we use the `from_string` class method to parse employee info from a string.
- Corey pulls up the `datetime` module in _datetime.py_ to show examples of other class constructors.

### staticmethods

- Starts around 10.00 in the video.
- So far, we've seen that:
  - Classes pass the instance as the first argument, usually `self`.
  - `classmethods` pass the class as the first argument, `cls`.
- `staticmethods` don't pass anything automatically. They behave like regular functions. We include them in classes because they have some logical connection.

## 4 inheritance

- **Subclasses inherit methods and attributes from a parent class.** The parent class is passed in as an argument for the subclass.
- Python will walk through the chain of inheritance. This is called the **method resolution order.**
- Run `help()` on a class to see Python's information.
- If we want to create additional attributes in a subclass that are not present in the parent class, we can create an additional `__init__` method for the subclass.

  - There are two ways of doing this:
    - `super()`: Better convention, especially when using multiple inheritance.
    - Parent `__init__` method

  ```py
  class Developer(Employee):
      """Class constructor for developers that inherits the Employee class."""

      raise_amount = 0.10

      def __init__(self, first, last, pay, lang):
          """Sets employee attributes for the Developer subclass."""
          super().__init__(first, last, pay)
          # Alternative:
          # Employee.__init__(self, first, last, pay)
          self.lang = lang
          # Can I inherit and change a classmethod, like from_string?
  ```

- Corey also provides the example of a manager with employees.
- When passing a list as an argument, don't pass the list directly. **Never pass mutable data types as default arguments.** Here, `employees=None` is passed in, and the list is specified later.

  ```py
  class Manager(Employee):
      """Class constructor for managers that inherits the Employee class."""

      def __init__(self, first, last, pay, employees=None):
          """Sets employee attributes for the Manager subclass."""
          super().__init__(first, last, pay)
          if employees is None:
              self.employees = []
          else:
              self.employees = employees

      def add_emp(self, emp):
          """Adds an employee to the manager's employees list."""
          if emp not in self.employees:
              self.employees.append(emp)

      def remove_emp(self, emp):
          """Removes an employee from the manager's employees list."""
          if emp in self.employees:
              self.employees.remove(emp)

      def print_emps(self):
          """Prints the list of the manager's employees."""
          print("People managed by {}:".format(self.fullname()))
          for emp in self.employees:
              print("-> {}".format(emp.fullname()))
  ```

- 0.16.00 Python has two built-in functions: `isinstance()` and `issubclass()`.
- Example of inheritance: Werkzeug library _exceptions.py_ module.

## 5 special methods

- **Magic/dunder methods** help us implement built-in behavior and operator overloading.
- Special methods are surrounded by dunders (double underscores).
- The `__init__` method we have been using is one example.
- `__repr__`: Unambiguous representation (repr) of an object, used for debugging and logging.
- `__str__`: Readable representation of an object, displayed to end user.
- The integer addition that occurs with `print(1 + 2)` is using `__add__(1, 2)` under the hood.
- 0.11.00 Standard Library examples
- _datetime.py_

## 6 property decorators

- Property decorators allow us to define methods, but access them like attributes.
- Example from `class Employee`: Update email automatically when name is changed
- Getters
- Setters
- Deleters

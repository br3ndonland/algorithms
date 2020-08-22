"""
Corey Schafer Python OOP tutorials
----------------------------------

Corey Schafer Python Object-Oriented Programming tutorials YouTube playlist:
https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

Completed code
"""
import datetime
from typing import Optional


class Employee:
    """Baseclass constructor for employee data.
    ---
    """

    # Create class variables
    raise_amount = 0.04
    total_emps = 0

    def __init__(self, first: Optional[str], last: Optional[str], pay: int):
        """Sets employee attributes."""
        self.first = first
        self.last = last
        self.pay = int(pay)
        Employee.total_emps += 1

    def __repr__(self) -> str:
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self) -> str:
        return f"{self.fullname} - {self.email}"

    def apply_raise(self) -> int:
        """Calculates the new salary after a pay raise."""
        self.pay = int(self.pay * (1 + self.raise_amount))
        return self.pay

    @property
    def email(self) -> str:
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self) -> str:
        """Constructs employee full name."""
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name: str) -> str:
        first, last = name.split(" ")
        self.first = first
        self.last = last
        return f"Full name set to {name} with setter method."

    @fullname.deleter
    def fullname(self) -> str:
        old_name = self.fullname
        message = f"Delete name {old_name}!"
        self.first = None
        self.last = None
        message += " Deleted!"
        return message

    @classmethod
    def set_raise_amount(cls, amount: float) -> float:
        """Set the amount of the pay raise."""
        cls.raise_amount = amount
        return amount

    @classmethod
    def from_string(cls, emp_str: str):
        """Parse employee data out of a string."""
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def weekday(day: datetime.date) -> bool:
        """Determine if a given date is a weekday."""
        return day.weekday() != 5 and day.weekday() != 6


class Developer(Employee):
    """Class constructor for developers that inherits the Employee class."""

    raise_amount = 0.10

    def __init__(self, first: Optional[str], last: Optional[str], pay: int, lang: str):
        """Set employee attributes for the Developer subclass."""
        super().__init__(first, last, pay)
        self.lang = lang

    @classmethod
    def from_string(cls, emp_str: str):
        """Parse developer data out of a string."""
        first, last, pay, lang = emp_str.split("-")
        return cls(first, last, int(pay), lang)


class Manager(Employee):
    """Class constructor for managers that inherits the Employee class."""

    def __init__(
        self, first: Optional[str], last: Optional[str], pay: int, employees=None
    ):
        """Set employee attributes for the Manager subclass."""
        super().__init__(first, last, pay)
        self.employees = [] if employees is None else employees

    def add_emp(self, emp: Employee) -> None:
        """Add an employee to the manager's employees list."""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee) -> None:
        """Remove an employee from the manager's employees list."""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self) -> None:
        """Print the list of the manager's employees."""
        print(f"People managed by {self.fullname}:")
        for emp in self.employees:
            print(f"-> {emp.fullname}")


def class_example() -> None:
    """Instantiate the classes from the module with example information.
    ---
    """
    dev_1 = Developer("Corey", "Schafer", 50000, "Python")
    dev_1.fullname = "Corey SchaferSetter"
    dev_2 = Developer("Test", "User", 60000, "Java")
    dev_3 = Developer.from_string("Jane-Doe-90000-Scala")
    # dev_3 = Developer("Jane", "Doe", 90000, "Scala")
    devs = [dev_1, dev_2, dev_3]
    emp_1 = Employee("Employee", "One", 50000)
    emp_2 = Employee("Employee", "Two", 60000)
    emp_3 = Employee.from_string("John-Doe-70000")
    emps = [emp_1, emp_2, emp_3]
    mgr_1 = Manager("Sue", "Smith", 120000, [dev_1])
    # Print desired output
    print(f"Total people: {Employee.total_emps}")
    for dev in devs:
        print(f"Developer {dev.fullname} email: {dev.email}")
        print(f"Programming language of choice: {dev.lang}")
        print(
            f"Raise for {dev.fullname}: {dev.raise_amount:.0%}.",
            f"Salary: {dev.pay} -> {dev.apply_raise()}",
        )
    for emp in emps:
        emp.apply_raise()
        print(f"Employee {emp.fullname} email: {emp.email}")
        print(
            f"Raise for {emp.fullname}: {emp.raise_amount:.0%}.",
            f"Salary: {emp.pay} -> {emp.apply_raise()}",
        )
    mgr_1.add_emp(dev_2)
    mgr_1.print_emps()
    del emp_1.fullname
    print(f"New emp_1 name: {emp_1.fullname}")
    tut_date = datetime.date(2018, 11, 9)
    print(f"Did I do this tutorial on a weekday? {Employee.weekday(tut_date)}")
    # Print information on the developer class
    # print(help(Developer))


if __name__ == "__main__":
    class_example()

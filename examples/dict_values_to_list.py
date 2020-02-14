"""
Generate a list from dictionary values
--------------------------------------

This was a whiteboard question in a software engineering job interview.
I was asked to generate a list from the values in a dictionary.
"""
from typing import Dict, List

# Generate an example dict with a dict comprehension
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
example_dict: Dict[str, int] = {str(i): i for i in range(10)}

# Generate a list of ten integers with a list comprehension
list_of_ints: List[int] = [i for i in range(10)]

# Generate the same list from the values in the dict with a list comprehension
values_from_dict: List[int] = [val for key, val in example_dict.items()]
print(values_from_dict)

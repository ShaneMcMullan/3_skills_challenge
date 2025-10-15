# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(text):
    # Parmeters:
    #   text: a string containing the words to be read
    # Return:
    #   The estimated amount of time it would take to read the words provided
    #   E.g. "I found a new hat in the shop today, it wsa cheap so I bought it"
    pass

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
If we give it an empty sting
It will return no time needed to read
"""

reading_time("")
# -> "There is nothing to read!

"""
If we give it a string
It will return the time needed to read it
"""

reading_time("")
# -> "It will take ... minutes to read this"

"""
Given a None value
It throws an error
"""
reading_time(None) throws an error

"""
Given a non-string value
It throws an error
"""
reading_time(number), where number is an "int" datatype throws an error
reading_time(boolean), where boolean is an "bool" datatype throws an error

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.reading import reading_line

"""
If we give it an empty sting
It will return no time needed to read
"""

def test_read_empty_string():
    result = reading_time("")
    assert result == "There is nothing to read!"

Ensure all test function names are unique, otherwise pytest will ignore them!

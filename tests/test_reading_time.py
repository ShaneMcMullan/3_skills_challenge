from lib.reading import reading_time
import pytest

"""
If we give it an empty sting
It will return no time needed to read
"""

def test_read_empty_string():
    result = reading_time("")
    assert result == "There is nothing to read!"

"""
If we give it a string
It will return the time needed to read it
"""

def test_estimate_reading_time():
    string = "I want to know how long this will take to read"
    result = reading_time(string)
    time = (len(string.strip().split()) / 200)
    assert result == f"It will take {time} minutes to read this"

def test_type_error():
    string = 50
    with pytest.raises(Exception) as e:
        reading_time(string)
    error_message = str(e.value)
    assert error_message == "Invalid data type"
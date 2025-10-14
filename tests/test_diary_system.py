from lib.diary_system import make_snippet
import pytest

def test_first_five_words():
    result = make_snippet("Today I went to the park and had a walk.")
    assert result == "Today I went to the..."
    
def test_str_less_than_five_words():
    result = make_snippet("Today I went")
    assert result == "Today I went"

def test_not_string_argument():
    
    with pytest.raises(Exception) as e:
        result = make_snippet(55)
    error_message = str(e.value)
    assert error_message == "A string has not been entered."

from lib.diary_system import make_snippet

def test_first_five_words():
    result = make_snippet("Today I went to the park and had a walk.")
    assert result == "Today I went to the..."
    
def test_str_less_than_five_words():
    result = make_snippet("Today I went")
    assert result == "Today I went..."


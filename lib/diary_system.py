def make_snippet(text):

    if type(text) is not str:
        raise Exception("A string has not been entered.")
    
    new_str = text.strip().split()
    
    if len(new_str) > 5:
        return " ".join(new_str[:5])+"..."
    else:
        return " ".join(new_str)

def make_snippet(str):
    new_str = str.strip().split()
    return " ".join(new_str[:5])+"..."
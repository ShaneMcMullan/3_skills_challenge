def reading_time(text):

    if type(text) is not str:
        raise Exception("Invalid data type")

    if text == "":
        return "There is nothing to read!"
    
    string_length = len(text.strip().split())

    time_to_read = string_length / 200

    return f"It will take {time_to_read} minutes to read this"
    
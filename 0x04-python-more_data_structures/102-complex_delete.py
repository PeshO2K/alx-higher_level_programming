def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):  # Create a copy of keys
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary

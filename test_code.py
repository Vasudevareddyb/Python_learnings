input_string = "In the bustling bustling city city of New York, New York, the the bright bright lights lights and and the the constant constant hum hum of of activity activity create create an an atmosphere atmosphere that that is is both both exhilarating exhilarating and and exhausting exhausting."

def remove_duplicates(input_string):
    unique_string_list = []
    unique_string = ""
    words = input_string.split()
    for word in words:
        if word not in unique_string_list:
            unique_string_list.append(word)
    
    unique_string = ' '.join(unique_string_list)
    Addditional_String = "The bustling city lights and the constant hum of activity create an atmosphere that is both exhilarating and exhausting in New York."
    return unique_string + " " + Addditional_String
    

    
print(remove_duplicates(input_string))
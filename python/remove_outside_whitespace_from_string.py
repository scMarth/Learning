def remove_outside_whitespace_from_string(input_str):
    return (' ').join(input_str.split())

input_string = '       hi how are you '
print('|' + input_string + '|')
print('|' + remove_outside_whitespace_from_string(input_string) + '|')

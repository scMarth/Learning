import sys

int_var = 34
bool_var = True
array_of_ints = [int_var, int_var, int_var]
array_of_bools = [bool_var, bool_var, bool_var]
string_var = "The quick brown fox jumps over the lazy dog."
string_var_2 = "Hello World"
char_var = "a"
char_var2 = 'a'

print("int_var: " + str(int_var))
print(sys.getsizeof(int_var))
print("")
print("bool_var: " + str(bool_var))
print(sys.getsizeof(bool_var))
print("")
print("array_of_ints: " + str(array_of_ints))
print(sys.getsizeof(array_of_ints))
print("")
print("array_of_bools: " + str(array_of_bools))
print(sys.getsizeof(array_of_bools))
print("")
print("string_var: " + str(string_var))
print(sys.getsizeof(string_var))
print("")
print("string_var_2: " + str(string_var_2))
print(sys.getsizeof(string_var_2))
print("")
print("char_var: " + str(char_var))
print(sys.getsizeof(char_var))
print("")
print("char_var2: " + str(char_var2))
print(sys.getsizeof(char_var2))
print("")



'''
with open("single_char.txt", "w") as file:
   file.write(char_var2)

# the resulting file 'single_char.txt' is only 1 byte, despite char_var2 being 38 bytes

'''
import random, struct, datetime

def create_random_byte():
    binary_string = ""
    while len(binary_string) < 8:
        binary_string = binary_string + str(random.randint(0,1))
    output_char = struct.pack('B',int(binary_string, base=2))
    return output_char

print(datetime.datetime.now())
print("\nGenerating 'junkfile'...")

with open("junkfile", "wb") as outfile:
    for j in range(0,1000):
        for i in range(0,1000000): # 1 megabyte worth of data
            outfile.write(create_random_byte())

print("\nCompleted!\n")
print(datetime.datetime.now())

'''

Currently takes ~2h to do 300mb... not very practical

stretch goals: do multiprocessing without locking the output file so that
the random bytes are randomly interwoven?

does multiprocess writing to same file without locking the output file even work?
does it even cause the output to be interwoven?

actually.. what about simply storing the generated code in memory before writing it to disk?
will that speed up execution?

'''
import time

# without multithreading

def calc_square(numbers):
    print("calculate square numbers\n")
    for n in numbers:
        print("square:" + str(n*n) + "\n")

def calc_cube(numbers):
    print("calculate cube of numbers\n")
    for n in numbers:
        print("cube:" +  str(n*n*n) + "\n")

arr = range(0,1000)

t = time.time()
calc_square(arr)
calc_cube(arr)

first_time = time.time() - t

print("done in : ", first_time)
print("Done with all work.")

# with multithreading

import threading

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join() # wait until t1 is done
t2.join() # wait until t2 is done

second_time = time.time() - t

print("done in : ", second_time)
print("Done with all work.")

print("first run : ", first_time)
print("second run : ", second_time)

'''

range(0,1000)

('first run : ', 8.6489999294281)
('second run : ', 5.6600000858306885)

'''
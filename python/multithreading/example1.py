import time

# without multithreading

def calc_square(numbers):
    print("calculate square numbers\n")
    for n in numbers:
        time.sleep(0.2)
        print("square:" + str(n*n) + "\n")

def calc_cube(numbers):
    print("calculate cube of numbers\n")
    for n in numbers:
        time.sleep(0.2)
        print("cube:" +  str(n*n*n) + "\n")

arr = [2,3,8,9]

t = time.time()
calc_square(arr)
calc_cube(arr)

print("done in : ", time.time()-t)
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

print("done in : ", time.time()-t)
print("Done with all work.")
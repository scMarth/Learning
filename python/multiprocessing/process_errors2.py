# This program attempts to use multiple processes to process some dataset.
# Some values in the dataset cause the job function to fail, but that doesn't
# stop the other processes from completing and passing the data back to the
# main program.

import multiprocessing
from multiprocessing import Queue

def spawn(i, q):
    q.put(int(i))

# only runs if the script itself is being run.
# if the script is being called by something, the below code won't run
if __name__ == '__main__':
    q = Queue()
    inputs = [0, 1, "yes", 3, "no"]
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(inputs[i],q))
        p.start()
        p.join() # wait for process to complete
    print(range(5))
    while not q.empty():
        print(q.get())


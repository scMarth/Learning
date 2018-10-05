# This program attempts to use multiple processes to process some dataset.
# Some values in the dataset cause the job function to fail, but that doesn't
# stop the other processes from completing and passing the data back to the
# main program.

import multiprocessing
from multiprocessing import Queue

def spawn(i, q):
    result = None
    if i % 2 == 0:
        result = {"hello" : range(i)}
    else:
        result = range(i)
    q.put(result)

# only runs if the script itself is being run.
# if the script is being called by something, the below code won't run
if __name__ == '__main__':
    q = Queue()
    inputs = [0, 1, "yes", 3, "no", 4, 5, 6, 7, 8, 9, 10]
    processes = []

    for i in range(0,len(inputs)):
        p = multiprocessing.Process(target=spawn, args=(inputs[i],q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join() # wait for process to complete
        p.terminate() # terminate the process

    print(range(5))
    while not q.empty():
        print(q.get())


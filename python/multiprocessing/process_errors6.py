# If a process is killed / suddenly exits before it finishes its job,
# it causes a multiprocessing pool to hang..

import sys, multiprocessing, os
from multiprocessing import Pool

def error_sometimes(arg):
    if arg == 1:
        print("Killing: ")
        print(multiprocessing.current_process())
        print(multiprocessing.current_process().pid)
        os.kill(multiprocessing.current_process().pid, 9)
    try:
        return int(arg)
    except:
        return None

if __name__ == '__main__':
    p = Pool(processes=5)
    input = [1, 2, 3, 45, 5, "yes", 4, 3, 1, "bad"]
    data = p.map(error_sometimes, input)
    p.close()
    print(data) # this is never reached because of the error..

    

# Test if multiprocessing is working properly on a computer
# Creates a file called 'TEST_MULTIPROCESSING.txt' containing "aaaaaaa"

import multiprocessing, os

def spawn():
    with open(r"./TEST_MULTIPROCESSING.txt", "a") as file:
        file.write("a")

if __name__ == '__main__':

    processes = []

    # remove 'TEST_MULTIPROCESSING.txt" if it exists
    if os.path.exists(r"./TEST_MULTIPROCESSING.txt"):
        os.remove(r"./TEST_MULTIPROCESSING.txt")

    for i in range(0,7):
        p = multiprocessing.Process(target=spawn)
        processes.append(p)
        p.start()

    for p in processes:
        p.join() # wait for process to complete
        p.terminate() # terminate the process


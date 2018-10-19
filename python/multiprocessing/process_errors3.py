# do processes that error out stay 'alive' before you join?
# no...  they don't

import multiprocessing

def spawn(i, q):
    number = int(i)
    q.put([[i*number for i in range(0,100000)], multiprocessing.current_process().pid])

# only runs if the script itself is being run.
# if the script is being called by something, the below code won't run
if __name__ == '__main__':
    q = multiprocessing.Queue()
    processes = []
    inputs = [0, 1, "yes", 3, "no"]

    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(inputs[i],q))
        processes.append(p)
        p.start()

    # print whether the processes are alive or not
    print([p.is_alive() for p in processes])

    # wait for the expected 3 results
    while q.qsize() < 3:
        continue

    # get the results
    while not q.empty():
        q.get()

    # print whether the processes are alive or not
    print([p.is_alive() for p in processes])

    for p in processes:
        p.join()
        p.terminate()

    # print whether the processes are alive or not
    print([p.is_alive() for p in processes])


# Same as groups_of_processes3 except uses pipes instead of multiprocessing queues

import multiprocessing, sys, os, datetime

def job(input_number, con):
    if input_number in [3, 5, 16]: # randomly kill some processes
        os.kill(multiprocessing.current_process().pid, 9)
    con.send([input_number])
    con.close()

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(start_time)
    print("\nStarting...")
    inputs = range(0,5000)
    # inputs = [0, 2, 3]

    process_results = []
    MAX_GROUP_SIZE = 30
    input_index = 0
    processes = []

    print("number of inputs: " + str(len(inputs)))

    while input_index < len(inputs) or len([p for p in processes if p[0].is_alive()]) > 0:
        # print(multiprocessing.active_children())
        if len(multiprocessing.active_children()) < MAX_GROUP_SIZE and input_index < len(inputs):
            parent_con, child_con = multiprocessing.Pipe()
            p = multiprocessing.Process(target=job, args=(inputs[input_index], child_con))
            input_index += 1
            processes.append([p, parent_con])
            p.start()

        dead_processes = [p for p in processes if p[1].poll()]
        for p in dead_processes:
            try:
                process_results.append(p[1].recv())
            except:
                continue # 'gracefully' handle an EOFError the Pyth0n1c w@y ?
            # print("finished one process" + str(p))
            p[1].close()
            p[0].join()
            p[0].terminate()

    print("Exited process loop")

    print("\nnumber of results: " + str(len(process_results)))
    print("\nDone.\n")
    end_time = datetime.datetime.now()
    print(end_time)

    print("Time to complete: " + str(end_time - start_time))

# maybe have a look at this: https://stackoverflow.com/questions/8594909/python-multiprocessing-pipe-recv-doc-unclear-or-did-i-miss-anything
# test if pipes cause processes to hang until the data has been received?
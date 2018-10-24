# Same as groups_of_processes3 except uses pipes instead of multiprocessing queues

import multiprocessing, sys, os, datetime

def job(input_number, con):
    if input_number in [3, 5, 16]: # randomly kill some processes
        os.kill(multiprocessing.current_process().pid, 9)
    con.send([i*input_number for i in range(0,100000)])
    con.close()

if __name__ == "__main__":
    print(datetime.datetime.now())
    print("\nStarting...")
    inputs = range(0,3000)
    # inputs = [0, 2, 3]

    process_results = []
    MAX_GROUP_SIZE = 30
    input_index = 0
    processes = []

    print("number of inputs: " + str(len(inputs)))

    while input_index < len(inputs) or len([p for p in processes if p[0].is_alive()]) > 0 or len([p for p in processes if p[1].poll()]) > 0:
        # print(multiprocessing.active_children())
        if len(multiprocessing.active_children()) < MAX_GROUP_SIZE and input_index < len(inputs):
            parent_con, child_con = multiprocessing.Pipe()
            p = multiprocessing.Process(target=job, args=(inputs[input_index], child_con))
            input_index += 1
            processes.append([p, parent_con])
            p.start()

        dead_processes = [p for p in processes if p[1].poll()]
        for p in dead_processes:
            process_results.append(p[1].recv())
            p[0].join()
            p[0].terminate()

    print("Exited process loop")

    print("\nnumber of results: " + str(len(process_results)))
    print("\nDone.\n")
    print(datetime.datetime.now())
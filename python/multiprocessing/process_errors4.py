# In this example, an input set is given to a pool of processes. These
# inputs sometimes cause the target job to error out. The program still
# gracefully waits for as much inputs it can get as possible.

# Code isn't very D.R.Y., but it seems to avoid Spaghetti code

import multiprocessing, sys

def job(q, perhaps_a_number):
    number = int(perhaps_a_number)
    q.put([[i*number for i in range(0,100000)], multiprocessing.current_process().pid])

def join_and_terminate_process(processes, pid):
    dead_process = [p for p in processes if p.pid == pid][0]
    dead_process.join()
    dead_process.terminate()

if __name__ == "__main__":
    print("Starting...")

    q = multiprocessing.Queue()

    inputs = range(0,40)
    inputs[3] = "Hello"
    inputs[13] = "Hello"
    inputs[17] = "Hello"
    inputs[25] = "Hello"
    inputs[35] = "Hello"

    process_results = []
    MAX_GROUP_SIZE = 5
    input_index = 0
    processes = []
    num_finished_processes = 0

    print("number of processes: " + str(len(processes)))
    print("number of inputs: " + str(len(inputs)))
    print("")

    # while num_finished_processes < len(inputs):
    while input_index < len(inputs):
        if len(multiprocessing.active_children()) < MAX_GROUP_SIZE and input_index < len(inputs):
            p = multiprocessing.Process(target=job, args=(q,inputs[input_index]))
            input_index += 1
            processes.append(p)
            p.start()

        # join and terminate any processes that have completed
        while not q.empty():
            return_value = q.get()
            result = return_value[0]
            pid = return_value[1]
            join_and_terminate_process(processes, pid)
            num_finished_processes += 1
            process_results.append(result)

    # wait for the remaining alive processes to complete, and store
    # their results
    while True:
        alive_processes = [p for p in processes if p.is_alive()]
        if len(alive_processes) == 0:
            break

        while not q.empty():
            return_value = q.get()
            result = return_value[0]
            pid = return_value[1]
            join_and_terminate_process(processes, pid)
            num_finished_processes += 1
            process_results.append(result)

    print("\nnumber of results: " + str(len(process_results)))
    print("num_finished_processes: " + str(num_finished_processes))
    print("Done.")
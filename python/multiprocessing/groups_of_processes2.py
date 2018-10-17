# This example shows how to limit the number of processes to an arbitrary group size

import multiprocessing, sys

def job(q, input):
    q.put([[i*input for i in range(0,100000)], multiprocessing.current_process().pid])

if __name__ == "__main__":
    print("Starting...")

    q = multiprocessing.Queue()

    inputs = range(0,30)

    process_results = []
    MAX_GROUP_SIZE = 5
    input_index = 0
    processes = []
    num_finished_processes = 0

    print("number of processes: " + str(len(processes)))
    print("number of inputs: " + str(len(inputs)))
    print("")

    while num_finished_processes < len(inputs):
        if len(multiprocessing.active_children()) < MAX_GROUP_SIZE and input_index < len(inputs):
            p = multiprocessing.Process(target=job, args=(q,inputs[input_index]))
            input_index += 1
            processes.append(p)
            p.start()

        while not q.empty():
            return_value = q.get()
            result = return_value[0]
            pid = return_value[1]
            num_finished_processes += 1
            process_results.append(result)
             # this may or may not be empty because sometimes by this time, the process has already died, and therefore no longer a subset of multiprocessing.active_children()
            dead_processes = [p for p in multiprocessing.active_children() if p.pid == pid]
            for p in dead_processes:
                p.join()
                p.terminate()

    print("\nnumber of results: " + str(len(process_results)))
    print("num_finished_processes: " + str(num_finished_processes))
    print("Done.")
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

        # join and terminate any processes that have completed
        while not q.empty():
            return_value = q.get()
            result = return_value[0]
            pid = return_value[1]
            dead_process = [p for p in processes if p.pid == pid][0]
            dead_process.join()
            dead_process.terminate()
            num_finished_processes += 1
            process_results.append(result)

    print("\nnumber of results: " + str(len(process_results)))
    print("num_finished_processes: " + str(num_finished_processes))
    print("Done.")
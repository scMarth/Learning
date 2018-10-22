# This example shows how to limit the number of processes to MAX_GROUP_SIZE
# it doesn't matter whether the job processes is killed before it joins or not

import multiprocessing, sys, os

def job(q, input_number):
    if input_number in [3, 5, 16]: # randomly kill some processes
        os.kill(multiprocessing.current_process().pid, 9)
    q.put([[i*input_number for i in range(0,100000)], multiprocessing.current_process().pid])

if __name__ == "__main__":
    print("Starting...")

    q = multiprocessing.Queue()

    inputs = range(0,30)

    process_results = []
    MAX_GROUP_SIZE = 5
    input_index = 0
    processes = []

    print("number of processes: " + str(len(processes)))
    print("number of inputs: " + str(len(inputs)))

    while input_index < len(inputs) or len([p for p in processes if p.is_alive()]) or not q.empty():
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
            process_results.append(result)

    print("\nnumber of results: " + str(len(process_results)))
    print("Done.")
# This example shows how to limit the number of processes to MAX_GROUP_SIZE
# it doesn't matter whether the job processes is killed before it joins or not
# CPU usage stays below
#    % for 1 processes
#    20% for 5 processes
#    40% for 100 processes
#    44% for 200 processes
#    48% for 300 processes

import multiprocessing, sys, os, datetime

def job(q, input_number):
    if input_number in [3, 5, 16]: # randomly kill some processes
        os.kill(multiprocessing.current_process().pid, 9)
    q.put([[i*input_number for i in range(0,100000)], multiprocessing.current_process().pid]) # slow

if __name__ == "__main__":
    print(datetime.datetime.now())
    print("\nStarting...")

    q = multiprocessing.Queue()

    inputs = range(0,3000)

    process_results = []
    MAX_GROUP_SIZE = 30
    input_index = 0
    processes = []

    print("number of inputs: " + str(len(inputs)))

    while input_index < len(inputs) or len([p for p in processes if p.is_alive()]) > 0 or not q.empty():
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
    print("\nDone.\n")
    print(datetime.datetime.now())
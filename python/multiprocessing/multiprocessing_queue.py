# This example shows how to have a worker process pass a large amount of
# data back to the main program

import multiprocessing

class WorkerProcess(multiprocessing.Process):
    def __init__(self, queue, size):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.size = size

    def run(self):
        self.queue.put(range(size))

if __name__ == "__main__":
    size = 100000
    queue = multiprocessing.Queue()

    print("starting worker process:")
    worker_process = WorkerProcess(queue, size)

# this will hang:
    # worker_process.start()
    # worker_process.join()
    # print("process results length: " + len(queue.get()))

# this will not hang:
    worker_process.start()
    # wait while the queue is empty
    while queue.empty():
        continue
    got = queue.get()
    worker_process.join()
    print("process results length: " + str(len(got)))


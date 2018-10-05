import multiprocessing, os
from multiprocessing import Queue

class Real:
    def __init__(self, realpart):
        self.r = realpart

    def printReal(self):
        print(self.r)

class Complex(Real): # real is the base class
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def printReal(self):
        print(self.r)

    def printImag(self):
        print(self.i)

    def printRealAndImag(self):
        self.printReal()
        self.printImag()

    def setRealAndImag(self, realPart, imagPart):
        self.r = realPart
        self.i = imagPart

def spawn(i, j, q):
    with open(r"./TEST_MULTIPROCESSING.txt", "a") as file:
        file.write("signal 0\n")
        file.write("i: {0} ; j: {1}".format(i,j))
        file.write("\n")

    c_num = Complex(i, j)

    with open(r"./TEST_MULTIPROCESSING.txt", "a") as file:
        file.write("signal 1\n")

    q.put(c_num)

    with open(r"./TEST_MULTIPROCESSING.txt", "a") as file:
        file.write("signal 2\n\n")


if __name__ == '__main__':

    q = Queue()
    processes = []

    # remove 'TEST_MULTIPROCESSING.txt" if it exists
    if os.path.exists(r"./TEST_MULTIPROCESSING.txt"):
        os.remove(r"./TEST_MULTIPROCESSING.txt")

    for i in [0,1]:
        p = multiprocessing.Process(target=spawn, args=(i, i+1, q))
        processes.append(p)
        p.start()
        p.join() # wait for process to complete
        p.terminate() # terminate the process

    # for p in processes:
    #     p.join() # wait for process to complete
    #     p.terminate() # terminate the process

    while not q.empty():
        c_num = q.get()
        c_num.printReal()
        c_num.printImag()
        print("")


import multiprocessing

def job(con):
    con.send("message")
    con.close()

if __name__ == "__main__":

    a, b = multiprocessing.Pipe()
    p = multiprocessing.Process(target=job, args=(b,))
    p.start()
    print(a.poll())
    while not a.poll():
        continue
    print(a.poll())
    print(a.recv())
    print(a.poll())
    a.close()
    # print(a.poll()) # causes IOError: [Errno 6] The handle is invalid because you're trying to poll a pipe that has already been closed.
    p.join()



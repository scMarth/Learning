import multiprocessing

def job(input_number, con):
    con.send([i*input_number for i in range(0,100000)])
    con.close()

if __name__ == '__main__':
    parent_con, child_con = multiprocessing.Pipe()

    inputs = [0]

    p = multiprocessing.Process(target=job, args=(inputs[0],child_con))
    p.start()
    while not parent_con.poll():
        continue
    print(parent_con.poll())
    test = parent_con.recv()
    # print(parent_con.recv())
    print(parent_con.poll())
    print(p.is_alive())
    p.join()
    print(p.is_alive())
    print("Done")


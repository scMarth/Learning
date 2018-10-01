from multiprocessing import Pool

def job(args):
    num = args[0]
    num2 = args[1]
    return num * num2

if __name__ == '__main__':
    p = Pool(processes=20)

    input_set = []
    for i in range(500):
        input_set.append([i, i+1])

    data = p.map(job, input_set)
    p.close()
    print(data)

    

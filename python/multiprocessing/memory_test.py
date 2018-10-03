from multiprocessing import Pool

def job(args):
    num = args[0]
    num2 = args[1]

    lots_of_data = []
    for i in range(5000):
        lots_of_data.append(i+num+num2)

    return lots_of_data[2500]

if __name__ == '__main__':
    p = Pool(processes=2)

    input_set = []
    for i in range(50000):
        input_set.append([i, i+1])

    data = p.map(job, input_set)
    p.close()
    print(data)

    

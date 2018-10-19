# What happens when some processes in a pool of processes fail?
#
# A. It gives an error and all other processes after it don't get to execute

from multiprocessing import Pool

def error_sometimes(arg):
    try:
        return int(arg)
    except:
        return None

if __name__ == '__main__':
    p = Pool(processes=20)
    input = [1, 2, 3, 45, 5, "yes", 4, 3, 1, "bad"]
    data = p.map(error_sometimes, input)
    p.close()
    print(data) # this is never reached because of the error..

    

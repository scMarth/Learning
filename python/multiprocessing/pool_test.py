# a test to see if this pool successfully completes its inputs when
# the target job only returns a value sometimes

import multiprocessing

def job(returnSomething):
    if returnSomething:
        return "Hello"

if __name__ == "__main__":
    inputs = [True, False, True, True, False, True, True, False, False, False, True]

    pool = multiprocessing.Pool(processes=5)
    results = pool.map(job, inputs)
    print(inputs)
    print(results)
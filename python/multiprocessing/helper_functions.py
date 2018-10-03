import multiprocessing

def helper_print_function(string):
    print(string)

def spawn(i):
    helper_print_function("Spawned: " + str(i))

# only runs if the script itself is being run.
# if the script is being called by something, the below code won't run
if __name__ == '__main__':
    for i in range(50,101):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        # p.join() # wait for process to complete

import multiprocessing

def spawn(i):
    print("Spawned!" + i)

# only runs if the script itself is being run.
# if the script is being called by something, the below code won't run
if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join() # wait for process to complete
        input("Press Enter to continue...")

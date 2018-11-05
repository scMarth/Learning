import time
import multiprocessing

def print_every_sec():
    while True:
        print("Every second.")
        time.sleep(1)

def print_every_4_secs():
    while True:
        print("Every 4 seconds.")
        time.sleep(4)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_every_sec)
    p2 = multiprocessing.Process(target=print_every_4_secs)
    p1.start()
    p2.start()
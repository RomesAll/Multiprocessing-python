from random import random
from multiprocessing import Process, Lock
import time, os

def file_wr(start: int, finish:int, l):
    l.acquire()
    for i in range(start, finish):
        with open("locker.txt", "a") as f:
            time.sleep(.1)
            print(i)
            f.write(str(i) + "\n")
    l.release()

if __name__ == '__main__':
    lock = Lock() 
    p1 = Process(target=file_wr, args=(0, 5, lock))
    p2 = Process(target=file_wr, args=(5, 10, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
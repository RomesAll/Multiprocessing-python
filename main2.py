import multiprocessing, os, time
CNT = 0

def f():
    global CNT 
    print('f started from ', os.getpid())
    time.sleep(5)
    CNT += 2
    print(f'f: {CNT} from ', os.getpid())

if __name__ == '__main__':
    p = multiprocessing.Process(target=f, args=())
    p.start()
    p.join()
    print('Finished')
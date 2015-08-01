from multiprocessing import Pool
from time import sleep

def f():
    c = 0
    while True:
        f = open('/home/josh/Desktop/' + str(c) + '.txt', 'w')
        f.close()
        c += 1
        sleep(0.5)

if __name__ == '__main__':
    p = Pool()
    p.apply_async(f) 
    sleep(2)
    p.terminate()
    p.join()
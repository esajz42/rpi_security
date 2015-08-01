from multiprocessing import Pool
from time import sleep

def f(name):
    while True:
        print 'hello', name
        sleep(0.5)

if __name__ == '__main__':
    p = Pool()
    p.apply_async(f, ['bob'])
    sleep(4)
    p.terminate()
    p.join()
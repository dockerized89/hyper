__author__ = 'elopptj'

import multiprocessing as mp
import time


def worker():

    print('Starting', mp.current_process().name)
    for x in range(1000000):
        time.sleep(0.0003)
    print('Ending', mp.current_process().name)



def main():
    start = time.time()

    for n in range(10):
        process = mp.Process(target=worker)
        process.start()

    process.join()
    print("Took ", time.time() - start)
    print('We are done!')


if __name__ == '__main__':
    main()


import threading
import time

__author__ = 'elopptj'

from queue import Queue


queue = Queue()


def worker():
    x = queue.get()
    print('Starting', threading.current_thread().name)
    for x in range(100000):
        time.sleep(0.000003)
    queue.task_done()

    print('Ending', threading.current_thread().name)


def main():
    for i in range(10):
        queue.put(i)

    start = time.time()
    for n in range(10):
        t = threading.Thread(target=worker)
        t.daemon = True

        t.start()

    queue.join()
    print("Took ", time.time() - start)
    print('We are done!')


if __name__ == '__main__':
    main()

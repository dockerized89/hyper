import itertools
from math import sqrt
import threading
import time

__author__ = 'elopptj'

from queue import Queue


def split_seq(iterable, size):
    it = iter(iterable)

    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))


def create_lists(max, numPerList):
    return list(split_seq(range(max), numPerList))
    pass


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def is_prime_v1(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    if number % 2 == 0:
        return False

    sqrtN = sqrt(number)
    i = 2
    while i < sqrtN:
        if number % i == 0:
            return False
        i += \
            1
    return True


def main():
    q = Queue()
    prime_list = []
    list_lock = threading.Lock()
    work_lists = create_lists(1000000, 1000)

    for l in work_lists:
        q.put(l)

    print("Setup done!")

    # Worker function for the threads.
    def worker():
        while True:
            list_to_work_on = q.get()
            for num in list_to_work_on:
                if is_prime(num):
                    with list_lock:
                        prime_list.append(num)
                    time.sleep(0.00005)
            q.task_done()
            print(threading.current_thread().getName(), "is done with a task. : ", q.unfinished_tasks, "tasks left")

    start = time.time()

    for i in range(100):
        t = threading.Thread(target=worker)
        t.daemon = True
        print('Starting thread', i)
        t.start()

    q.join()

    print('Took', time.time() - start, 'seconds')

    prime_list.sort()
    print(prime_list)


if __name__ == '__main__':
    main()

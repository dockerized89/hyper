import threading
import time
from collections import Counter
from queue import Queue

__author__ = 'elopptj'

queue = Queue()
lock = threading.Lock()

result_list = {}


# Get the file at dockerized.org/static/alice.txt
# Help functions
def get_content(split=' '):
    try:
        with open('alice.txt', 'r') as file_obj:
            content = file_obj.read()
            return content.split(split)
    except IOError as e:
        print('File not found....', e)


def word_counter1():
    # count-list-items-1.py

    wordlist = get_content()

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    print("List\n" + str(wordlist) + "\n")
    print("Frequencies\n" + str(wordfreq) + "\n")
    print("Total words: " + str(len(wordlist)))


def word_counter2():
    wordlist = get_content()

    wordfreq = [wordlist.count(w) for w in wordlist]  # a list comprehension

    print("List\n" + str(wordlist) + "\n")
    print("Frequencies\n" + str(wordfreq) + "\n")


def word_counter3():
    for n in range(10):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    row_list = get_content(split='\n')
    for i in range(len(row_list)):
        queue.put({'row': i, 'content': row_list[i]})

    queue.join()

    sorted_dict = sorted(result_list.items(), reverse=True, key=lambda x: x[1])
    for key, value in sorted_dict:
        print('Word:' + '\'' + str(key) + '\'' + ' Count:' + str(value))

    print("\nTotal words: {0}".format(len(sorted_dict)))

    print("Top 20 words: ".format())

    for i in range(0, 19):
        word = sorted_dict[i][0]
        count = sorted_dict[i][1]
        print('Word: {0}{1}'.format(word, ', '), 'Count: {0}'.format(count))


def do_work(item):
    print('Counting row {0}'.format(item['row']))
    content = item['content'].split()
    freq = dict(Counter(content).items())

    with lock:
        for key, value in freq.items():
            if key in result_list:
                result_list[key] += 1
            else:
                result_list.update({key: value})


def worker():
    while True:
        item = queue.get()
        do_work(item)
        queue.task_done()


def main():
    start = time.time()
    word_counter1()

    #finished = (time.time() - start)


if __name__ == '__main__':
    main()

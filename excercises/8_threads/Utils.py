__author__ = 'elopptj'

import time


class StopWatch():
    def __init__(self):
        self.totalTime = 0.
        self.start = 0.
        self.stop = 0.

    def start(self):
        self.start = self.__getCurrTime()

    def stop(self):
        self.stop = self.__getCurrTime()

    def getTime(self):
        return self.stop - self.start

    def __getCurrTime(self):
        return int(round(time.time() * 1000))

    def getFinalTime(self):
        pass
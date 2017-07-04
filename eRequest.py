import datetime


class request(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def setStart(self, startTime):
        self.start = startTime

    # @staticmethod
    def getStart(self):
        return self.start

    def setEnd(self, endTime):
        self.end = endTime

    # @staticmethod
    def getEnd(self):
        return self.end

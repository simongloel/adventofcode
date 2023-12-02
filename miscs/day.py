from miscs.formatter import Formatter

class Day:
    def __init__(self, day, year):
        self.day = day
        self.year = year
        self.formatter = None

    def getInput(self):
        f = open("../inputs/" + str(self.year) + "-" + str(self.day) + ".txt", "r")
        return f.read()

    def createFormatter(self):
        if self.formatter:
            return self.formatter
        else:
            self.formatter = Formatter()
            return self.formatter


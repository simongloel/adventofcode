import sys

sys.path.append('../')
from miscs.day import Day


class DayOne(Day):
    def __init__(self):
        super().__init__(1, 2023)
        self.createFormatter()
        self.list = self.formatter.toList(self.getInput())
    def getDigit(self, entry):
        digit = None
        entry_length = len(entry)
        i = 0
        while i < entry_length and digit is None:
            currentChar = entry[i]
            if currentChar.isdigit():
                digit = int(currentChar)
            i = i + 1
        return digit


currentDay = DayOne()
formatter = currentDay.formatter
endResult = 0
for entry in currentDay.list:
    firstDigit = currentDay.getDigit(entry)
    reversed_entry = formatter.reverse(entry)
    lastDigit = currentDay.getDigit(reversed_entry)
    result = int(str(firstDigit) + str(lastDigit))
    endResult = endResult + result
print("The end result is " + str(endResult))
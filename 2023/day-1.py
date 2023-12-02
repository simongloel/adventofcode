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

# SECOND PART START

replaceDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
i = 0
for entry in currentDay.list:
    currentDay.list[i] = formatter.replaceByDict(entry, replaceDict)
    print(currentDay.list[i])
    i = i + 1

# SECOND PART END

endResult = 0
for entry in currentDay.list:
    firstDigit = currentDay.getDigit(entry)
    reversed_entry = formatter.reverse(entry)
    lastDigit = currentDay.getDigit(reversed_entry)
    result = int(str(firstDigit) + str(lastDigit))
    endResult = endResult + result
print("The end result is " + str(endResult))

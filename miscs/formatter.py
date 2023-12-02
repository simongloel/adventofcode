class Formatter:
    def __init__(self):
        pass

    def toList(self, input):
        return input.split("\n")

    def reverse(self, input):
        return input[::-1]
    def replaceByDict(self, input, dict):
        for entry in dict.keys():
            input = input.replace(entry, entry + str(dict.get(entry)) + entry)
        return input
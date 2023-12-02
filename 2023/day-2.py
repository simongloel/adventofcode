import sys

sys.path.append('../')
from miscs.day import Day


class DayTwo(Day):
    def __init__(self):
        super().__init__(2, 2023)
        self.createFormatter()
        self.list = self.formatter.toList(self.getInput(), "\n")
    def getDictOfSet(self, set_entry):
        sets = set_entry.split("; ")
        i = 0
        for set in sets:
            sets[i] = set.split(", ")
            colorDict = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for entry in sets[i]:
                color = entry.split(" ")[1]
                count = entry.split(" ")[0]
                colorDict[color] = count
            sets[i] = colorDict
            i = i + 1
        return sets
    def createDictOfGame(self, game_entry):
        set_string = game_entry.split(": ")[1]

        game_id = game_entry.split(":")[0].split("Game ")[1]
        newDict = {
            "game_id": game_id,
            "sets": self.getDictOfSet(set_string)
        }
        return newDict





currentDay = DayTwo()
formatter = currentDay.formatter
games = []
for entry in currentDay.list:
    games.append(currentDay.createDictOfGame(entry))

possibleCubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}
sumGameIds = 0
sumPower = 0
for game in games:
    gameValid = True
    gamePower = 1
    highestOfGame = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for set in game["sets"]:
        cubesOfSet = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for key in set.keys():
            currentValue = int(set.get(key))
            cubesOfSet[key] = cubesOfSet[key] + currentValue
            if currentValue > highestOfGame[key]:
                highestOfGame[key] = currentValue
        # Check validity of set:
        setValid = True
        for key in cubesOfSet.keys():
            if cubesOfSet.get(key) > possibleCubes.get(key):
                # game invalid
                setValid = False
        if setValid == False:
            gameValid = False

    if gameValid == True:
        sumGameIds = sumGameIds + int(game["game_id"])

    for key in highestOfGame.keys():
        if highestOfGame.get(key) > 0:
            gamePower = gamePower * highestOfGame.get(key)
    sumPower = sumPower + gamePower

print("The end result is " + str(sumGameIds))
print("The sum of power is " + str(sumPower))
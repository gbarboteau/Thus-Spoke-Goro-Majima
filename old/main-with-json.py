import random
import json

characters = ["Jotaro Kujo", "joseph joestar", "Josuke higashikata", "rohan Kishibe", "Koichi Hirose", "Okuyasu Nijimura"]
actions = ["determined to beat Killer Queen", "taking a nap", "using his stand", "thinking about Dio", "searching for Kira"]


def readValueFromJson():
    values = []
    with open('charactersYakuza.json') as f:
        data = json.load(f)
        for entry in data:
            values.append(entry["character"])
    return values

def GetRandomItem(myList):
    randomNumber = random.randint(0, len(myList) - 1)
    return myList[randomNumber]

def RandomCharacter():
    allValues= readValueFromJson()
    return GetRandomItem(allValues)

def RandomAction(characters, actions):
    return "{} is {}".format(RandomCharacter(), GetRandomItem(actions))

userInput = input("Tapez Entrée pour une autre citation de Jojo, Q pour quitter")

while userInput.lower() != "q":
    print(RandomAction(characters, actions))
    userInput = input("Tapez Entrée pour une autre citation de Jojo, Q pour quitter")


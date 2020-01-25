import random

characters = ["Jotaro Kujo", "joseph joestar", "Josuke higashikata", "rohan Kishibe", "Koichi Hirose", "Okuyasu Nijimura"]
actions = ["determined to beat Killer Queen", "taking a nap", "using his stand", "thinking about Dio", "searching for Kira"]

def GetRandomItem(myList):
    randomNumber = random.randint(0, len(myList) - 1)
    return myList[randomNumber]

def RandomAction(characters, actions):
    return "{} is {}".format(GetRandomItem(characters).capitalize(), GetRandomItem(actions))

userInput = input("Tapez Entrée pour une autre citation de Jojo, Q pour quitter")

while userInput.lower() != "q":
    print(RandomAction(characters, actions))
    userInput = input("Tapez Entrée pour une autre citation de Jojo, Q pour quitter")


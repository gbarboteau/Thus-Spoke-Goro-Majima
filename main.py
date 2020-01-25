import json
import random
import sys

#The first argument you write on the command line will be the file containing every characters, the second will contain every quotes
#I used the scrapy library to collect those datas, look inside the spiders folder for those scripts
#IMPORTANT: The way these files are named are important: if your file is named "characters.json", the script will use the key "character" to search for corresponding values
#If your file is named "quotes.json", it'll search for values of keys named "quote", etc...
characters = sys.argv[1]
quotes = sys.argv[2]

#Return a Nietzche quote said by a Yakuza character, or... Anything you want.
#Try to let Pokemon say Bernie Sanders quotes, or Final Fantasy characters sing Celine Dion lyrics. The choice is yours.
def RandomQuote(c, q):
    return "{} says: {}".format(RandomElement(c, sys.argv[1][:-6]), RandomElement(q, sys.argv[2][:-6]))

#Return a random element from a list
def RandomElement(f, k):
    myList = readValuesFromJson(f, k)
    return GetRandomItem(myList)

#Make a list from a .json file
#IMPORTANT: the key this function uses to read the file is always the name of the file
def readValuesFromJson(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values

#Get a random element from a list
def GetRandomItem(myList):
    randomNumber = random.randint(0, len(myList) - 1)
    return myList[randomNumber]

#Wait for an input from the user, quit if the letter Q is entered
userInput = input("Press Enter for another quote, Q to quit")
while userInput.lower() != "q":
    print(RandomQuote(characters, quotes))
    userInput = input("Press Enter for another quote, Q to quit")



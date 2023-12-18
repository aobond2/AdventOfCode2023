import os
import re

inputName = "input"
numberArray = []

def GetInputTextFile():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    fileInDir = os.listdir(currentDir)
    textFiles = [file for file in fileInDir if file.endswith(".txt")]
    for textFile in textFiles:
        if inputName in textFile:
            return textFile

def ReadInputText():
    input = GetInputTextFile()
    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            #na = checkNonAlphaNumeric(line)
            checkNumeric(line)

def checkNonAlphaNumeric(string):
    matches = re.findall(r"[^\w\d\.]", string)
    return matches

def checkNumeric(string):
    result = []
    numbersList = []
    orderList = []
    for i in range(len(string)):
        if string[i].isdigit():
            numbersList.append(int(string[i]))
            orderList.append(i)
        elif string[i] == '.':
            if numbersList:
                # Combine number and order list to a tuple
                combinedTuple = (numbersList, orderList)
                result.append(combinedTuple)
                numbersList = []
                orderList = []
    print(result)

if __name__ == "__main__":
    ReadInputText()
import os
import re

inputName = "input"
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
            na = checkNonAlphaNumeric(line)
            print (na)

def checkNonAlphaNumeric(string):
    matches = re.findall(r"[^\w\d\.]", string)
    return matches

if __name__ == "__main__":
    ReadInputText()
import os

inputName = "input"
sum = 0

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
            ProcessLine(line)
    print(sum)

def ProcessLine(line):
    global sum
    strippedLine = line.strip()
    numberArray = []
    for char in strippedLine:
        if char.isdigit():
            numberArray.append(char)
    if len(numberArray) == 1:
        newNumber = int(str(numberArray[0]) + str(numberArray[0]))
        sum += newNumber
        print (sum)
    elif len(numberArray) > 1:
        firstNumber = numberArray[0]
        lastNumber = numberArray[-1]
        newNumber = int(str(firstNumber) + str(lastNumber))
        sum += newNumber
        print (sum)

ReadInputText()
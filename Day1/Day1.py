import os

inputName = "input"
sum = 0
numberDict = {
    'one' : 1,
    'two' : 2, 
    'three' : 3, 
    'four' : 4, 
    'five' : 5, 
    'six' : 6, 
    'seven' : 7, 
    'eight' : 8, 
    'nine' : 9
}

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

def CheckIfKeyInString(dict, line, array, indexArray):
    for key in dict.keys():
        index = line.find(key)
        while index != -1:
            array.append(str(dict[key]))
            indexArray.append(index)
            index = line.find(key, index + 1)
    sortedNumber, sortedIndex = SortArrayPair(array, indexArray)
    return sortedNumber, sortedIndex

def SortArrayPair(numberArray, indexArray):
    m = len(numberArray)
    for i in range(m):
        for j in range(0, m-i-1):
            if (indexArray[j] > indexArray[j+1]):
                indexArray[j], indexArray[j+1] = indexArray[j+1], indexArray[j]
                numberArray[j], numberArray[j+1] = numberArray[j+1], numberArray[j]
    return numberArray, indexArray

def ProcessLine(line):
    global sum
    strippedLine = line.strip()
    numberArray = []
    indexArray = []

    result = [(char, index) for index, char in enumerate(strippedLine) if char.isdigit()]

    for i in range(len(result)):
        numberArray.append(result[i][0])
        indexArray.append(result[i][1])    

    sortedNumberArray, sortedIndex = CheckIfKeyInString(numberDict, strippedLine, numberArray, indexArray)
    
    if len(sortedNumberArray) == 1:
        newNumber = int((sortedNumberArray[0]) + (sortedNumberArray[0]))

    elif len(numberArray) > 1:
        firstNumber = sortedNumberArray[0]
        lastNumber = sortedNumberArray[-1]
        newNumber = int((firstNumber) + (lastNumber))
    
    sum += newNumber

if __name__ == "__main__":
    ReadInputText()
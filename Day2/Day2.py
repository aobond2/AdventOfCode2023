import os

inputName = "input"
cubeRuleDict = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
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
            line = line.strip()
            ProcessLine(line)

def ProcessLine(line):
    passCheck = 0
    cubeSetDict = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    separateLine = line.split(':')
    gameID = (separateLine[0].split('Game '))[1].strip()
    cubeSets = separateLine[1].strip()
    cubeSetsArray = (cubeSets.split(';'))
    for cubeSet in cubeSetsArray:
        cubeSet = cubeSet.strip()
        individualCubeArray = cubeSet.split(',')
        for individualCube in individualCubeArray:
            individualCube = (individualCube.strip())
            individualCubeKey = (individualCube.split())[1]
            individualCubeValue = (individualCube.split())[0]
            cubeSetDict[individualCubeKey] = individualCubeValue
        print (cubeSetDict)
        x = compareDictionary(cubeRuleDict, cubeSetDict)
        print(x)

def compareDictionary(baseDictionary, targetDictionary):
    for key in baseDictionary:
        if key in targetDictionary and int(targetDictionary[key]) > int(baseDictionary[key]):
            return True
        return False

if __name__ == "__main__":
    ReadInputText()
import os

inputName = "input"
cubeRuleDict = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}
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
            line = line.strip()
            ProcessLine(line)
    print (sum)

def ProcessLine(line):
    global sum
    failCheck = 0
    print (line)
    separateLine = line.split(':')
    gameID = (separateLine[0].split('Game '))[1].strip()
    cubeSets = separateLine[1].strip()
    cubeSetsArray = (cubeSets.split(';'))
    for cubeSet in cubeSetsArray:
        cubeSetDict = {
                'red' : 0,
                'green' : 0,
                'blue' : 0
            }
        cubeSet = cubeSet.strip()
        individualCubeArray = cubeSet.split(',')
        for individualCube in individualCubeArray:
            individualCube = (individualCube.strip())
            individualCubeKey = (individualCube.split())[1]
            individualCubeValue = (individualCube.split())[0]
            cubeSetDict[individualCubeKey] = individualCubeValue
        x = compareDictionary(cubeRuleDict, cubeSetDict)
        print (cubeSetDict)
        failCheck += x
    print (failCheck)
    
    if failCheck == 0:
        sum += int(gameID)
        #print (line)

def compareDictionary(baseDictionary, targetDictionary):
    # Check if any value is larger than base dictionary
    for key in baseDictionary:
        if (int(targetDictionary[key]) > int(baseDictionary[key])) or (int(targetDictionary[key]) == int(baseDictionary[key])):
            return 1
        return 0

if __name__ == "__main__":
    ReadInputText()
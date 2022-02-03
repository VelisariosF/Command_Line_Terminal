def loadCommandsList(path):
    f = open(path, "r")
    lines = f.readlines()
    tokenizedLines = []
    for line in lines:
        tokenizedLines.append(line.rstrip())
    return tokenizedLines


def constructPreviousPathFromList(pathList):
    delimiter = "\\"
    path = ""
    for i in range(0, len(pathList) - 1):
        if(i != len(pathList) - 1):
           path = path + pathList[i] + delimiter
        else:
           path = path + pathList[i]
    return path

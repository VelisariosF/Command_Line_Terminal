def loadCommandsList(path):
    f = open(path, "r")
    lines = f.readlines()
    tokenizedLines = []
    for line in lines:
        tokenizedLines.append(line.rstrip())
    return tokenizedLines


def constructPreviousPathFromList(pathList):
    delimiter = r'\\'
    path = ""
    for i in range(0, len(pathList) - 1):
        if(i < len(pathList) - 2):
           
           path = path + pathList[i] + delimiter
        else:
           
           path = path + pathList[i]
    return path

def saveCurrentPath(path):
     f = open("currentPath.txt", "w", encoding='utf8')
     f.write(path)
     
    
     f.close()

def loadCurrentPath():
    f = open("currentPath.txt", "r", encoding='utf8')
    currentPath = str(f.readline())
   
    return currentPath

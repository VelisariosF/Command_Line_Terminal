def loadCommandsList(path):
    f = open(path, "r")
    lines = f.readlines()
    tokenizedLines = []
    for line in lines:
        tokenizedLines.append(line.rstrip())
    return tokenizedLines
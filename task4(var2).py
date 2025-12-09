
def unionDict(firstDict, secondDict):
    generalDict = {}
    for f in firstDict.keys():
        if f in generalDict.keys():
            generalDict[f] += firstDict[f]
        else:
            generalDict[f] = firstDict[f]
    
    for s in secondDict.keys():
        if s in generalDict.keys():
            generalDict[s] += secondDict[s]
        else:
            generalDict[s] = secondDict[s]
            
    return generalDict

print(unionDict({"some": 3, "body": 2}, {"every": 4, "body": 6}))
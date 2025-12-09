

def createDict(keyArray, valueArray):
    resultDict = {}
    for key in keyArray:
        resultValueArray = divKey(key, valueArray)
        resultDict[key] = resultValueArray
    return resultDict


def divKey(key, valueArray):
    resultValueArray = []
    for value in valueArray:
        if value % key == 0:
            resultValueArray.append(value)
    return resultValueArray

print(createDict([4, 5, 2, 7, 3], [20, 45, 24, 49, 28, 33, 66]))
        
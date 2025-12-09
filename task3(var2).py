
def task3_1():
    array = []
    while True:
        curVal = int(input("Введите значение: "))
        if curVal != 100:
            array.append(curVal)
        else:
            break
    return array

print(task3_1())

def task3_2(initArray):
    sumArray = []
    for i in range(0, len(initArray)):
        if i == (len(initArray) - 1):
            sum = initArray[i-1] + initArray[0]
            sumArray.append(sum)
        else:
            sum = initArray[i-1] + initArray[i+1]
            sumArray.append(sum)
    return sumArray

# print(task3_2([3, 5, 2, 1, 7]))

def task3_1():
    generalArray = []
    while True:
        curVal = input("Введите подстроку: ")
        if curVal != "end":
            generalArray.append(len(curVal))
        else:
            break

    return generalArray

# print(task3_1())

def task3_2(array):
    loc_max_array = []
    for i in range(0, len(array)):
        if i == (len(array)-1) and array[i] >= array[i-1] >= array[0]:
            loc_max_array.append(i)
        elif i != (len(array)-1) and array[i] >= array[i-1] and array[i] >= array[i+1]:
            loc_max_array.append(i)
    return loc_max_array


print(task3_2([4, 5, 1, 7, 3, 2, 3 , 1, 7 , 2]))

    

        
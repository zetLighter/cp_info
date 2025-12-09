
def some():
    A = int(input("Укажите начало интервала: "))
    B = int(input("Укажите конец интервала: "))

    sum = 0

    for elem in range(A, B+1):
        if elem % 2 == 0:
            sum += elem
    return sum

print(some())


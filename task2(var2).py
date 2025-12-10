
def some(A, B):
    sum = 0

    for elem in range(A, B+1):
        if elem % 2 == 0:
            sum += elem
    return sum

print(some(4, 13))

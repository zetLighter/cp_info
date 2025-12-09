
def some(A, B):
    multiply = 1

    for elem in range(A, B+1):
        if elem % 5 == 0:
            print(elem)
            multiply *= elem
    
    return multiply

print(some(4, 56))
    
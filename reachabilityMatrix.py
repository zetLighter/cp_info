
string1 = input("Введите строку матрицы смежности: ")
columnArray = string1.split()
adjacency_matrix = [None] * len(columnArray)
adjacency_matrix[0] = columnArray
i = 1
while i < len(columnArray):
    string2 = input("Введите строку матрицы смежности: ")
    columnArray_ = string2.split()
    adjacency_matrix[i] = columnArray_
    i += 1

print("Полученная матрица:")
for row in adjacency_matrix:
    print(row)

def get_transposed_matrix(adjacency_matrix):
    transposed_adjacency_matrix = [[0] * len(adjacency_matrix)] * len(adjacency_matrix)
    print(transposed_adjacency_matrix)
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            transposed_adjacency_matrix[j][i] = adjacency_matrix[i][j]
    return transposed_adjacency_matrix


def get_reachability_matrix (adjacency_matrix):
    stringsCount = len(adjacency_matrix)
    # Создаем копию матрицы смежности
    reachability_matrix = adjacency_matrix.copy()
    
    # Добавляем петли (каждая вершина достижима сама из себя)
    for i in range(stringsCount):
        reachability_matrix[stringsCount][stringsCount] = 1
    
    # Алгоритм Уоршелла
    for k in range(stringsCount):
        for i in range(stringsCount):
            for j in range(stringsCount):
                reachability_matrix[i][j] = reachability_matrix[i][j] or (reachability_matrix[i][k] and reachability_matrix[k][j])
    
    return reachability_matrix


def getStrongConectivityMatrix(reachibility_matrix, transposed_reachability_matrix):
    strongConectivityMatrix = [[0] * len(adjacency_matrix)] * len(adjacency_matrix)
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if reachibility_matrix[i][j] == 1 and transposed_reachability_matrix[i][j] == 1:
                strongConectivityMatrix[i][j] = 1
            else:
                strongConectivityMatrix[i][j] = 0

def get_strong_conectivity_components(strongConectivityMatrix):
    visited = [False] * len(strongConectivityMatrix)
    for in range(len(strongConectivityMatrix)):
        if not visited[i]:
            component = [i]
            visited[i] = True

            for j in range(len(strongConectivityMatrix))
            



reachibility_matrix = get_reachability_matrix(adjacency_matrix)
transposed_reachability_matrix = get_transposed_matrix(reachibility_matrix)
strongConectivityMatrix = getStrongConectivityMatrix(reachibility_matrix, transposed_reachability_matrix)

for row in strongConectivityMatrix:
    print(row)
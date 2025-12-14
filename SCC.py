
def get_adjacency_matrix():
    n = int(input("Ведите размерность матрицы: "))
    adjacency_matrix = [[]] * n
    for r in range(n):
        adjacency_matrix[r] = [int(c) for c in (input(f"Введите элементы {n} строки через пробел: ").split())]
    return adjacency_matrix

def strongly_connected_components(adj):
    n = len(adj)
    visited = [False] * n
    order = []

    # 1. DFS для заполнения порядка выхода
    def dfs1(v):
        visited[v] = True
        for u in range(n):
            if adj[v][u] and not visited[u]:
                dfs1(u)
        order.append(v)

    for v in range(n):
        if not visited[v]:
            dfs1(v)

    # 2. Транспонирование матрицы
    adj_t = [[adj[j][i] for j in range(n)] for i in range(n)]

    # 3. DFS по транспонированному графу
    visited = [False] * n
    components = []

    def dfs2(v, comp):
        visited[v] = True
        comp.append(v)
        for u in range(n):
            if adj_t[v][u] and not visited[u]:
                dfs2(u, comp)

    for v in reversed(order):
        if not visited[v]:
            comp = []
            dfs2(v, comp)
            components.append(comp)

    return components


adj_matr = get_adjacency_matrix()

print("Adjacency matrix:")
for r in range(len(adj_matr)):
    print(adj_matr[r])

print(strongly_connected_components(adj_matr))

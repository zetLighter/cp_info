
n, m = [int(i) for i in input("Введите кол-во вершин и кол-во дуг через пробел: ").split()]
visited = [False for i in range(n)]
graph = [[] for i in range(n)]
t_graph = [[] for i in range(n)]
k = 0
tout=[]

print(graph)

def dfs1(v):
    visited[v] = True
    for u in graph[v]:
        if visited[u] is False:
            dfs1(u)
    tout.append(v)
def dfs2(v):
    visited[v] = True
    for u in t_graph[v]:
        if visited[u] is False:
            dfs2(u)

for i in range(m):
    a, b = [int(i) for i in input().split()]
    graph[a].append(b)
    t_graph[b].append(a)

for i in range(n):
    if visited[i] is False:
        dfs1(i)
        print(tout )

visited = [False for i in range(n)]
tout=tout[::-1]
for v in tout:
    if visited[v] is False:
        dfs2(v)
        k+=1
print(k)
from sys import stdin

def bfs(graph, start_node):
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited
    
def dfs(graph, start_node):
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            for i in range(len(graph[node])-1, -1, -1):
                need_visited.insert(0, graph[node][i])
    return visited
    
N, M, V = map(int, stdin.readline().rstrip().split())

graph = dict()
for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    A, B = map(int, stdin.readline().rstrip().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N+1):
    graph[i].sort()
print(' '.join(map(str, dfs(graph, V))))
print(' '.join(map(str, bfs(graph, V)))))

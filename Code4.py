import heapq

def prim(graph, start):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    parent = [-1] * num_vertices
    key = [float('inf')] * num_vertices
    key[start] = 0
    pq = [(0, start)] 

    while pq:
        weight, u = heapq.heappop(pq)

        if selected[u]:
            continue

        selected[u] = True

        for v, edge_weight in graph[u]:
            if not selected[v] and edge_weight < key[v]:
                key[v] = edge_weight
                parent[v] = u
                heapq.heappush(pq, (edge_weight, v))

    return parent, key

def print_mst(graph, parent, key):
    print("Edge \tWeight")
    for i in range(1, len(graph)):
        print(f"{parent[i]} - {i} \t{key[i]}")

graph = [
    [(1, 28), (5, 10)],  # Node 0
    [(0, 28), (2, 16), (6, 14)],  # Node 1
    [(1, 16), (3, 12)],  # Node 2
    [(2, 12), (4, 22), (6, 18)],  # Node 3
    [(3, 22), (5, 25)],  # Node 4
    [(0, 10), (4, 25), (6, 24)],  # Node 5
    [(1, 14), (3, 18), (5, 24)]  # Node 6
]

start_node = 0
parent, key = prim(graph, start_node)
print_mst(graph, parent, key)
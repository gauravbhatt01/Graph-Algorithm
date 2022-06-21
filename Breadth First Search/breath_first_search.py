'''
create a queue
mark v as visited and put v into Q
while Q is non-empty
    remove the head u of Q
    mark and enqueued all (unvisited) neighbors of u
'''

graph = {
    '5' : ['3'],
    '3' : ['4','8'],
    '7' : ['4'],
    '2' : ['7'],
    '4' : ['7','3'],
    '8' : ['3','7']
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end = "")

        for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

print("Following is the Breath-First Search")
bfs(visited, graph, '5')

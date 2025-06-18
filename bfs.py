graph = { 
    'A': ['B', 'C'], 
    'B': ['A', 'C', 'D'], 
    'C': ['A', 'B', 'E'], 
    'D': ['B', 'E'], 
    'E': ['C', 'D'] 
}

# BFS function
def bfs(graph, snode): 
    visitedNodes = []     # Declare inside to reset every run
    queueNodes = []

    visitedNodes.append(snode) 
    queueNodes.append(snode) 
    
    print("\nRESULT :")
    while queueNodes: 
        s = queueNodes.pop(0) 
        print(s, end=" ") 
        
        for neighbour in graph[s]: 
            if neighbour not in visitedNodes: 
                visitedNodes.append(neighbour) 
                queueNodes.append(neighbour)

# Loop to allow multiple runs
while True:
    snode = input("\nEnter Starting Node (A, B, C, D, or E) or 'q' to quit: ").upper()
    if snode == 'Q':
        break
    elif snode in graph:
        bfs(graph, snode)
    else:
        print("Invalid starting node.")

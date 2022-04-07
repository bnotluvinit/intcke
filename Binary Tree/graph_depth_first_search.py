graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')


def dfs_binary_tree(root):
    if root is None:

        return

    else:

        print(root.value, end=" ")

        dfs_binary_tree(root.left)

        dfs_binary_tree(root.right)


def dfs_non_recursive(graph, source):
    if source is None or source not in graph:
        return "Invalid input"

    path = []

    stack = [source]

    while (len(stack) != 0):

        s = stack.pop()

        if s not in path:
            path.append(s)

        if s not in graph:
            # leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)
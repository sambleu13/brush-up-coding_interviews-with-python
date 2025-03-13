from collections import deque

def BFS(tree, root):
    # TODO: implement BFS for the given tree, starting at node `root`
    queue = deque()
    visited = []
    queue.append(root)
    
    # TODO: return the list of tree nodes in the order they were visited
    while queue:
      node = queue.popleft()
      print(node)
      visited.append(node)
      
      for sub in tree[node]:
        if sub not in visited:
          queue.append(sub)
      
    return visited

tree = {
  'computer' : ['printer', 'router'],
  'printer' : ['paper', 'computer'],
  'router' : ['internet', 'computer'],
  'internet' : ['data', 'router'],
  'paper' : ['printer'],
  'data' : ['internet'],
}

print(BFS(tree, 'computer')) # Change 'computer' to starting node of your choice

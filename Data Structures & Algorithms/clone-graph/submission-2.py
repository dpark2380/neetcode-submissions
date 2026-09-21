"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    clones = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.clones = {}
        return self.dfs(node)
        
    
    def dfs(self, node):
        # If the node is none, then we simple return the node. 
        if node is None:
            return node

        # If a clone of the node already exists, return the clone.
        if node in self.clones:
            return self.clones[node]
        
        # Initialising the clone of the current node. 
        self.clones[node] = Node(node.val)

        # Adding the neighbor nodes. 
        for n in node.neighbors:
            # Clone of neighbor
            nclone = self.dfs(n)
            # Appending clone of neighbor
            self.clones[node].neighbors.append(nclone)
        
        return self.clones[node]


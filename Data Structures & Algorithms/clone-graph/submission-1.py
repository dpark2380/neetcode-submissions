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
        if node is None:
            return node
        if node in self.clones:
            return self.clones[node]
        
        self.clones[node] = Node(node.val)

        for n in node.neighbors:
            self.clones[node].neighbors.append(self.dfs(n))
        
        return self.clones[node]


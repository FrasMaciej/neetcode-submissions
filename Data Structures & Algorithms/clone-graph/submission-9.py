"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import copy

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:        
        old_to_new = {}
        def dfs(cur_node):
            if cur_node in old_to_new:
                return old_to_new[cur_node]
            
            copy_node = Node(cur_node.val)
            old_to_new[cur_node] = copy_node
            for neigh in cur_node.neighbors:
                copy_node.neighbors.append(dfs(neigh))
            
            return copy_node


        
        return dfs(node) if node else None



        

        
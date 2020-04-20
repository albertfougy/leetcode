"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    """ Breadth First Search with Queue """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        else:
			queue = [node]
			root = Node(node.val, [])
			hashMap = {}
			hashMap[node] = root
			while (len(queue) !=0):
				curr = queue.pop(0)
				for i in curr.neighbors:
					if i not in hashMap:
						newNode = Node(i.val, [])
						hashMap[i] = newNode
						queue.append(i)
					hashMap[curr].neighbors.append(hashMap[i])
            return root

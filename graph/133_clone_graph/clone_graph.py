# 133. Clone a Graph
# 

# Python 3
# A Pythonic Detailed step-by-step explanation in BFS (below)
# https://www.youtube.com/watch?v=Jx3Cz_A60Oc&t=256s

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
        # case when graph is empty
        # return None
        if node == None:
            return None

        # initialize queue with reference node: node
        queue = [node]
        # create root node (reference node)
        root = Node(node.val, [])
        # initialize hashMap ( Dictionary in Python )
        hashMap = {}
        # put the root in hashMap
        hashMap[node] = root
        # bfs continue as long as queue is not empty
        while (len(queue) !=0):
            # take current element form queue
            curr = queue.pop(0)
            # iterate neighbors
            for i in curr.neighbors:
                # check if neighbor is in hashMap. if neighbor is not in hashMap
                if i not in hashMap:
                    # create node(neighbor)
                    newNode = Node(i.val, [])
                    # add node to hashmap key is value, and value is the node(neighbor)
                    hashMap[i] = newNode
                    # append original neighbor node to queue
                    queue.append(i)
                # add the neighbor node to current node.neighbors
                hashMap[curr].neighbors.append(hashMap[i])
        return root



# Python3
# Depth First Search with Stack
# Just use DFS approach by help from a stack for running through entire graph.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

# Python3
# Depth First Search with Recursion
# Use call stack for DFS approach. This one is cleaner and more beautiful.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])


# Detailed explanation on YouTube in Java
# https://www.youtube.com/watch?v=e5tNvT1iUXs

# Understanding Graph Algorithms with Breadth First & Depth First
# https://www.youtube.com/watch?v=bIA8HEEUxZI

# ---

# The dictionary (or HashTable) is just used to keep the nodes that we have cloned already.

# How would you clone a graph if it has multiple edges and no cycles?

# This algorithm works in that example, as long as we can reach all the nodes from the original node.
# If we are guaranteed that there is no cycles, then the dictionary (Map) is not necessary.

# What about different color edges?
# The given class UndirectedGraphNode keeps all the neighbors identically, 
# If it had several lists one for each color, then the algorithm would be nearly identical, 
# having to replicate the traversing the neighbors for each color.



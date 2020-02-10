# Breadth First Search

# Clone an undirected graph. Each node in the graph contains a label and a list 
# of its neighbors.

# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# We use "#" as a separator for each node, and , as a separator for node label 
# and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# The graph has a total of three nodes, and therefore contains three parts as 
# separated by "#".
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a 
# self-cycle.

# Visually, the graph looks like the following:
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

# ---

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodeMap = {}
        return self.cloneNode(node, nodeMap)
    
    def cloneNode(self, node, nodeMap):
        if node == None:
            return None
        if node.label in nodeMap:
            return nodeMap[node.label]
        newNode = UndirectedGraphNode(node.label)
        nodeMap[node.label] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.cloneNode(neighbor, nodeMap))
        return newNode

# The dictionary (or HashTable) is just used to keep the nodes that we have cloned already.

# How would you clone a graph if it has multiple edges and no cycles?

# This algorithm works in that example, as long as we can reach all the nodes from the original node.
# If we are guaranteed that there is no cycles, then the dictionary (Map) is not necessary.

# What about different color edges?
# The given class UndirectedGraphNode keeps all the neighbors identically, 
# If it had several lists one for each color, then the algorithm would be nearly identical, 
# having to replicate the traversing the neighbors for each color.



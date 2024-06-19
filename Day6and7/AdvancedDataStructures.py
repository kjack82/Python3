## HEAPS 

# A Heap is a tree like data structure using heapq module. Classified as a binary tree. 

import heapq
# Instantiate a Heap
H = [21,1,45,78,3,5]
# Covert the list into a Heap
heapq.heapify(H)
print("Heap : "+str(H))  ##prints Heap : [1, 3, 5, 78, 21, 45]

# In this code, you initialise a list 'H' with some values. Using the 'heapify' function from heapq, the list is transformed into a heap.


## GRAPHS 

# Complex data structure containing an ordered, finite set of vertices and edges connecting them. 
# Python uses adjacency lst representation to implement a graph
# Used to vidualise relationships. Each vertex prepresents an object and each edge speaks to the relationship between them. 

## example

# For instance, in a social network, each person could be represented as a vertex, and if they are friends, there would be an edge connecting the two vertices. 
# So, if Tom is friends with Jerry, in the graph data structure, Tom and Jerry would be two vertices with an edge in between.
# There are undirected graphs, where edges don't have a direction, indicating that the relationship is two-way. Then, there are directed graphs or 'digraphs', 
# where each edge has a direction, signifying a one-way relationship.

# Key terms for graphs

# Vertex: A single node in the graph data structure.
# Edge: The connection or relationship between any two vertices.
# Adjacent Vertices: Two vertices connected by an edge.
# Degree of a Vertex: The total number of edges connected to a vertex.
# Path: A sequence of vertices where each adjacent pair is connected by an edge.

## HASH TABLES 

# A Hash Table is a data structure that implements an associative array abstract data type, a structure which can map keys to values.
# Two primary use cases for hash tables, data retrieval and data insertion. 

# Data Retrieval: Hash Tables are known for their phenomenal speed in data retrieval. Given the key, the value can be retrieved in O(1) time complexity.
# Data Insertion: Similar to data retrieval, data insertion in a Hash Table is also O(1). This is because it directly places the data at the address 
# calculated by the hashing function.

# Key components of a hash table
# A hash table consists of several major components:
# Key: The unique identifier with which data is associated.
# Value: The data which is stored and retrieved.
# Hash Function: A function that computes an index into an array of slots, from which the desired value can be fetched.
# Collisions: When two keys hash to the same index.
# Load factor: A measure that decides when to resize the hashtable.

 ####
 
## there are others too. 
 
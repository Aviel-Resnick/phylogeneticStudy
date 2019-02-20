''' Prim’s algorithm on a distance matrix:
1. Choose any vertex to start.
2. Delete the row in the matrix for the chosen vertex.
3. Number the column in the matrix for the chosen vertex.
4. Put a ring round the lowest undeleted entry in any of the numbered columns (if there is more than one lowest entry, choose any).
5. The ringed entry becomes the next arc to be added to the tree.
6. Repeat steps 2, 3, 4 and 5 until all rows are deleted.
'''

sampleMatrix = [[0.0, 761, 731, 756, 747, 750, 245, 318, 314], [761, 0.0, 628, 365, 616, 678, 765, 765, 772], [731, 628, 0.0, 630, 625, 667, 742, 736, 743], [756, 365, 630, 0.0, 615, 667, 755, 745, 748], [747, 616, 625, 615, 0.0, 647, 750, 739, 751], [750, 678, 667, 667, 647, 0.0, 751, 733, 740], [245, 765, 742, 755, 750, 751, 0.0, 325, 321], [318, 765, 736, 745, 739, 733, 325, 0.0, 253], [314, 772, 743, 748, 751, 740, 321, 253, 0.0]]

import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1,self.V):
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        #Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1 # First node is always the root

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u

        self.printMST(parent)

g = Graph(9)
g.graph = sampleMatrix

g.primMST();

# Contributed by Divyanshu Mehta

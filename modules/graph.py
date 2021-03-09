import math

# A class that supports adding (x,y) coords one at a time via addPoint(),
# then using those to find a minimum spanning tree
class Graph:

    def __init__(self):
        #x,y coords of the points
        self.points = []
        #this will be the actual adjacency matrix with weight values
        self.weights = []

    #add a point to the points array, does not update adjacency matrix
    def addPoint (self, x, y):
        self.points.append([x, y])

    #print all the points (x,y) in the object
    def printPoints(self):
        print("Points in set: ")
        for i in range(len(self.points)):
            print(self.points[i])

    #find the distance between two (x, y) point values
    def findDistance(self, point1, point2):
        #Pythagorean theorum between the two points
        dist = math.sqrt(((self.points[point1][0] - self.points[point2][0]) ** 2 )+ ((self.points[point1][1] - self.points[point2][1]) ** 2 ))
        #round to nearest int before returning
        return round(dist)

    #fill in the adjacency matrix with weight values
    def calculateWeights(self):
        for i in range(len(self.points)):
            #For each row, append another row
            self.weights.append([])

            #calculate the distance between every point
            for j in range(len(self.points)):
                self.weights[i].append(self.findDistance(i, j))

        #testing purposes
        #print("Calculated Weights: ")
        #print(self.weights)   

    #Utility to find the minimum key that is not already in the MST
    #Returns the index in keys[] of the vert
    def minWeight(self, keys):
        #init min
        min = float('inf')
        minIndex = -1

        #loop thru all and find min
        for i in range(len(keys)):
            if keys[i] < min and keys[i] >= 0:
                minIndex = i
                min = keys[i]

        return minIndex


    #updates the key for every verticy in the graph, based on its distance from previous added. 
    # since graph is complete always do all of them. Ignores keys that are already included
    def updateKeys(self, keys, lastIncludedVert):
        for i in range(len(keys)):
            #ignore negitive keys, as they are already in MST
            if keys[i] >= 0:
                    #find dist from last included vert
                    keys[i] = self.weights[lastIncludedVert][i]


    #find the minimum spanning tree given the current (x,y) points in the object
    def calculateMST(self):
        #Fill in weights before proceeding
        self.calculateWeights()

        #keep track of the total MST weight
        totalWeight = 0
        lastVert = 0

        #start with all keys as infinity, except the first one as zero 
        keys = [float('inf')] * len(self.points)
        keys[0] = 0

        #loop enough times to include all verticies
        for i in range(len(self.points)):
            if i > 0:
                lastVert = minWeightVertex
            minWeightVertex = self.minWeight(keys)
            print("Added: ", self.points[lastVert], " - ", self.points[minWeightVertex], " which adds: ", keys[minWeightVertex], " to MST.")
            totalWeight += keys[minWeightVertex]

            #update adjacent (so all) verticies, set prev one to an invalid state
            keys[minWeightVertex] = -1
            self.updateKeys(keys, minWeightVertex)

        print("Total Weight of the MST: ", totalWeight)
        
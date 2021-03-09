from modules import util
from modules import graph
        
# NOTE: This is driver code only. For the actual MST implimentation, check
# the modules folder

# Read in the data from graph.txt into a 2D array
data = util.readFile()

#keep track of how many lines of data have been read
lineInData = 0

# For each test case, make a graph and run MST algo
for i in range(data[0][0]):
    # create Graph instance
    print("\nData Set: ", i + 1)
    currentGraph = graph.Graph()
    lineInData += 1
    
    # Add all the individual points
    for j in range((data[lineInData][0])):
        lineInData += 1
        currentGraph.addPoint(data[lineInData][0], data[lineInData][1])
    
    # Call Graph method to calculate MST
    currentGraph.calculateMST()





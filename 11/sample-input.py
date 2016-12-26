from solver import *

# The start state (equivalent to a set of grid coordinates in other dijkstra)
start = Node(elevator = 1, locations = {'h': (2, 1), 'l': (3, 1)}, distance = 0)

test  = Node(elevator = 2, locations = {'h': (3, 1), 'l': (2, 2)})

# The goal state where everything is on the fourth floor
goal  = Node(elevator = 4, locations = {'h': (4, 4),  'l': (4, 4)})


# Make the real call to solve the problem
print(solve(start, goal))

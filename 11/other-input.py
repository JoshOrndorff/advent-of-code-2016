from solver import *

# The start state
start = Node(elevator = 1,
             locations = {'u': (2, 3),
                          'r': (2, 3),
                          'l': (2, 3),
                          'c': (2, 3),
                          'p': (1, 1)},
             distance = 0)


# The goal state where everything is on the fourth floor
goal = Node(elevator = 4,
            locations = {'u': (4, 4),  # Order is (generator, microchip)
                         'r': (4, 4),  # Floors are 1-indexed
                         'l': (4, 4),
                         'c': (4, 4),
                         'p': (4, 4)})



# Make the real call to solve the problem
print(solve(start, goal))




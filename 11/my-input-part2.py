from solver import *

# The start state
start = Node(elevator = 1,
             locations = {'d': (1, 1),
                          'e': (1, 1),
                          'r': (2, 2),
                          't': (2, 3),
                          's': (1, 1),
                          'c': (2, 2),
                          'p': (1, 1)},
             distance = 0)


# The goal state where everything is on the fourth floor
goal = Node(elevator = 4,
            locations = {'d': (4, 4),
                         'e': (4, 4),
                         'r': (4, 4),  # Order is (generator, microchip)
                         't': (4, 4),  # Floors are 1-indexed
                         's': (4, 4),
                         'c': (4, 4),
                         'p': (4, 4)})



# Make the real call to solve the problem
print(solve(start, goal))



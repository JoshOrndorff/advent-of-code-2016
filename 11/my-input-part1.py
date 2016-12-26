from solver import *

# The start state
start = Node(elevator = 1,
             locations = {'r': (2, 2),  # Order is (generator, microchip)
                          't': (2, 3),  # Floors are 1-indexed
                          's': (1, 1),
                          'c': (2, 2),
                          'p': (1, 1)},
             distance = 0)


# The goal state where everything is on the fourth floor
goal = Node(elevator = 4,
            locations = {'r': (4, 4),  # Order is (generator, microchip)
                         't': (4, 4),  # Floors are 1-indexed
                         's': (4, 4),
                         'c': (4, 4),
                         'p': (4, 4)})



# Make the real call to solve the problem
print(solve(start, goal))



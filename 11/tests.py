from solver import *


#########################
# Tests for valid nodes #
#########################

print("\nThese nodes should all be VALID.")
n = Node(elevator = 4,
            locations = {'c': (3, 3), # All paired perfectly
                         's': (4, 4),
                         'r': (4, 4),
                         't': (4, 4),
                         'p': (3, 3)})
print(n.is_valid())

###############

n = Node(elevator = 2,
            locations = {'c': (3, 3),
                         's': (3, 3),
                         'r': (3, 4), # All chips on 3 are paired, so safe
                         't': (2, 4), # Unpaired chips are on floor 4 without any generators
                         'p': (3, 3)})
print(n.is_valid())

###############

n = Node(elevator = 1,
            locations = {'c': (1, 3), # All generators are stashed on 1, chips are elsewhere
                         's': (1, 4),
                         'r': (1, 4),
                         't': (1, 4),
                         'p': (1, 3)})
print(n.is_valid())

###############

n = Node(elevator = 4,
            locations = {'c': (3, 1), # A chip on every floor
                         's': (4, 1),
                         'r': (4, 2),
                         't': (4, 4),
                         'p': (3, 3)})
print(n.is_valid())

###############

n = Node(elevator = 4,
            locations = {'c': (1, 1), # A generator on every floor
                         's': (2, 2), # Only way to make it valid to to pair every chip
                         'r': (2, 2),
                         't': (4, 4),
                         'p': (3, 3)})
print(n.is_valid())

###############


###########################
# Tests for invalid nodes #
###########################

print("\nThese nodes should all be INVALID.")

n = Node(elevator = 3,
             locations = {'c': (3, 3),
                          's': (4, 4),
                          'r': (3, 4), # Invalid because r chip is irradiated by s and t generators
                          't': (4, 4),
                          'p': (3, 3)})
print(n.is_valid())



###########################
# Tests for get_neighbors #
###########################
print("\n\n\n")
n = Node(elevator = 4,
         locations = {'p': (4, 4),
                      'c': (4, 4),
                      'r': (3, 3),
                      's': (3, 2),
                      't': (4, 4)})
print("\nNode under test: {}".format(n))
print_nodes(n.get_neighbors()) 


n = Node(elevator = 1, # My starting node
         locations = {'r': (2, 2),
                      't': (2, 3),
                      's': (1, 1),
                      'c': (2, 2),
                      'p': (1, 1)})
                      
print("\nNode under test: {}".format(n))
print_nodes(n.get_neighbors()) 

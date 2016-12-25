
# This class (for hashing) thanks to: http://stackoverflow.com/a/9997347/4184410
class Node(object):
  
  def __init__(self, elevator, locations, distance = None):
    
    self.distance = distance
    self.elevator = elevator
    self.locations = locations
  
  def get_neighbors(self):
    """ Returns all valid neighbors of this state. """
    
    # Figure out all the things that can be taken
    items = []
    
    for element in elements:
      if self.locations[element][0] == self.elevator:
        items.append(element + 'g')
      if self.locations[element][1] == self.elevator:
        items.append(element + 'm')
    
    # Generate all possible payload sets
    payloads = []
    
    # First choose the one required item
    for firstItem in items:
      # Now choose the optional second item
      for secondItem in items:
        # The same item can't be taken twice; let that mean only one item goes.
        if secondItem == firstItem and set((firstItem,)) not in payloads:
          payloads.append(set((firstItem,)))
        elif set((firstItem, secondItem)) not in payloads:
          payloads.append(set((firstItem, secondItem)))
    
    # Now build the actual states
    neighbors = []
    for destination in (self.elevator - 1, self.elevator + 1):
    
      # If this isn't a valid floor, bail out
      if destination < 1 or destination > 4:
        continue
      
      for payload in payloads:
        
        # Build up new state node one element at a time (handle elevator manually)
        newLocations = {}
        for element in elements:
          newLocations[element] = (destination if element + 'g' in payload else self.locations[element][0],
                                   destination if element + 'm' in payload else self.locations[element][1])
        
        neighbor = Node(destination, newLocations)
        if neighbor.is_valid():
          neighbors.append(neighbor)
        
    return neighbors
    
  
  
  def is_valid(self):
    """ Returns whether this state follows protocol (is legal). """
    
    # Setup the containers for vaulnerable chips and dangerous generators
    soloChips = []
    gens  = []
    
    # Loop through each element finding separated chips and generators
    for elem, floors in self.locations.items():
      
      if floors[0] != floors[1]:
        soloChips.append(floors[1])
      gens.append(floors[0])
    
    # If there is any overlap, this state isn't valid
    return not any(gen in soloChips for gen in gens)
  
  
  
  def __str__(self):
    return "Elev: " + str(self.elevator) + "  Dist: " + str(self.distance) + '  ' + str(self.locations)
  
  def __eq__(self, other):
    return self.key() == other.key()
  
  # I can't believe forgetting to implement this led to a bug for so long.
  def __ne__(self, other):
    return not self == other
  
  # Someone recommended calling this __key(), but I'm not for debugging purposes
  def key(self):
    return (self.elevator, tuple(sorted(set(self.locations.values()))))
  
  def __hash__(self):
    return hash(self.key())
 


def print_nodes(nodes):
  """ Debugging helper to print any iterable of nodes. """
  
  for node in nodes:
    print(str(node))



############### My real data

# The start state (equivalent to a set of grid coordinates in other dijkstra)
start = Node(elevator = 1,
             locations = {'r': (2, 2),  # Order is (generator, microchip)
                          't': (2, 3),  # Floors are 1-indexed
                          's': (1, 1),
                          'c': (2, 2),
                          'p': (1, 1)},
             distance = 0)

# Some test nodes
test1 = Node(elevator = 4,
            locations = {'c': (3, 3),
                         's': (4, 4),
                         'r': (4, 4),
                         't': (4, 4),
                         'p': (3, 3)})

test2 = Node(elevator = 3,
             locations = {'c': (3, 3),
                          's': (4, 4),
                          'r': (3, 4),
                          't': (4, 4),
                          'p': (3, 3)})

# The goal state where everything is on the fourth floor
goal = Node(elevator = 4,
            locations = {'r': (4, 4),  # Order is (generator, microchip)
                         't': (4, 4),  # Floors are 1-indexed
                         's': (4, 4),
                         'c': (4, 4),
                         'p': (4, 4)})

elements = ('r', 't', 's', 'c', 'p')

###########

########### Other user's input

#TODO maybe

###########

########### Sample data
'''
# The start state (equivalent to a set of grid coordinates in other dijkstra)
start = Node(elevator = 1, locations = {'h': (2, 1), 'l': (3, 1)}, distance = 0)

test = Node(elevator = 2, locations = {'h': (3, 1), 'l': (2, 2)})

# The goal state where everything is on the fourth floor
goal = Node(elevator = 4, locations = {'h': (4, 4),  'l': (4, 4)})

elements = ('h', 'l')
'''
############

# The two sets
openSet = set([start])
closedSet = set()








############## Main Program ####################

print("Are start, test, and goal nodes valid?")
print(start.is_valid())
print(test1.is_valid())
print(test2.is_valid())
print(goal.is_valid())


print("\nNow starting real run.\n\n")


# Keep searching until we find a path (which will certainly be shortest) to goal
current = start
count = 0
while current != goal:
  
  # Check out each new neighbor
  for neighbor in current.get_neighbors():
  
    # Did we find a new node?
    if neighbor not in openSet and neighbor not in closedSet:
      neighbor.distance = current.distance + 1
      openSet.add(neighbor)

  # Count this node explored
  closedSet.add(current)
  openSet.remove(current)

  # Debugging info
  #print("Checking node: {}".format(str(current)))
  #print("closed set ({} items)".format(len(closedSet)))
  #print("open set ({} items):".format(len(openSet)))
  #print_nodes(openSet)
  #if raw_input() == "debug":
  #  import ipdb;ipdb.set_trace()
  count += 1
  print(count)

  # Grab the most promising unexplored node for next time through the loop
  current = min(openSet, key = lambda node: node.distance)
  

# Print final result
print(current.distance)


# My program runs out of possibilities after 30 so I guessed 30.
# 30 is too low, so I guess that means I not finding all neighbors?




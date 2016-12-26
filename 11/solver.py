class Node(object):
  
  def __init__(self, elevator, locations, distance = None):
    
    self.distance = distance
    self.elevator = elevator
    self.locations = locations
  
  def get_neighbors(self):
    """ Returns all valid neighbors of this state. """
    
    # Figure out all the things that can be taken
    items = []
    
    for element in self.locations:
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
        for element in self.locations:
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
  
  def __ne__(self, other):
    return not self == other
  
  # Someone recommended calling this __key(), but I'm not for debugging purposes
  def key(self):
    return (self.elevator, tuple(sorted(self.locations.values())))
  
  def __hash__(self):
    return hash(self.key())
 


def print_nodes(nodes):
  """ Debugging helper to print any iterable of nodes. """
  
  for node in nodes:
    print(str(node))



def solve(start, goal):
  """ Solves the chips and generators problem given starting and goal nodes. """
  
  # Declare the two sets
  openSet = set([start])
  closedSet = set()


  # Keep searching until we find a path (which will certainly be shortest) to goal
  current = start
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

    # Grab the most promising unexplored node for next time through the loop
    current = min(openSet, key = lambda node: node.distance)
  
  return current.distance






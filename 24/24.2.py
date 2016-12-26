class POI(object):
  """ Class to represent a point of interest (a numbered spot) in the original
      graph. These are the nodes in the second phase path-finding algorithm. """
      
  def __init__(self, coords, name):
    
    # A 2-tuple representing the x, y coordinates in the original graph
    # I may not end up needing these.
    self.coords = coords
    self.name = name # The special number given to the spot
                     # This is actually also a way to identify the start node.
    
    # When the poi is made, neighbors are not known. They're added later.
    # Key:value pairs are POI: distance
    self.neighbors = {}
  
  def __str__(self):
    """ Printing the POI nicely is helpful for debugging. """
    
    text = "\nPOI {} (coordinates: {})".format(self.name, self.coords)
    
    return text



class State(object):
  """ Class to represent the state of a path head in the second phase path-find.
      It consists of the point at which the walker is currently standing, and
      the points of interest that are yet to be visited. """
  
  def __init__(self, loc, toSee, dist):
    # The current path head (where the walker is standing)
    self.loc = loc
    
    # POIs that have not been visited on this path
    self.toSee = toSee
    
    # The distance traveled so far
    self.dist = dist
  
  
  def __str__(self):
    """ Printing the State nicely is helpful for debugging. """
    
    text = "\nStanding at {}. Distance traveled: {}".format(self.loc, self.dist)
    
    text += "\nYet to see: "
    
    for poi in self.toSee:
      text +=  poi.name + ' '
    
    return text
  
  
  
  def key(self):
    return (self.loc.name, self.dist, tuple(sorted(self.toSee)))
  
  def __hash__(self):
    return hash(self.key())
  
  def __eq__(self, other):
    return self.key() == other.key()
  
  def __ne__(self, other):
    # I don't think I even use this, but it was such a hard-to-find bug
    # during the day 11 problem, I don't want to risk missing it again.
    return not self == other



def find_path(start, goal, maze):
  """ A breadth first search to find the shortest path from start to goal.
      This is the phase-one path-find to link the POIs.
      
      This algorithm terminates a path when it passes through another poi to
      as an optimization that attempts to reduce the number of neighbors in
      the phase-two graph. It may sometimes just find a less ideal path, but
      that's okay. """
  
  openSet = {start: 0}
  closedSet = {}
  
  current = start
  
  # Search until we reach the goal
  while current != goal:
    
    neighbors = [(current[0] + 1, current[1]), # Right
                 (current[0] - 1, current[1]), # Left
                 (current[0], current[1] + 1), # Up
                 (current[0], current[1] - 1)] # Down
    
    # Check out all the neighbors
    for neighbor in neighbors:
      
      # If the neighbor is valid, and new, add it to the open set
      if maze[neighbor[1]][neighbor[0]] != '#' and neighbor not in closedSet:
        openSet[neighbor] = openSet[current] + 1
    
    # Mark this as explored
    closedSet[current] = openSet[current]
    del openSet[current]
    
    # Grab next location
    current = min(openSet, key = lambda node: openSet[node])
  
  # Return the result
  return openSet[current]



############### Main Program ###############

# A set that will hold POI objects
# A separate reference to to the starting poi will be stored later below
pois = set()

# Parse the input into a 2D list and make the POI instances
with open("input.txt", 'r') as f:
  
  maze = []
  y = 0
  for line in f:
  
    row = []
    x = 0
    for char in line:
    
      # The newlines are useless, just skip them
      if char == '\n':
        continue
      
      # Put the location into the maze row
      row.append(char)
      
      # If it's a POI, make the object, and store the reference
      if char in "01234567": # My particular puzzle only had thses POIs
        poi = POI((x, y), char)
        pois.add(poi)
        
        # A special reference to the starting POI
        if char == '0':
          poi0 = poi
      
      x += 1
    
    maze.append(row)
    y += 1

# This is the set of phase 1 searches
# Discover the neighbors and distances for each POI
for start in pois:
  
  for end in pois:
    
    # Paths that start and end in the same place aren't helpful here
    if start == end:
      continue
    
    # Don't find the path forward if it was already found backward
    if start in end.neighbors:
      continue
    
    # Find the path and link the nodes in both directions
    dist = find_path(start.coords, end.coords, maze)
    start.neighbors[end] = dist
    end.neighbors[start] = dist

######### Below is the phase-two search
state0 = State(loc = poi0,
               toSee = pois,
               dist = 0)

p2open = set([state0])
p2closed = set()

current = state0

# Keep searching as long as we haven't see all the POIs AND returned to start
while current.loc != poi0 or len(current.toSee) > 0:
  
  # Explore all the neighbors
  for neighbor in current.toSee:
    
    # Since we need to end in the same place we start, it's possible that the
    # Current location is still in the toSee set. Just skip those.
    if current.loc == neighbor:
      continue
    
    newState = State(loc = neighbor,
                     toSee = current.toSee - set([neighbor]),
                     dist = current.dist + current.loc.neighbors[neighbor])
    
    # If the new state is not already explored, add it to the open set
    if newState not in p2closed:
      p2open.add(newState)
  
  # Mark this state as explored
  p2closed.add(current)
  p2open.remove(current)
  
  # Grab the next state
  current = min(p2open, key = lambda node: node.dist)

# Finished the phase-2 search, so print the final result
print(current.dist)









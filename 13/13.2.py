# Office designer's favorite number; my puzzle input
favNum = 1364

# Given Special Coordinates
start = (1, 1)

# Two sets of nodes and their best known path distances
openSet  = {start: 0}
closedSet = {}

def is_open(node):
  """ Returns boolean whether a given cell can be walked on. """
  
  x, y = node
  
  # Make sure the coordinates are positive or else they are outside the building
  if x < 0 or y < 0:
    return False
  
  z = x * x + 3 * x + 2 * x * y + y + y * y + favNum
  
  setBits = 0
  while z > 0:
    if z % 2 == 1:
      setBits += 1
    z = z // 2
  
  return setBits % 2 == 0



def get_neighbors(node):
  """ Returns all valid neighbors of a node. """
  
  candidates = [(node[0] - 1, node[1]),
                (node[0] + 1, node[1]),
                (node[0], node[1] - 1),
                (node[0], node[1] + 1)]
  
  neighbors = []
  
  for candidate in candidates:
    if is_open(candidate):
      neighbors.append(candidate)
    
  return neighbors
      
    
def print_board(current):
  for i in range(45):
    for j in range(45):
      if (i, j) == goal:
        char = 'M'
      elif is_open((i,j)):
        char = ' '
      else:
        char = '#'
      
      print char,
    print



############ Main Program #########

# Keep searching until no more paths are yet to be explored
while len(openSet) > 0:

  # Grab the most promising unexplored node for next time through the loop
  current = min(openSet, key = lambda node: openSet[node])
  
  # Debugging info
  #print("Checking node: {}".format(current))
  #print("Unique nodes checked: {}".format(len(closedSet)))
  #raw_input("open set: {}\n\n".format(openSet))
  
  # Check out each new neighbor
  for neighbor in get_neighbors(current):
  
    # Did we find a shorter path to a known node?
    # Is it fewer than 50 steps away?
    if neighbor not in openSet and neighbor not in closedSet and openSet[current] < 50:
      openSet[neighbor] = openSet[current] + 1

  # Count this node explored
  closedSet[current] = openSet[current]
  del openSet[current]
  

# Print final result
print(len(closedSet))











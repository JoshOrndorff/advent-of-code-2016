class Server(object):
  
  def __init__(self, size, used):
    self.size = size
    self.used = used
    self.goal = False
  
  def get_used(self):
    return sum(self.data)
    
  def get_free(self):
    return self.total - self.used
  
  def get_percent(self):
    return float(used) / total
  
  def char(self):
    """ Return the symbolic character used to represent this node according
        to the example givin on the problem page. """
    
    if self.goal:
      return'G'
    
    if self.used == 0:
      return '_'
    
    if self.used < 100:
      return '.'
    
    return '#'
    
    


################ Main Program ######################

# Setup a grid to hold the server nodes (Assume my dimensions)
servers = [[None for x in range(32)] for y in range(30)]

# Parse the file
with open("input.txt", 'r') as f:
  # Skip the first two lines because they are headers
  f.next()
  f.next()
  for line in f:
    # Parse an individual server
    x = int(line[line.index('x') + 1: line.rindex('-')]) # x to last dash
    y = int(line[line.index('y') + 1: line.index(' ')]) # y to first space
    size = int(line[24:27])
    used = int(line[30:33])
    
    # Add that server to the list
    servers[y][x] = Server(size, used)

# Set the goal node
servers[0][31].goal = True

# Print the grid
for row in servers:
  line = ""
  for server in row:
    line += ' ' + server.char()
  print(line)
  
# Sketch of algorithm to solve automatically
# Find path from start to finish  that doesn't go through walls (in my case that's straight across the top.
# Repeat until goal data is at finish:
  # Find path from current blank to desired blank
  # Move goal data into blank

'''
To get empty in right spot:
2 left
22 up
6 right
Cycling the goal left one and keeping the empty spot ahead of it takes 5 moves
Do that 30 times to get goal one spot away
1 Final move left
'''


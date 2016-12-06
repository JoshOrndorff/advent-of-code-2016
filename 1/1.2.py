
# Take the input and processes it down
directions = "R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1"
directions = directions.replace(' ','')
directions = directions.split(',')

# Make a (nearly) empty list of pairs corresponding to coordinates crossed.
path = [(0,0)]

# Start facing North
facing = 0

# Initialize a variable for the first duplicate.
firstDupe = None

# Loop through each direction and process it
for direction in directions:
  lastLocation = path[-1]
  turn = direction[0]
  distance = int(direction[1:])
  
  # Figure out which way we are facing
  if turn == "R":
    facing = (facing + 1) % 4
  else:
    facing = (facing - 1) % 4
  
  # Now walk the right distance
  newX = 0
  newY = 0
  for i in range(distance):
    if facing == 0: #North
      newY += 1
    elif facing == 1:
      newX += 1
    elif facing == 2:
      newY -= 1
    else:
      newX -= 1
    
    # Check whether we've been here before, and if so we're done.
    newLocation = (lastLocation[0] + newX, lastLocation[1] + newY)
    if newLocation in path and firstDupe is None:
      firstDupe = newLocation
    path.append(newLocation)
    
# Find the total block distance to the first repeated location
finalDistance = abs(firstDupe[0]) + abs(firstDupe[1])
print(finalDistance)
  
  
  
  
  
  

def calc_tile(lcr):
  """ Calulates one new tile given the left, center, and right tiles. """
  
  # Just manually test all the trap conditions given
  if lcr == '^^.' or lcr == '.^^' or lcr == '^..' or lcr == '..^':
    return '^'
    
  # If none of those were men, this tile is safe
  return '.'

def next_row(prev):
  """ Caluclates and returns the next row of tiles given the previous row. """
  
  # Build up next row one tile at a time
  next = ""
  
  # Handle the first tile manually becuase it has a special left
  next += calc_tile('.' + prev[:2])
  
  # Handle most tiles systematically
  for i in range(len(prev) - 2):
    next += calc_tile(prev[i: i + 3])
  
  # Handle the last tile manually because it has a special right
  next += calc_tile(prev[-2:] + '.')
  
  # All done
  return next



########### Main Program #################

# Setup a list of rows and read in the first row
floor = []
with open("input.txt", 'r') as f:
  floor.append(f.read()[:-1])

# Loop through generating the required number of rows
while len(floor) < 40:
  floor.append(next_row(floor[-1]))

# Count the total number of safe tiles and print the result.
safe = 0
for row in floor:
  for tile in row:
    if tile == '.':
      safe += 1
print(safe)

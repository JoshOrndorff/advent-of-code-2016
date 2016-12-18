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

# Read in the first row
with open("input.txt", 'r') as f:
  row = f.read()[:-1]
  
# Setup a safe tile counter and count the safe tiles in the first row
safe = 0
for tile in row:
  if tile == '.':
    safe += 1

# Loop through generating the required number of rows
rows = 1 # Start at 1 because we've manually handled the first row already.
while rows < 400000:
  row = next_row(row)
  for tile in row:
    if tile == '.':
      safe += 1
  rows += 1

# Print the final result
print(safe)

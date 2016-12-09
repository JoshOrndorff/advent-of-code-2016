# Module level variable to represent the screen
screen = []

def rect(a, b):
  """ Performs the rect operation on the screen. """
  for i in range(b):
    for j in range(a):
      screen[i][j] = True
  
  
def rotate_row(y, by):
  """ Rotates a row in the screen. """
  
  row = screen[y]
  newRow = []
  
  # Loop through the new row putting in values from the old row
  for i in range(len(row)):
    newRow.append(row[(i - by) % len(row)])
  
  # Reassign the reference in screen to the new row
  screen[y] = newRow
  
  
def rotate_column(x, by):
  """ Rotates a column in the screen. """
  
  newCol = []
  
  # Loop through the column putting in values from the old column
  for i in range(len(screen)):
    newCol.append(screen[i - by][x])
  
  # There is no reference to columns in screen to be reassigned, so we need
  # to loop through again to copy the values back into place.
  for i in range(len(newCol)):
    screen[i][x] = newCol[i]




############ Main Program ##################

# Initialize the 2D list of bools to represent the screen
for i in range(6):
  row = []
  for j in range(50):
    row.append(False)
  screen.append(row)
  
# Read the input file one line at a time and perform the given operation
with open("input.txt", 'r') as f:
  for line in f:
    
    if line[:4] == "rect":
      sp = line.index(' ')
      x  = line.index('x')
      a = int(line[sp + 1:x])
      b = int(line[x + 1:])
      
      rect(a, b)
    
    elif line[:10] == "rotate row":
      eq = line.index('=')
      sp = line.rindex(' ')
      a = int(line[eq + 1:sp - 3])
      b = int(line[sp + 1:])
      
      rotate_row(a, b)
    
    
    elif line[:10] == "rotate col":
      eq = line.index('=')
      sp = line.rindex(' ')
      a = int(line[eq + 1:sp - 3])
      b = int(line[sp + 1:])
      
      rotate_column(a, b)
    
    
    else:
      raise Exception("Found instruction that didn't parse: " + line)

# Count how many pixels were on and print the screen output nicely
onCount = 0

for row in screen:
  for pixel in row:
    if pixel:
      onCount += 1
      print '#',
    else:
      print ' ',
  print
  
  
# Print how many pixels were on
print("{} total pixels on".format(onCount))
  
  

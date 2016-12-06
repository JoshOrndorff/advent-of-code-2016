
def get_next_number(start, inst):
  """Returns the ending position on the key pad given the starting position,
     and the instruction string to follow."""
  
  # Setup current location variable for the first time.
  currentLocation = start
  
  # Loop through each character in inst and apply it (but watch out for the \n).
  for step in inst[:-1]:
    currentLocation = process_step(currentLocation, step)
  
  # When the loop finishes, we are done processing this instruction
  return currentLocation
  
  
  
def process_step(start, step):
  """Returns the ending location on the keypad given the starting location and
     a single step from {'U', 'D', 'L', 'R'}."""
     
  # Make a dictionary of helper functions to call depending on step.
  directory = {'U': step_up, 'D': step_down, 'L': step_left, 'R': step_right}
  
  # Now call the appropriate helper
  return directory[step](start)
  
def step_up(start):
  mapping = {3:1, 6:2, 7:3, 8:4, 'A':6, 'B':7, 'C':8, 'D':'B'}
  
  if start in mapping:
    return mapping[start]
  else:
    return start
    
def step_down(start):
  mapping = {1:3, 2:6, 3:7, 4:8, 6:'A', 7:'B', 8:'C', 'B':'D'}
  
  if start in mapping:
    return mapping[start]
  else:
    return start
    
def step_left(start):
  mapping = {3:2, 4:3, 6:5, 7:6, 8:7, 9:8, 'B':'A', 'C':'B'}
  
  if start in mapping:
    return mapping[start]
  else:
    return start
    
def step_right(start):
  mapping = {2:3, 3:4, 5:6, 6:7, 7:8, 8:9, 'A':'B', 'B':'C'}
  
  if start in mapping:
    return mapping[start]
  else:
    return start
    

############# Main Program ##################

# Make an empty list that will hold the results of the PIN
# The list will be built up later.
pin = []

# Start at the right spot according to the directions
leftOff = 5

# Open the input file in read only mode and call the file object f
# The file will be automatically closed when the with block ends
with open("input.txt", "r") as f:
  
  # Loop through each LINE in the file (each line represents one instruction
  for instruction in f:
  
    # Calculate the next number in the pin.
    leftOff = get_next_number(leftOff, instruction)
    
    # Add the result the the pin list before processing the next instruction.
    pin.append(leftOff)
    
    
# Finally preint the result to the screen.
print(pin)

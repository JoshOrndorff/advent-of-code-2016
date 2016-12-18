from hashlib import md5

# My puzzle input
passcode = "hhhxzeay"

# A global to hold all successful paths.
paths = []

def get_valid_moves(x, y, path):
  """ Computes all valid moves from the given state, and returns them. """
  
  valids = ""
  
  # First compute the hash
  digest = md5(passcode + path).hexdigest()
  
  # Check Up
  if y != 0 and digest[0] in "bcdef":
    valids += 'U'
  
  # Check Down
  if y != 3 and digest[1] in "bcdef":
    valids += 'D'
  
  # Check Left
  if x != 0 and digest[2] in "bcdef":
    valids += 'L'
  
  # Check Right
  if x != 3 and digest[3] in "bcdef":
    valids += 'R'
  
  return valids



def next_step(x, y, path):
  """ Recursively tries all valid moves until a dead end or vault is reached.
      If the vault is reached, the successful path is appended to the list
      of successful paths to be later tested for the shortest item. """
  
  # Terminate if we're at the vault
  if x == 3 and y == 3:
    paths.append(path)
    return
  
  # Not at the vault, so figure out where we can go
  valids = get_valid_moves(x, y, path)
  
  # Try all the valid moves.
  if 'U' in valids:
    next_step(x, y - 1, path + 'U')
  
  if 'D' in valids:
    next_step(x, y + 1, path + 'D')
  
  if 'L' in valids:
    next_step(x - 1, y, path + 'L')
  
  if 'R' in valids:
    next_step(x + 1, y, path + 'R')
  
  # We've explored al lvalid paths (which may have been none) so return
  return
  
  



########## Main Program ##########

# Get the recursive path-finding going
next_step(0, 0, '')

# Figure out which paths were longest and shortest
shortest = paths[0]
longest  = paths[0]

for path in paths:
  if len(path) < len(shortest):
    shortest = path
  elif len(path) > len(longest):
    longest = path


# Print the results
print("Shortest path: {} ({})".format(shortest, len(shortest)))
print(" Longest path: {} ({})".format(longest , len(longest )))







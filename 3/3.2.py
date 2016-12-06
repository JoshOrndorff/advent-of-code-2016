
def is_triangle(candidate):
  """Takes a 3-tuple of numbers and returns whether those numbers make a
     valid triangle."""
     
  largest = max(candidate)
     
  others = sum(candidate) - largest
  
  # According to the problem:
  # the sum of any two sides must be larger than the remaining side.
  return others > largest

def parse_input(filename):
  """Parses filename according to the problem rules and return a list of three-
     tuples representing tirangle candidates."""

  # Make an empty list of candidates into which the input file will be parsed.
  candidates = []
  
  # Hack that hardcodes the number of lines in the file :(
  lines = 1914
  linesProcessed = 0
  
  with open(filename, 'r') as f:
    while linesProcessed < lines:
      linesProcessed += 3
    
      # Read three lines at a time
      a = f.readline()
      b = f.readline()
      c = f.readline()
      
      # Process three candidates at a time
      candidates.append((int(a[0:5])  , int(b[0:5])  , int(c[0:5])))
      candidates.append((int(a[5:10]) , int(b[5:10]) , int(c[5:10])))
      candidates.append((int(a[10:15]), int(b[10:15]), int(c[10:15])))
   
  return candidates
  
  
################# Main Program ####################

# Parse the input file
candidates = parse_input("input.txt")

# Make an empty list of valid triangles to be built up
triangles = []

# Check whether each candidate is a valid triangle
for candidate in candidates:
  if is_triangle(candidate):
    triangles.append(candidate)

# Finally, print how many were valid
print(len(triangles))












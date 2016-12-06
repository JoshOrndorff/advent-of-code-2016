
def is_triangle(candidate):
  """Takes a 3-tuple of numbers and returns whether those numbers make a
     valid triangle."""
     
  largest = max(candidate)
     
  others = sum(candidate) - largest
  
  # According to the problem:
  # the sum of any two sides must be larger than the remaining side.
  return others > largest

def parse_candidate(text):
  """Takes a line of text representing space-separated lengths and returns
     a three-tuple containing the values.
     
     Luckily the input format is formatted so that there are 5 characters per
     dimension, so I can just use python's casting functionality."""
  
  a = int(text[0:5])
  b = int(text[5:10])
  c = int(text[10:15])
  
  return (a, b, c)
     
     
     
################# Main Program ####################

# Make an empty list of candidates into which the input file will be parsed.
candidates = []

# And another for the candidates that turn out to be actual triangles
triangles = []

# Parse the input file
with open("input.txt", 'r') as f:
  for line in f:
    candidates.append(parse_candidate(line))
    
# Check whether each candidate is a valid triangle
for candidate in candidates:
  if is_triangle(candidate):
    triangles.append(candidate)

# Finally, print how many were valid
print(len(triangles))












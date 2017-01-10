
# First parse the input into a list
nodes = []
with open("input.txt", 'r') as f:
  # Skip the first two lines because they are headers
  f.next()
  f.next()
  for line in f:
    # Only keep name, used, avail
    nodes.append((line[15:22], int(line[30:33]), int(line[37:40])))

# A little info just to help understand the data
n = len(nodes)
print("Number of nodes is: {}".format(n))
print("Number of nodes squared: {}".format(n * n))
print("Total number of pairs: {}".format(n * (n - 1) / 2))

# Loop through each potential pair of nodes noting viable ones.
numViable = 0
for a in nodes:
  
  # If a is empty the pair is not vialbe
  if a[1] == 0:
    print("Rejecting a as empty. " + str(a))
    continue
  
  for b in nodes:
    
    # If this is the same node as a, it isn't really even a pair
    if b[0] == a[0]:
      continue
    
    # If the the data on a would fit on b, the pair is viable
    if b[2] >= a[1]:
      numViable += 1

# Print the final result
print(numViable)

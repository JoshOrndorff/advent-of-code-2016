numElves = 3018458 # My puzzle input

# List of booleans whether each elf has presents remaining
elves = [True] * numElves  # Elves are indexed from 0 internally


# Loop until only one elf has presents
i = 0
theif = -1
removeNext  = False
while theif != i:
  
  if elves[i]:
    if removeNext:
      elves[i] = False
      removeNext = False
    else:
      removeNext = True
      theif = i
  
  i = (i + 1) % numElves
      

# Print the result. (Plus 1 becuase elves are numbered from 0 internally.)
print("Elf {} has the presents.".format(theif + 1))
  

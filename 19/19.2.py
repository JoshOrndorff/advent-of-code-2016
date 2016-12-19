# My puzzle input: The number of elves to start with
elvesRemaining = 3018458

# Elves are stored in a dictionary.
# Key: Elf number (They are zero-based internally)
# Value: [previous, next]
elves = {}
for i in range(elvesRemaining):
  elves[i] = [i - 1, i + 1]
# Fix the previous for the first elf
elves[0][0] = i
# Fix the next for the last elf
elves[i][1] = 0

# Elf 0 gets to go first
theif = 0
victim = elvesRemaining // 2
while elvesRemaining > 1:
  
  # Calculate the next victim. It always moves up at least one
  nextVictim = elves[victim][1]
  # It moves up a second time if there is now an even number of elves remaining
  if elvesRemaining % 2 == 1:
    nextVictim = elves[nextVictim][1]
  
  # Update the previous and next and remove the victim
  previous = elves[victim][0]
  next = elves[victim][1]
  
  elves[previous][1] = next
  elves[next][0] = previous
  
  del elves[victim]
  
  # Choose the next theif and victim and update the number of remaining elves
  victim = nextVictim
  theif = elves[theif][1]
  elvesRemaining -= 1
  
  # Print some status update
  if elvesRemaining % 100 == 0:
    print(elvesRemaining)


# Print the last remaining elf
for elf in elves:
  print(elf + 1) # Zero-based

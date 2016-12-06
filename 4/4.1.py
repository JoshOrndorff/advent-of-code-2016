def parse_rooms(filename):
  """ Returns list of rooms parsed from filename. """
  
  rooms = []
  
  with open(filename, 'r') as f:
    for line in f:
      rooms.append(parse_room(line))
      
  return rooms
  
def parse_room(text):
  """ Returns a room tripple in the form (name, sector, check). """
  
  lastDash = text.rfind("-")
  left = text.find("[")
  right = text.find("]")
  
  name = text[:lastDash]
  sector = int(text[lastDash + 1: left])
  check = text[left + 1: right]
  
  return (name, sector, check)

def strip_decoys(candidates):
  """ Returns a new list identical to the original, but with decoys removed. """
  
  goodRooms = []
  
  for candidate in candidates:
    if compute_check(candidate[0]) == candidate[2]:
      goodRooms.append(candidate)
      
  return goodRooms
  

def compute_check(name):
  """ Computes (and returns) a correct checksum given a room's name. """
  
  # Remove dashes from the string name to perform character count successfully.
  name = name.replace('-', '')
  
  # Do a character frequency analysis here
  frequencies = {}
  for char in name:
    if char in frequencies:
      frequencies[char] += 1
    else:
      frequencies[char] = 1

  # Now invert that dictionary so frequencies are the keys and lists of letters
  # with those frequencies are the values.
  inverted = {}
  for letter, freq in frequencies.items():
    if freq in inverted:
      inverted[freq].append(letter)
    else:
      inverted[freq] = [letter]
  
  # This check requires the top five most frequent letters. Here I'll find at
  # least five letters, and make sure I return only 5. (There will only be more
  # than five in the case of a tie.
  topChars = []
  while len(topChars) < 5:
    # Find the next most common letter
    mostFreqSoFar = 0
    for freq, letters in inverted.items():
      if freq > mostFreqSoFar:
        mostFreqSoFar = freq
        
    topChars.extend(sorted(inverted[mostFreqSoFar])) # Sorting to alphebetize
    del inverted[mostFreqSoFar] # Removing the most frequent once we've added it.
    
  # Convert to string and truncate to 5 characters.
  return ''.join(topChars)[:5]


    
  
########## Main Program ####################
rooms = parse_rooms("input.txt")

rooms = strip_decoys(rooms)

# Setup a total variable, and loop through valid rooms adding the check
total = 0

for room in rooms:
  total += room[1]
  
# Finally print the result
print(total)






  
  
  

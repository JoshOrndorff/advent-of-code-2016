def get_most_frequent(freqs):
  """ Returns the letter (key) with the highest frequency (value) from the
      given dictionary. """
      
  bestFreq = 0
  bestLetter = ""
  for letter, freq in freqs.items():
    if freq > bestFreq:
      bestFreq = freq
      bestLetter = letter
      
  return bestLetter

def count_frequency(data):
  """Returns a dictionary of frequencies given any iterable. """
  
  freqs = {}
  
  for datum in data:
    if datum in freqs:
      freqs[datum] += 1
    else:
      freqs[datum] = 1
  
  return freqs


######### Main Program ###########
with open("input.txt", 'r') as f:
  messages = f.read().splitlines()

correctString = ""

# Count the frequencies in each column
for col in range(len(messages[0])): # Assume all messages are the same length
  
  # Make a string of all letters in the current column
  colLetters = ""
  for message in messages:
    colLetters += message[col]
    
  # Do the frequency analysis on the current column's letters
  freqs = count_frequency(colLetters)
  
  # Now get the most frequent letter for the column
  correctString += get_most_frequent(freqs)
  
# Print the result
print(correctString)
  
  

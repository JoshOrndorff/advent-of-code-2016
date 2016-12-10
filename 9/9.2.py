
def calc_length(compressed):
  """ Returns the decompressed LENGTH of the passed in compressed data.
      Does not attempt to actually decompress the data. """
  
# Terminating Case: String is empty
  if len(compressed) == 0:
    return 0
  
  # Easy Case: Not a marker, so just count it
  elif compressed[0] != '(':
    currentCount = 1
    next = compressed[1:]
  
  # Interesting Case: Found a marker, so parse it
  elif compressed[0] == '(':
    right = compressed.index(')')
    markerGuts = compressed[1:right]
    
    x = markerGuts.index('x')
    numChars = int(markerGuts[:x])
    times = int(markerGuts[x + 1:])
    
    # Update the compressed string and pick out the part to be repeated
    repeatedBit = compressed[len(markerGuts) + 2:len(markerGuts) + 2 + numChars]
    next = compressed[len(markerGuts) + 2 + numChars:]
    
    # Recurse to find the final length of the repeated bit
    repeatedLength = calc_length(repeatedBit)
    
    # Update total
    currentCount = times * repeatedLength
    
  else:
    raise Exception("Should have met one of the previous cases.")
    
  return currentCount + calc_length(next)



def run_tests():
  """ Runs the test cases given on the website and prints results. """
  testCases = ["ADVENT",
             "A(1x5)BC",
             "(3x3)XYZ",
             "A(2x2)BCD(2x2)EFG",
             "(6x1)(1x3)A",
             "X(8x2)(3x3)ABCY"]

  for case in testCases:
    print(case + " ----> " + calc_length(case))



############# Main Program #################

# Read ths input into a single string (it's all one line).
with open("input.txt", 'r') as f:
  data = f.read()[:-1] # Slice off the final line feed
  
# Print the final output
print(calc_length(data))









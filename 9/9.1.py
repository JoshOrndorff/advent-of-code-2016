
def inflate(compressed):
  """ Returns the decompressed version of the passed in compressed data. """

  decompressed = ""
  while len(compressed) > 0:
    
    if compressed[0] == '(':
      # Found a marker's beginning, so parse it
      right = compressed.index(')')
      markerGuts = compressed[1:right]
      
      x = markerGuts.index('x')
      numChars = int(markerGuts[:x])
      times = int(markerGuts[x + 1:])
      repeatedBit = compressed[len(markerGuts) + 2:len(markerGuts) + numChars + 2]
      
      # Attach repeated text
      for j in range(times):
        decompressed += repeatedBit
      
      # Remove repeated text from the uncompressed string
      compressed = compressed[len(markerGuts) + 2 + numChars:]
      
    else:
      # Not a marker, so just move the character over
      decompressed += compressed[0]
      compressed = compressed[1:]
    
  return decompressed



def run_tests():
  """ Runs the test cases given on the website and prints results. """
  testCases = ["ADVENT",
             "A(1x5)BC",
             "(3x3)XYZ",
             "A(2x2)BCD(2x2)EFG",
             "(6x1)(1x3)A",
             "X(8x2)(3x3)ABCY"]

  for case in testCases:
    print(case + " ----> " + inflate(case))



############# Main Program #################

# Read ths input into a single string (it's all one line).
with open("input.txt", 'r') as f:
  inputData = f.read()[:-1] # Slice off the final line feed

# Print the final output
print(len(inflate(inputData)))









maxIP = 4294967295

mins = []
maxs = []

with open("input.txt", 'r') as f:
  for line in f:
    mins.append(int(line[:line.index('-')]))
    maxs.append(int(line[line.index('-') + 1: -1]))


# Just to enter the loop
stillLooking = True

# Loop until we find a winner
testIP = 0

while stillLooking:

  print("Trying: {}".format(testIP))
  stillLooking = False
  for i in xrange(len(mins)):
    if testIP >= mins[i] and testIP <= maxs[i]:
      print("Banned in {}-{}".format(mins[i], maxs[i]))
      stillLooking = True
      
      # Skip to the end of the current range so we don't keep checking ones that
      # will definitely be banned
      testIP = maxs[i]
      break
  
  testIP += 1

print("First valid ip: {}".format(testIP - 1))

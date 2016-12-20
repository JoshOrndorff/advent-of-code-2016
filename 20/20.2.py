maxIP = 4294967295

mins = []
maxs = []

with open("input.txt", 'r') as f:
  for line in f:
    mins.append(int(line[:line.index('-')]))
    maxs.append(int(line[line.index('-') + 1: -1]))


valids = 0

# Loop until we find a winner
testIP = 0

while testIP <= maxIP:
  
  valid = True
  for i in xrange(len(mins)):
    if testIP >= mins[i] and testIP <= maxs[i]:
      print("Banned in {}-{}".format(mins[i], maxs[i]))
      valid = False
      
      # Skip to the end of the current range so we don't keep checking ones that
      # will definitely be banned
      testIP = maxs[i]
      break
    
  if valid:
    valids += 1
  testIP += 1

print("Number of valid IPs: {}".format(valids))

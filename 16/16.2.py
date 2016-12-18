# My puzzle inputs
a = "01000100010010111"
l = 35651584


def get_b(a):
  """ Calculates the next segment of the modified dragon curve as given in the
      problem description. This function does not combine a with b, it just
      calculates b given a.
      
      This function has been slightly modified from part 1 so as not to copy
      a on each iteration and save memory."""
  
  b = ""
  
  for i in range(len(a) - 1, -1, -1):
    if a[i] == '1':
      b += '0'
    else:
      b += '1'
  
  return b



def single_check(bits):
  """ Computes a SINGLE pass of the checksum algorithm regardless of length.
  
  This function is the big change from my approach in part 1. Python couldn't
  handle the tail recursion used previously with this big data, so I've
  rewritten the algorithm recursively."""
  
  check = ""
  
  for i in range(0, len(bits), 2):
    if bits[i] == bits[i + 1]:
      check += '1'
    else:
      check += '0'
  
  return check



############ Main Program Below #######################

# Calculate enough random data
while len(a) < l:
  a = a + '0' + get_b(a)

# Make sure we have the exact right amount (not too much)
a = a[:l]

# Compute the actual check
while len(a) % 2 == 0:
  a = single_check(a)

# Print the result
print(a)







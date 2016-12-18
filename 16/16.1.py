# My puzzle inputs
a = "01000100010010111"
l = 272


def get_b(a):
  """ Calculates the next segment of the modified dragon curve as given in the
      problem description. This function does not combine a with b, it just
      calculates b given a. """
  
  b = ""
  
  for bit in a[::-1]:
    if bit == '1':
      b += '0'
    else:
      b += '1'
  
  return b



def compute_check(bits):
  """ Computes an entire checksum including the length part. """
  
  while len(bits) % 2 == 0:
    bits = single_check(bits)
  
  return bits



def single_check(bits):
  """ Computes a SINGLE pass of the checksum algorithm regardless of length. """
  
  # Terminating case when we have no data to check
  if bits == "":
    return ""
    
  # Compute first bit, then recurse
  if bits[0] == bits[1]:
    return '1' + single_check(bits[2:])
  else:
    return '0' + single_check(bits[2:])



############ Main Program Below #######################

# Calculate enough random data
while len(a) < l:
  a = a + '0' + get_b(a)

# Make sure we have the exact right amount (not too much)
data = a[:l]

# Compute and printthe desired checksum
check = compute_check(data)
print(check)







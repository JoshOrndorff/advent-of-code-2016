#! /usr/bin/env python3

import hashlib

payload = "wtnhxymk"
digest = ""

nonce = 0
size = 5

# Create a list to hold the successful hashes, and initialize it to Nones
hashes = [None] * 8

while None in hashes:

  nonce += 1
  data = payload + str(nonce)
  digest = hashlib.md5(data).hexdigest()
  
  # First see whether the first 5 hexadigits are 00000
  if digest[:5] == "0" * size:
    
    # Compute the index based on the 6th hexadigit
    index = int(digest[5], 16)
    
    # Now stick it in the list of hashes if it belongs
    if (index in range(0, 8)) and (hashes[index] is None):
      hashes[index] = digest
      
    # Here is some debugging info
    print("Currently Hashing: " + data)
    print("Hash value is: " + digest)
    print("Hashes found so far: " + str(hashes))
    print()
    print()
      
      

# Print the hashes to visually confirm that they are correct
print(hashes)

# Now loop through the hashes and print the 7th hexadigit of each
password = ""
for h in hashes:
  password += h[6]
  
print(password)
  
  
  
  
  
  
  
  

#! /usr/bin/env python3

import hashlib

payload = "wtnhxymk"
digest = ""

nonce = 0
size = 5

# Create an empty list to hold the successful hashes.
hashes = []

while len(hashes) < 8:

  nonce += 1
  data = payload + str(nonce)
  digest = hashlib.md5(data).hexdigest()
  
  if digest[:5] == "0" * size:
    hashes.append(digest)

# Print the hashes to visually confirm that they all start with 0
print(hashes)

# Now loop through the hashes and print the 6th hexadigit of each
password = ""
for h in hashes:
  password += h[5]
  
print(password)
  
  
  
  
  
  
  
  

from hashlib import md5

# A few globals
salt = "ngcjuoqr" # My program input
cache = {}



def md(nonce):
  """
  Wrapper for getting a string representing a hex hash value.
  Abstracts the cache lookup, and handles combining the salt with the nonce.
  """
  
  if nonce in cache:
    return cache[nonce]
    
  else:
    digest =  md5(salt + str(nonce)).hexdigest()
    cache[nonce] = digest
    
    return digest


def consec(text, n, specificChar = None):
  """ Returns whether there are n consecutive occurences of char in text.
      If char is not specified, return whether there are n consecutive
      occurences of ANY character.
      
      Also returns the character."""
  
  # If no character supplied, set it to the first one
  if specificChar is None:
    char = text[0]
  else:
    char = specificChar
  
  # Terminating case: Can't have n consecutive if there aren't n total
  if len(text) < n:
    return False, None
  
  # Check for a consec at the beginning, and if there isn't one, recurse
  for i in range(n):
    if char != text[i]:
      return consec(text[1:], n, specificChar)
  
  # If we made it through the whole loop, we found one (at the beginning).
  return True, char



################# Main Program ########################

nonce = 0
keys = []

# Increment the nonce until we've found enough keys
while len(keys) < 64:
  currentHash = md(nonce)
  has3, currentChar = consec(currentHash, 3)
  
  if has3:
    for i in range(1, 1001):
      tempHash = md(nonce + i)
      has5, _ = consec(tempHash, 5, currentChar)
      if has5:
        keys.append(currentHash)
        print("Key #{}:\tindex: {}\tKey Hash: {}".format(len(keys),nonce, currentHash))
        print("Confirmed by index: {}\tHash: {}".format(nonce + i, tempHash))
        print("\n\n")
        break # So we don't append duplicates
  
  # Clear the cache
  if nonce in cache:
    del cache[nonce]
  
  nonce += 1
  
# Print the final result
  
print("Last useful index: {}".format(nonce - 1)) # -1 to undo the last increment




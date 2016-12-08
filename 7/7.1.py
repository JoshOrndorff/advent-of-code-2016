# Structure of an "address" pair
# (["xxx", "xxx", "xxx"], ["xxx", "xxx", "xxx"])
# Head item is list of strings not from brackets
# Last item is list or stings from brackets (brackets not included)

def parse_address(text):
  """ returns an address parsed from the text string """
  # Create the address parts to build up
  bracketed = []
  plain = []
  
  # Keep processing as long as there are bracketed phrases remaining
  while '[' in text:
  
    # Find the first bracket pair
    left = text.index('[')
    right = text.index(']')
    
    # Isolate the leading plain and bracketed parts and apped them
    thisPlain = text[0: left]
    thisBracketed = text[left + 1: right]
        
    if thisPlain != "":
      plain.append(thisPlain)
      
    if thisBracketed != "":
      bracketed.append(thisBracketed)
      
    # Remove processed bits from text
    text = text[right + 1:]
    
  # If any text remains after processesing, it is one contiguous plain bit
  if text != "":
    plain.append(text)
      
  # Return the address pair
  return(plain, bracketed)



def contains_abba(text):
  """ Returns boolean whether given text contains an abba """
  
  # Terminate if text can't have an abba
  if len(text) < 4:
    return False
  
  # Terminate if text does have an abba
  if text[0] == text[3] and text[1] == text[2] and text[0] != text[1]:
    return True
  
  # Recurse if both cases are still possible
  return contains_abba(text[1:])



def supports_tls(add):
  """ Takes an address pair and returns whether it is real based on ABBA
      checking. """
  
  # First check whether the address is disqualified for bracketed ABBAs
  for bracketPhrase in add[1]:
    if contains_abba(bracketPhrase):
      return False
      
  # Now check whether the address is qualified for non-bracketed ABBAs
  for plainPhrase in add[0]:
    if contains_abba(plainPhrase):
      return True
  
  # If neither of the above cases applies, default to  not a real address.
  return False




############### Main Program ################

# Read in the raw file info
with open("input.txt", 'r') as f:
  raws = f.read().splitlines()

# Parse each piece of text into an address
addresses = []
for raw in raws:
  addresses.append(parse_address(raw))
  
# Strip the ones that have ABBAs in brackets
finalAddresses = []
for address in addresses:
  if supports_tls(address):
    finalAddresses.append(address)

# Finally, print how many there are
print(len(finalAddresses))

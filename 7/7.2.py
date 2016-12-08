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



def supports_ssl(add):
  """ Takes an address pair and returns whether it is real based on ABBA
      checking. """
  
  # Get ABAs from the address's plain parts
  abas = []
  
  for plainPhrase in add[0]:
    abas.extend(get_all_abas(plainPhrase))
  
  # Calculate the corresponding BABs
  soughtBabs = []
  for aba in abas: 
    soughtBabs.append(invert(aba))
  
  # Get actual BABs from address's bracketed parts
  babs = []
  for bracketedPhrase in add[1]:
    babs.extend(get_all_abas(bracketedPhrase))
  
  # Check for overlap, and if it exists, the address supports SSL
  for soughtBab in soughtBabs:
    for bab in babs:
      if soughtBab == bab:
        return True
  
  # There was no overlap, so the address does not support SSL
  return False



def get_all_abas(text):
  """ returns a list of all ABAs in text """
  
  # Terminate if text can't have ABAs
  if len(text) < 3:
    return []
    
  # When string starts with ABA return it, plus any others (including overlap)
  if text[0] == text[2] and text[0] != text[1]:
    return [text[0:3]] + get_all_abas(text[1:])
  
  # When string does not start with ABA, just look through the rest
  return get_all_abas(text[1:])



def invert(aba):
  """ Geven an ABA, returns the corresponding BAB """
  
  # Error check to save sanity
  if aba[0] != aba[2] or aba[0] == aba[1]:
    raise ValueError("non ABA passes to invert")
    
    
  return aba[1] + aba[0] + aba[1]


############### Main Program ################

# Read in the raw file info
with open("input.txt", 'r') as f:
  raws = f.read().splitlines()

# Parse each piece of text into an address
addresses = []
for raw in raws:
  addresses.append(parse_address(raw))
  
# Strip the ones that don't support SSL
finalAddresses = []
for address in addresses:
  if supports_ssl(address):
    finalAddresses.append(address)

# Finally, print how many there are
print(len(finalAddresses))

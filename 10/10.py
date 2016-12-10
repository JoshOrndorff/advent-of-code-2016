# This hack is necessary so python doesn't exceed the maximum recursion depth.
# Some details here: stackoverflow.com/questions/3323001/
# Guess I really should be using haskell
import sys
sys.setrecursionlimit(2500)

# A few global dicts
output = {}
bot = {} # keys are bot numbers, values are lists of chip numbers.

def process_input(inst):
  """ Processes a single input instruction on global variables. """
  
  botNum = int(inst[inst.rindex(' ') + 1:])
  
  inst = inst[inst.index(' ') + 1:]
  chipNum = int(inst[:inst.index(' ')])
  
  if botNum in bot:
    bot[botNum].append(chipNum)
  else:
    bot[botNum] = [chipNum]



def process_all_handoffs(handoffs, toCheck = 0):
  """ Recursively cycles through list of all handoffs processing any that are
      ready, on global variables, until none remain. """
  
  # If no handoffs remain, terminate
  if handoffs == []:
    return
  
  # If we're past the end of the list, reset the pointer to the beginning
  if toCheck == len(handoffs):
    toCheck = 0
  
  # If the current handoff can be processed, do it
  if process_handoff(handoffs[toCheck]):
    handoffs.remove(handoffs[toCheck])
  else:
    toCheck += 1
   
  # Recurse to check the next one
  process_all_handoffs(handoffs, toCheck)



def process_handoff(inst):
  """ Processes a single handoff instructions on global variables.
      Returns whether the instruction was successfully processed."""

  # Extract the bot number and remove "bot n gives " from the beginning
  inst = inst[inst.index(' ') + 1:]
  botNum = int(inst[:inst.index(' ')])
  inst = inst[inst.index('l'):] # l as in low
  
  # If it can't be processed (the bot doesn't yet have two chips), just return
  if botNum not in bot or len(bot[botNum]) < 2:
    return False
  
  # Actually parse and process
  inst = inst.replace(' ', '')
  
  low = inst[5:inst.index('a')] # a as in and
  high = inst[inst.rindex('to') + 2:]
  
  give_chip(min(bot[botNum]), low)
  give_chip(max(bot[botNum]), high)
  
  # Return success
  return True



def give_chip(chipNum, dest):
  """ Gives numbered chip to specified destination (either output or bot). """
  
  if "output" in dest:
    outputNum = int(dest[6:])
    output[outputNum] = chipNum
    
  elif "bot" in dest:
    botNum = int(dest[3:])
    if botNum in bot:
      bot[botNum].append(chipNum)
    else:
      bot[botNum] = [chipNum]
  
  else:
    raise Exception("Invalid Destination.")



################# Main Program ###################

# Read the input file into a list of instructions
with open("input.txt", 'r') as f:
  instructions = f.read().splitlines()

  
# Parse all the input commands, and save in handoffs for later
handoffs = []
for instruction in instructions:
  if "goes" in instruction:
    process_input(instruction)
  else:
    handoffs.append(instruction)

# Now call the function that processes handoffs until none remain
process_all_handoffs(handoffs)

# Find the desired bot who compared chip 61 to 17 (for part 1)
for botNum, chipNums in bot.items():
  if 61 in chipNums and 17 in chipNums:
    print(botNum)

# Multiply the chip numbers from outputs 0, 1, and 2 (for part 2)
print(output[0] * output[1] * output[2])









# Globals for the registers (4 general purpose, and a program counter)
regs = {'a':7, 'b':0, 'c':0, 'd':0}
pc = 0



def is_literal(arg):
  """ Returns whether the given argument is a literal or a register """
  
  return arg in "1234567890"



def execute(inst):
  """ Takes an arbitrary instruction, parses it, and executes it. """
  
  op = inst[:3]
  args = inst[4:]

  if op == "inc":
    # Can't increment a literal
    if is_literal(args):
      return
    regs[args] += 1
    return
  
  if op == "dec":
    # Can't decrement a literal
    if is_literal(args):
      return
    regs[args] -= 1
    return
  
  if op == "tgl":
    tgl(args)
    return
  
  # If we made it this far, there are two args, so parse them
  x = args[:args.index(' ')]
  y = args[args.index(' ') + 1:]
  
  if op == "cpy":
    # Can't copy TO a literal
    if is_literal(y):
      return
    cpy(x, y)
    return
  
  if op == "jnz":
    # Can't jump to a literal
    if is_literal(y):
      return
    jnz(x, y)
    return
    
  raise Exception("Instruction did not parse correctly.")



def tgl(offset):
  """ Toggles the instruction that is x away from the current program counter. """
  
  # Which instruction are we talking about?
  loc = pc + arg_value(offset)
  
  # If the instruction is outside the program, do nothing
  if loc < 0 or loc >= len(instructions):
    return
  
  # Figure out the what the new instruction is
  old = instructions[loc]
  
  oldOp = old[:3]
  args = old[4:]
  
  # inc becomes dec
  if oldOp == "inc":
    new = "dec " + args
  
  # All other one arg instructions become inc
  elif len(args) == 1:
    new = "inc " + args
  
  # jnz becomes cpy
  elif oldOp == "jnz":
    new = "cpy " + args
  
  # All other 2 arg instructions become jnz
  elif len(args) > 1:
    new = "jnz " + args
    
  # Sanity check
  else:
    raise Exception("Instruction being toggled didn't parse properly")
  
  # Put the new instruction into place
  instructions[loc] = new




def cpy(x, y):
  """ Copies x (which could be a literal or a register name) to register y. """

  x = arg_value(x)
  
  regs[y] = x



def jnz(x, y):
  """ Jumps (changes pc) to y iff x (literal or register) is not 0. """
  global pc
  
  x = arg_value(x)
  y = arg_value(y)
  
  # Make the actual jump
  if x != 0:
    pc += + int(y) - 1        # += because jumps are relative
                              # -1 because pc will be incremented again after return



def arg_value(raw):
  """ Extracts a value from an argument either a literal or a register name. """
  
  try:
    val = int(raw)
  except ValueError:
    val = regs[raw]
  
  return val



def print_regs():
  """ Debugging helper that prints all registers. """
  
  for reg, val in regs.items():
    print("{}: {}".format(reg, val))



############## Main Program ##################

# Read the input into a list of instructions
with open("input.txt", 'r') as f:
  instructions = f.read().splitlines()

# Loop until we've reach the end of the instructions.
while pc < len(instructions):
  execute(instructions[pc])
  pc += 1

# Print the requested final result
print("The final value left in register a is {}".format(regs['a']))







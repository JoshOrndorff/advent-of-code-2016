# Globals for the registers (4 general purpose, and a program counter)
regs = {'a':0, 'b':0, 'c':0, 'd':0}
pc = 0



def execute(inst):
  """ Takes an arbitrary instruction, parses it, and executes it. """
  
  op = inst[:3]
  args = inst[inst.index(' ') + 1:]

  if op == "inc":
    regs[args] += 1
    return
  
  if op == "dec":
    regs[args] -= 1
    return
  
  # If we made it this far, there are two args, so parse them
  x = args[:args.index(' ')]
  y = args[args.index(' ') + 1:]
  
  if op == "cpy":
    cpy(x, y)
    return
  
  if op == "jnz":
    jnz(x, y)
    return
    
  raise Exception("Instruction did not parse correctly.")



def cpy(x, y):
  """ Copies x (which could be a literal or a register name) to register y. """

  # Figure out whether x is an integer or not.
  try:
    source = int(x)
  except ValueError:
    source = regs[x]
  
  regs[y] = source



def jnz(x, y):
  """ Jumps (changes pc) to y iff x (literal or register) is not 0. """
  global pc
  
  # Figure out whether x is an integer or not.
  try:
    source = int(x)
  except ValueError:
    source = regs[x]
  
  # Make the actual jump
  if source != 0:
    pc += + int(y) - 1        # += because jumps are relative
                              # -1 because pc will be incremented again after return



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







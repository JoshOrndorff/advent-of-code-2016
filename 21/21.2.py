pw = "fbgdceah"



def swap_position(x, y):
  swap_letter(pw[x], pw[y])

def swap_letter(a, b):
  global pw
  
  pw = pw.replace(a, '_')
  pw = pw.replace(b, a)
  pw = pw.replace('_', b)


def rotate_lr(lr, x):
  global pw
  
  for i in range(x):
    if lr == 'l':
      pw = pw[1:] + pw[0]
    else:
      pw = pw[-1] + pw[:-1]


#def rotate_pos(letter):
#  
#  index = pw.index(letter)
#  by = 1 + index + (1 if index >= 4 else 0)
#  
#  rotate_lr('r', by)

# Rainbow table to help rotate_pos_undo
rainbow = {# index, shift
             1: 1,
             3: 2,
             5: 3,
             7: 4,
             2: 6,
             4: 7,
             6: 0,
             0: 1 }

def rotate_pos_undo(letter):
  
  index = pw.index(letter)
  rotate_lr('l', rainbow[index])


def reverse(x, y):
  global pw
  
  # Make sure x is smaller
  if x > y:
    x,y = y,x
  
  if x > 0:
    pw = pw[:x] + pw[y:x - 1:-1] + pw[y + 1:]
  else:
    pw = pw[y::-1] + pw[y + 1:]
  

def move(frm, to):
  global pw
  
  char = pw[frm]
  
  pw = pw[:frm] + pw[frm + 1:]
  pw = pw[:to] + char + pw[to:]




############# Main Program ##############

# Parse the input
with open("input.txt", 'r') as f:
  insts=f.readlines()
  
# Now execute instructions
for inst in insts[::-1]:

  if "swap position" in inst:
    # Still works backwards
    swap_position(int(inst[14]), int(inst[-2]))
    
  elif "swap letter" in inst:
    # Still works backwards
    swap_letter(inst[12], inst[-2])
  
  elif "rotate left" in inst:
    # Swap left and right
    rotate_lr('r', int(inst[12]))
  
  elif "rotate right" in inst:
    # Swap left and right
    rotate_lr('l', int(inst[13]))
  
  elif "rotate based" in inst:
    # Wrote a brand new function. This one was not trivial
    rotate_pos_undo(inst[-2])
  
  elif "reverse" in inst:
    # Still works backwards
    reverse(int(inst[18]), int(inst[-2]))
  
  elif "move" in inst:
    # Had to swap arguments
    move(int(inst[-2]), int(inst[14]))
  
  else:
    raise Exception("Didn't parse instruction correctly")
  
  #print(inst[:-1])
  #raw_input("Result: " + pw + '\n')

# Print the final output
print(pw)


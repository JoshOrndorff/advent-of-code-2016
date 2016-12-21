pw = "abcdefgh"



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


def rotate_pos(letter):
  
  index = pw.index(letter)
  by = 1 + index + (1 if index >= 4 else 0)
  
  rotate_lr('r', by)


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
'''
#reverse(0, len(pw))
#move(3,5)
print(pw)
'''
# Parse the input
with open("input.txt", 'r') as f:
  for inst in f:
  
    if "swap position" in inst:
      swap_position(int(inst[14]), int(inst[-2]))
      
    elif "swap letter" in inst:
      swap_letter(inst[12], inst[-2])
    
    elif "rotate left" in inst:
      rotate_lr('l', int(inst[12]))
    
    elif "rotate right" in inst:
      rotate_lr('r', int(inst[13]))
    
    elif "rotate based" in inst:
      rotate_pos(inst[-2])
    
    elif "reverse" in inst:
      reverse(int(inst[18]), int(inst[-2]))
    
    elif "move" in inst:
      move(int(inst[14]), int(inst[-2]))
    
    else:
      raise Exception("Didn't parse instruction correctly")

# Print the final output
print(pw)


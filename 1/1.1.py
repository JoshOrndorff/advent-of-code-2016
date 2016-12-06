GIVEN = "R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1"

def get_route(text):
  
  # Terminating case: on last element
  if "," not in text:
    return [(text[0], int(text[1:]))]
    
  firstComma = text.index(",")  
    
  direction = text[0]
  distance = int(text[1: firstComma])
  
  return [(direction, distance)] + get_route(text[firstComma + 2:])



############ Main Program Below ######################

heading = 0
northDist = 0
eastDist = 0

# Convert route text into a list of pairs
route = get_route(GIVEN)

# Process the route and log all the visit points.
for step in route:
  if step[0] == "L":
    heading = (heading - 1) % 4
  else:
    heading = (heading + 1) % 4
    
    
  if heading == 0:
    northDist += step[1]
  
  elif heading == 1:
    eastDist += step[1]
    
  elif heading == 2:
    northDist -= step[1]
  
  elif heading == 3:
    eastDist -= step[1]
  

# Print results    
print("North displacement: {}".format(northDist))
print("East displacement:  {}".format(eastDist))
print("Total distance:     {}".format(abs(eastDist) + abs(northDist)))
  
  

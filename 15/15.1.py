# My puzzle input keyed into a list of disctionaries
discs = [{"total": 7,  "start": 0},
         {"total": 13, "start": 0},
         {"total": 3,  "start": 2},
         {"total": 5,  "start": 2},
         {"total": 17, "start": 0},
         {"total": 19, "start": 7}]


######### Main Program ##########

pressTime = 0

while True:
	
	positions = []
	
	for i in range(len(discs)):
	  # Plus 1 because it takes a second to reach the first disc
		positions.append((discs[i]["start"] + i + pressTime + 1) % discs[i]["total"])
	
	if positions == [0] * len(discs):
		break
	else:
		pressTime += 1
	
print(pressTime)

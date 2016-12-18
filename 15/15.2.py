# My puzzle input keyed into a list of disctionaries
discs = [{"total": 7,  "start": 0},
         {"total": 13, "start": 0},
         {"total": 3,  "start": 2},
         {"total": 5,  "start": 2},
         {"total": 17, "start": 0},
         {"total": 19, "start": 7},
         {"total": 11, "start": 0}]


######### Main Program ##########

pressTime = 0

while True:
	
	positions = []
	
	for i in range(len(discs)):
		positions.append((discs[i]["start"] + i + pressTime + 1) % discs[i]["total"]) # Plus 1 because it takes a second to reac hthe first disc
	
	#raw_input("Time: {} \t Positions: {}".format(pressTime, positions))
	
	if positions == [0] * len(discs):
		break
	else:
		pressTime += 1
	
print(pressTime)

# 121835 is too high

import math
grid = [[0,0,0,1],
		[0,2,0,0],
		[0,0,4,0],
		[3,0,0,0]]
size = len(grid)
area = int(math.sqrt(size))
for row in grid:
	print(row)
solved = False
while solved == False:
	target=int(input("Please enter target: "))
	print('Looking for', target)
	
	print("Searching area ",area,"x",area)	#First Quadrant
	for r in range(area):
		for c in range(area):
			if (grid[r][c] == target):
				print('Target is already in area')
			else:
				print(' - Not here')

	print("Searching area ",area,"x",area)	#Second Quadrant
	for r in range(area):
		for c in range(area,2*area):
			if (grid[r][c] == target):
				print('Target is already in area')
			else:
				print(' - Not here')


	print("Searching area ",area,"x",area)	#Third Quadrant
	for r in range(area,2*area):
		for c in range(area):
			if (grid[r][c] == target):
				print('Target is already in area')
			else:
				print(' - Not here')

	print("Searching area ",area,"x",area)	#Fourth Quadrant
	for r in range(area,2*area):
		for c in range(area,2*area):
			if (grid[r][c] == target):
				print('Target is already in area')
			else:
				print(' - Not here')
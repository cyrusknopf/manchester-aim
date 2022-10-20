#9x9

import math

grid = [[7,0,0,1,0,0,0,0,0],
		[8,1,4,6,9,0,0,0,3],
		[0,3,9,8,5,0,0,0,0],
		[1,9,0,5,0,3,6,0,7],
		[0,4,0,7,0,9,0,3,0],
		[0,7,3,2,0,8,0,0,9],
		[9,0,1,4,7,0,3,2,0],
		[4,2,6,3,8,1,9,7,5],
		[3,0,7,9,2,0,0,0,4],]

size = len(grid)
area = int(math.sqrt(size))
for row in grid:
	print(row)
targetInQuadrant=False
print("\n\n\n")
listAll = [1,2,3,4,5,6,7,8,9]
listPossible = [1,2,3,4,5,6,7,8,9]


for r in range(area):
	for c in range(area):
		listPossible = [1,2,3,4,5,6,7,8,9]		
		print("row= ",grid[r])
		column=list(zip(*grid))
		print("column= ",column[c])
		contents = grid[r][c]
		print("contents:",contents)
		for target in range(1,10):
			if contents in listAll:
				print("Location",r,c,"full, next location")
				break
			elif target in grid[r] or target in column[c]:
				print("checking row",r,"and column",c,"for",target)
				if target in listPossible:
					listPossible.remove(target)
					print(target," removed") 
					print("possible:",listPossible)
			else:
				print(target," not in row or column")
				print("possible:",listPossible)













# for i in range(dfk):
# 	start = 0
# 	end = area
# 	for r in range(start,end):
# 		for c in range(start,end):
# 			if target == grid[r][c]:
# 				print("target in area")
# 				start = end
# 				end = 
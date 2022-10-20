import math

grid = [[0,0,0,1],
		[0,2,0,0],
		[0,0,4,0],
		[3,0,0,0]]
size = len(grid)
area = int(math.sqrt(size))
for row in grid:
	print(row)
targetInQuadrant=False
print("\n\n\n")




for target in range(1,5):
	targetInQuadrant=False
	placeCount=0
	print("\n\n------------------------------\n\nLooking for", target)
	print("Searching first quadrant ",area,"x",area)	#First Quadrant
	for r in range(area):
		for c in range(area):
			print("target:",target)
			if (grid[r][c] == target):
				print("\nTarget is already in area")
				targetInQuadrant=True
			elif (grid[r][c] != 0):
				print("\nLocation Taken, not placeable")
			else:
				print("\n",target," not here")
				print("row num= ",r)
				print("column num= ",c)
				row=(grid[r])
				print("\n","row =",row)
				column=list(zip(*grid))
				print("column: ",column[c],"\n")
				print("targetin Quadrant?",targetInQuadrant)
				if targetInQuadrant == True:
					print("Target is already in quadrant, not placeable")
				elif target in row or target in column[c]:
					print("Target in row or column, not placeable")
					placeable=False
					placeCount=placeCount
				else:
					print("Target not in row or column, placeable")
					placeable=True
					placeCount = placeCount + 1
					placeRow = r
					placeColumn = c
					print("placerow, placecolum:",placeRow, placeColumn)
	if targetInQuadrant==True:
		placeCount=0
		for row in grid:
			print(row)
	if placeCount == 1:
		print("Only one placeable location")
		grid[placeRow][placeColumn] = target
		print("PLACED\n\n\n\n")
		for row in grid:
			print(row)









































	##################################################################
	# 	targetInQuadrant=False
	# 	placeCount=0
	# 	print("\n\n------------------------------\n\nLooking for", target)
		# print("Searching second quadrant ",area,"x",area)
		# for r in range(area):
		# 	for c in range(area,2*area):
		# 		print("target:",target)
		# 		if (grid[r][c] == target):
		# 			print("\nTarget is already in area")
		# 			targetInQuadrant=True
		# 		elif (grid[r][c] != 0):
		# 			print("\nLocation Taken, not placeable")
		# 			numCount = numCount + 1
		# 		else:
		# 			print("\n",target," not here")
		# 			print("row num= ",r)
		# 			print("column num= ",c)
		# 			row=(grid[r])
		# 			print("\n","row:",row)
		# 			column=list(zip(*grid))
		# 			print("colum:",column[c],"\n")
		# 			print("targetinquad?",targetInQuadrant)
		# 			if targetInQuadrant == True:
		# 				print("Target is already in quadrant, not placeable")
		# 			elif target in row or target in column[c]:
		# 				print("Target in row or column, not placeable")
		# 				placeable=False
		# 				placeCount=placeCount
		# 			else:
		# 				print("Target not in row or column, placeable")
		# 				placeable=True
		# 				placeCount = placeCount + 1
		# 				placeRow = r
		# 				placeColumn = c
		# 				print("placerowplacecolum:",placeRow, placeColumn)
		# if targetInQuadrant==True:
		# 	placeCount=0
		# 	for row in grid:
		# 		print(row)
		# if placeCount == 1:
		# 	print("Only one placeable location")
		# 	grid[placeRow][placeColumn] = target
		# 	print("PLACED\n\n\n\n")
		# 	for row in grid:
		# 		print(row)
	# ###################################################################################
	# 	targetInQuadrant=False
	# 	placeCount=0
	# 	print("\n\n------------------------------\n\nLooking for", target)
		# print("Searching third quadrant ",area,"x",area)
		# for r in range(area,2*area):
		# 	for c in range(area):
		# 		print("target:",target)
		# 		if (grid[r][c] == target):
		# 			print("\nTarget is already in area")
		# 			targetInQuadrant=True
		# 		elif (grid[r][c] != 0):
		# 			print("\nLocation Taken, not placeable")
		# 			numCount = numCount + 1
		# 		else:
		# 			print("\n",target," not here")
		# 			print("row num= ",r)
		# 			print("column num= ",c)
		# 			row=(grid[r])
		# 			print("\n","row:",row)
		# 			column=list(zip(*grid))
		# 			print("colum:",column[c],"\n")
		# 			print("targetinquad?",targetInQuadrant)
		# 			if targetInQuadrant == True:
		# 				print("Target is already in quadrant, not placeable")
		# 			elif target in row or target in column[c]:
		# 				print("Target in row or column, not placeable")
		# 				placeable=False
		# 				placeCount=placeCount
		# 			else:
		# 				print("Target not in row or column, placeable")
		# 				placeable=True
		# 				placeCount = placeCount + 1
		# 				placeRow = r
		# 				placeColumn = c
		# 				print("placerowplacecolum:",placeRow, placeColumn)
		# if targetInQuadrant==True:
		# 	placeCount=0
		# 	for row in grid:
		# 		print(row)
		# if placeCount == 1:
		# 	print("Only one placeable location")
		# 	grid[placeRow][placeColumn] = target
		# 	print("PLACED\n\n\n\n")
		# 	for row in grid:
		# 		print(row)
	# ############################################################################
	# 	targetInQuadrant=False
	# 	placeCount=0
	# 	print("\n\n------------------------------\n\nLooking for", target)
	# 	print("Searching fourth quadrant ",area,"x",area)
	# 	for r in range(area,2*area):
	# 		for c in range(area,2*area):
	# 			print("target:",target)
	# 			if (grid[r][c] == target):
	# 				print("\nTarget is already in area")
	# 				targetInQuadrant=True
	# 			elif (grid[r][c] != 0):
	# 				print("\nLocation Taken, not placeable")
	# 				numCount = numCount + 1
	# 			else:
	# 				print("\n",target," not here")
	# 				print("row num= ",r)
	# 				print("column num= ",c)
	# 				row=(grid[r])
	# 				print("\n","row:",row)
	# 				column=list(zip(*grid))
	# 				print("colum:",column[c],"\n")
	# 				print("targetinquad?",targetInQuadrant)
	# 				if targetInQuadrant == True:
	# 					print("Target is already in quadrant, not placeable")
	# 				elif target in row or target in column[c]:
	# 					print("Target in row or column, not placeable")
	# 					placeable=False
	# 					placeCount=placeCount
	# 				else:
	# 					print("Target not in row or column, placeable")
	# 					placeable=True
	# 					placeCount = placeCount + 1
	# 					placeRow = r
	# 					placeColumn = c
	# 					print("placerowplacecolum:",placeRow, placeColumn)
	# 	if targetInQuadrant==True:
	# 		placeCount=0
	# 		for row in grid:
	# 			print(row)
	# 	if placeCount == 1:
	# 		print("Only one placeable location")
	# 		grid[placeRow][placeColumn] = target
	# 		print("PLACED\n\n\n\n")
	# 		for row in grid:
	# 			print(row)
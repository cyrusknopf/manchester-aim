reset = True
while reset == True:
	mode=input("Would you like to decrpyt or encrypt? ")
	if mode == "encrypt":
		shift=int(input("Enter the value of the shift: "))
		plainText=input("Enter text: ")
		cipherText=""
		plainTextPosition=0
		while plainTextPosition < len(plainText):
			plainTextChar=plainText[plainTextPosition]
			ASCIIVal=ord(plainTextChar)
			ASCIIVal=ASCIIVal-shift
			cipherText=cipherText+chr(ASCIIVal)
			plainTextPosition=plainTextPosition+1
		print(cipherText)
	elif mode == "decrypt":
		shift=int(input("Enter the value of the shift: "))
		plainText=input("Enter text: ")
		cipherText=""
		plainTextPosition=0
		while plainTextPosition < len(plainText):
			plainTextChar=plainText[plainTextPosition]
			ASCIIVal=ord(plainTextChar)
			ASCIIVal=ASCIIVal+shift
			cipherText=cipherText+chr(ASCIIVal)
			plainTextPosition=plainTextPosition+1
		print(cipherText)
	elif mode == "quit":
		reset = False
	else:
		print("Invalid input")
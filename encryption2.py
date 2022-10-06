plainText=input("Enter text: ")
cipherText=""
plainTextPosition=0
while plainTextPosition < len(plainText):
	plainTextChar=plainText[plainTextPosition]
	ASCIIVal=ord(plainTextChar)
	ASCIIVal=ASCIIVal-3
	cipherText=cipherText+chr(ASCIIVal)
	plainTextPosition=plainTextPosition+1
print(cipherText)
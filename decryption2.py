cipherText=input("Enter cipher text: ")
plainText=""
cipherTextPosition=0
while cipherTextPosition < len(cipherText):
	cipherTextChar=cipherText[cipherTextPosition]
	ASCIIVal=ord(cipherTextChar)
	ASCIIVal=ASCIIVal+3
	plainText=plainText+chr(ASCIIVal)
	cipherTextPosition=cipherTextPosition+1
print(plainText)

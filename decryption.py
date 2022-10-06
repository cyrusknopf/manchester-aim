cyphertext=input("Enter cipher text: ")
cyphertext=cyphertext.upper()
plainText=""
alphabet="XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
cyphertextPosition=0
while cyphertextPosition < len(cyphertext):
	cyphertextChar=cyphertext[cyphertextPosition]
	alphabetPosition=3
	while cyphertextChar != alphabet[alphabetPosition]:
		alphabetPosition=alphabetPosition+1
	alphabetPosition=alphabetPosition+3
	plainText=plainText+alphabet[alphabetPosition]
	cyphertextPosition=cyphertextPosition+1
print(plainText)

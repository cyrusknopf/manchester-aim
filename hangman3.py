#Hangman
import random

the_words = []
file = open('C:\\Uni\\Year1\\COMP16321\\GitRepos\\COMP16321-Labs_f10983ck\\EnglishWords.txt', 'r')
for line in file:
	line = line.rstrip()
	the_words.append(line)
word = random.choice(the_words)



guesses=[]
length = len(word)
answer = []
count=0
for i in range(length):
	answer.append("_ ")
	print(answer[i], end ="")



while "_ " in answer and count < 10:
	count = count + 1
	if guesses != []:
		print("You have guessed:")
		for p in guesses:
			print(p," ", end="")
		print("\n")
		for a in answer:
			print(a, end="")
	guess = input("\nEnter guess: ")
	while True:
		if guess in guesses:
			print("You have already guessed",guess,"\n")
			guess = input("\nEnter guess: ")
		elif len(guess) > 1:
			print("Please enter a single letter\n")
			guess = input("\nEnter guess: ")
		else:
			break
	guess = guess.lower()
	guesses.append(guess)
	inWord = 0
	for i in range(len(word)):
		if guess == word[i]:
			print("\n",guess,"is the ",i+1,"letter of the word\n")
			answer[i] = (guess)
			inWord = inWord + 1
	if inWord == 0:
		print("\n",guess,"is not in the word\n")

if "_ " not in answer:
	print("Correct! The word was",word)
else:
	print("You didn't get it, the word was",word)
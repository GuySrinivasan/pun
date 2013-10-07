wordlists = [ "american-words.35", "english-words.35" ]

def read_wordlists(wordlists):
	master = []
	for wordlist in wordlists:
		with open("wordlists/"+wordlist, "r") as dict:
			for line in dict:
				master.append(line[:len(line)-1:])
	return master

read_wordlists(wordlists)

def keyboard_distance(typed, word):
	# removal of a letter is 10
	# addition of a letter is 5 to 25 depending on how close it is to the previous and next
	# ignore swapping

### DEBUG
	
for i in range(0,len(master),(int)(len(master)/100)):
	print(master[i])


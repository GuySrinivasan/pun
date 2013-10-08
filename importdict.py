#import numpy

wordlists = [ "american-words.35", "english-words.35" ]

def read_wordlists(wordlists):
	master = []
	for wordlist in wordlists:
		with open("wordlists/"+wordlist, "r") as dict:
			for line in dict:
				master.append(line[:len(line)-1:])
	return master

def levenshtein_distance(typed, word):
	# dist[ti, wj] will hold the levenshtein distance between
	# the first i characters of typed and the first j characters
	# of word
	T = len(typed)
	W = len(word)
	#dist = numpy.zeros((T+1)*(W+1)).reshape(T+1, W+1)
	dist = [[0 for x in range(W+1)] for x in range(T+1)]
	for i in range(T+1):
		for j in range(W+1):
			#print(i,j)
			if min(i,j) == 0:
				dist[i][j] = max(i,j)
			else:
				deletion = dist[i-1][j] + 1
				insertion = dist[i][j-1] + 1
				match = dist[i-1][j-1] + (0 if typed[i-1] == word[j-1] else 1)
				dist[i][j] = min(deletion, insertion, match)
			#print(i,j,dist[i][j])
	return dist[T][W]

def smallest_distance(typed, dict):
	smallest = 1000
	all = []
	for word in dict:
		dist = levenshtein_distance(typed, word)
		if (dist < smallest):
			smallest = dist
			all = [word]
		elif (dist == smallest):
			all.append(word)
	return all
	
### DEBUG
debug = False

if debug:
	temp = read_wordlists(wordlists)

	for i in range(0,len(temp),(int)(len(temp)/100)):
		print(temp[i])

	m = levenshtein_distance("abc", "b")
	print(m)

	print(levenshtein_distance("asdfg", "fads"))

dict = read_wordlists(wordlists)

while True:
	typed = input("Enter misspelled word: ")
	print(smallest_distance(typed, dict))
	if typed == "quit" or typed == "q":
		break
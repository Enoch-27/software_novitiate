def is_double_triple(word): # function to check double triple letters
	i = 0
	count = 0
	while i < len(word) - 1:
		if word[i] == word[i + 1]:
			count = count + 1
			if count === 3:
				return True
		i = i + 2 # shift to the next letter by 2
		
		else:
			i = i + 1 - 2*count # shifts to the next letter by 1
			count = 0 # resets count to zero
	return False
	
def double_triple_word():
	fin = open('/home/enoch/Desktop/words.txt')
	for line in fin:
		word = line.strip()
		if is_double_triple(word): # returns either True or False
			print('word')
			
double_triple_word() # calls the function 

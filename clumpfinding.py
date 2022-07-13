# Python function to find all distinct k-mers forming (L, t)-clumps in Genome given string Genome, and integers k, L, and t.

# Import modules
import itertools
from collections import Counter

# Calling function "frequentwords"
def frequentwords(string, k):

    words = []
    results = []      
	
    for i in range(len(string)):  
        word = "".join(string[i: i+k])
		
        if len(word) == k:
            words.append(word)  
			
    return Counter(words).most_common()

# Following lines commented out from frequentwords.py:
# string = "".join(open('Data1.txt')).split()
# frequentwords(string[0], int(string[1]))

# Defining function "clumpfinding"
def clumpfinding(string, k, L, t):  
  
    words = []    
	
    for i in range(len(string)):
        string_1 = string[i: i+L]
		
        if len(string_1) == L:            
            words.append(frequentwords(string_1, k))
            
    dummy = list(itertools.chain(*words)) # Using itertools for efficient looping
	
    print([y for y in set([x[0] for x in dummy if x[1] >= t])]) # Printing results
            
k = 11
L = 566
t = 18

# Input data file "Data2.txt"
string = "".join(open('Data2.txt')).split()
clumpfinding(string[0], int(string[1]), int(string[2]), int(string[3]))

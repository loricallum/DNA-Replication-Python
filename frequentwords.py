# Python function that finds the most frequent k-mers in a string
# given a DNA string Text and an integer k.

# Import required modules
from collections import Counter

# Define function
def frequentwords(string, k):

    words = []
    results = []    
    
    for i in range(len(string)):    
        words.append("".join(string[i: i+k]))
                
    tuples = Counter(words).most_common()
    max_count = max([y for (x, y) in tuples])
    
    for (x, y) in tuples:
        if y == max_count:
            results.append(x)
            
    print(results)

# Input Data1.txt file with genetic sequence information
string = "".join(open('Data1.txt')).split()
frequentwords(string[0], int(string[1]))

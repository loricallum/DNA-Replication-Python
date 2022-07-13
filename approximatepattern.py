# Python function to find all starting positions where Pattern appears
# as a substring of Text with at most 'd' mismatches given strings
# Pattern and Text along with an integer 'd'.

# Define function "findpattern"
def findpattern(p, q, d):
    count = 0
    for x, y in zip(p,q):
        if x != y: 
            count = count + 1
        if count > d:
            return False
    return True

# Define function "approximatepattern"
def approximatepattern(pattern, genome, d):
    pos = []
    k = len(pattern) # Length of pattern
    l = len(genome) # Length of genome
    for i in range(l-k):
        if findpattern(pattern, genome[i:i+k], d):
            pos = pos + [i]
    print(pos)

# Input data file Data6.txt
string =  "".join(open("Data6.txt")).split()
approximatepattern(string[0], string[1], int(string[2]))
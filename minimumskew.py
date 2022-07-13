# Python function that finds all integer(s) i minimizing Skew(Prefixi (Text)) 
# over all values of i (from 0 to |Genome|) given a DNA string Genome.

# Defining the function "skew"
def skew(genome):
            
    output = [0]
    count = 0
    
    for x in genome:
        if x == "G": 
            count = count + 1
        if x == "C":
            count = count - 1
        output = output + [count]
        
    return output # Make this a print statement to view the output

# Defining the function "minimumskew"
def minimumskew(string):
            
    t = skew(string)
    minimumskew = [i for i,n in enumerate(t) if n == min(t)]
            
    print(minimumskew)
    
# Passing Data3.txt as input file (This is a large file!!)
string = "".join(open("Data3.txt")).split()           
minimumskew(string[0])

# Python function pattern matching algorithm for a DNA string
# that includes a simple for loop

# Defining the function "patternmatching"
def patternmatching(string_1, string_2):
    
    pos = []
    k = len(string_1)
        
    for i in range(len(string_2)):
        if string_1 == string_2[i: i+k]:
            pos.append(str(i))
            
    print( " ".join(pos))

# Pass input data as a text file - Data4.txt
string = open('Data4.txt').read().split()
patternmatching(string[0], string[1])

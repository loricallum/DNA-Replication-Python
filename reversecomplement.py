# Python function that finds the reverse complement of a DNA string
# given a DNA string Pattern. 

# Defining a function "reversecomplement"
def reversecomplement(string):
    
    dictionary = {"A":"T", # A dictionary is defined so within curly brackets
                  "T":"A",
                  "C":"G",
                  "G":"C"}
    output = [dictionary[x] for x in string.strip()[::-1]]
    print("".join(output))

# Input data file Data5.txt
string = "".join(open('Data5.txt'))
reversecomplement(string)

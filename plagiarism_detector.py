
from difflib import SequenceMatcher 
  
# Declaring string variables 
string1 = 'I am gubli'
string2 = 'I am gublu'
  
# Using the SequenceMatcher() 
match = SequenceMatcher(None ,  
                        string1, string2) 
  
# convert above output into ratio 
# and multiplying it with 100 
result = match.ratio() * 100

print(int(result), "%")
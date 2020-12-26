

# Regular expressions are essentially a tiny,highly specialized programming language
 # which embedded inside pythopn and model available through(re).

# used for searching text string which is in proper formate.
# Regular expressions is a special sequence of characters that help you match
  # or find other strings or sets of strings using special syntax held in pattern.


# Ex:- If we want to find any files which has patterns to get particular data & time.
   # from that log file.[Occures in operating system]
# If we want to find the no.of contact also can be found by using regular expressions.
   #  for different countries by using regular expressions.



# '.' Matches with any single character except newline ‘\n’. #
# '?'	 match 0 or 1 occurrence of the pattern to its left #
# '+'	 1 or more occurrences of the pattern to its left #
# '*'	 0 or more occurrences of the pattern to its left #
#'\w'	 Matches with a alphanumeric character whereas 
             \W (upper case W) matches non alphanumeric character.#
# '\d'	  Matches with digits [0-9] and /D (upper case D) matches with non-digits. #
# '\s'	 Matches with a single white space character (space, newline, return, tab, form) 
                       and \S (upper case S) matches any non-white space character.#
# '\b'	 boundary between word and non-word and /B is opposite of /b #
# '[..]'	 Matches any single character in a square bracket and [^..] matches any single character not in square bracket #
# '\'	 It is used for special meaning characters like \. to match a period or \+ for plus sign. #
# '^' and '$'	 '^ and $' match the start or end of the string respectively #
# {n,m}	 Matches at least n and at most m occurrences of preceding expression 
                   if we write it as {,m} then it will return at least any minimum occurrence to max m preceding expression. #
# 'a| b'	 Matches either a or b #
# ( )	Groups regular expressions and returns matched text #
# \t, \n, \r	 Matches tab, newline, return #
                   

# In order to do regular expression we use library called  " re " in python #
                   
                   
import re


# Most commonly used methods in re packages #

re.match()
re.search()
re.findall()
re.split()
re.sub()
re.compile()                  




import re
result = re.findall(r'.','DS is largest demand course in world')
print(result)

# we can use \w instaed of '.' to avoid space #

import re
result = re.findall(r'\w','DS is largest demand course in world')
print(result)


import re
result = re.match(r'demand','demand for data science')
print(result)

result = re.match(r'danger','demand for data science')
print(result)

import re
result = re.search(r'danger','demand for data science')
print("result.group(0)")





import re

examplestring = "karthik is 30 years old, and kalyan is 28 years old.rajesh is 26 , and his father is 50 ."
                 
ages = re.findall(r'\d{1,3}',examplestring)
names = re.findall(r'\w',examplestring)

print(names)


import re
str ="mon ,tues, wed,thur,fri"
allstr = re.findall("[shmp]at",str)

for i in allstr:
    
    print(i)


import re

randstr = "keep your concentration more"
print(randstr)
regex = re.compile("\n")
randstr = regex.sub(" ",randstr)
print(randstr)

import re
navin = 'do well'
allnavin = re.compile("\n")
print(navin)



import re

def Main():
    Line = "I think I need to understand"
    
    matchResult = re.match('think',Line,re.M|re.I)
    if matchResult:
        print("Match Found: "+matchResult.group())
    else:
        print("No Match was Found")
    
    searchResult = re.search('think', Line, re.M|re.I)
    if searchResult:
        print("Search Found : "+searchResult.group())
    else:
        print("Nothing Found in search")
        
if __name__ == " __main__ ":
         Main()        
    
    
    
    
    
    
    
import re

x = re.search("man","A man and a horse can't be friends.")
print(x)    
x = re.search("devil","A man and a horse can't be friends.")
print(x)
if re.search("man","A man and a horse can't be friends."):
    print("Some kind of man has been found: ")
else:
    print("No man has been found: "("Some kind of man has been found: "))
if re.search("devil","A man and a horse can't be friends."):
    print("mans and horses and a devil.")
else:
    print("No devil around.")
    
    
    




import re
s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
print(re.search(r"M[ae][iy]er", s1))
print(re.search(r"M[ae][iy]er", s2))
print(re.match(r"M[ae][iy]er", s1))
print(re.match(r"M[ae][iy]er", s2))


import re
s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
print(re.search(r"^M[ae][iy]er", s1))
print(re.search(r"^M[ae][iy]er", s2))
s = s2 + "\n" + s1
print(re.search(r"^M[ae][iy]er", s))























    
    
    
    
    
    
    
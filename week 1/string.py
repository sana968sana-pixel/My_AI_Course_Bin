# 1. Length of a String
#Write a program that reads a string and prints its length.
#o Input: "hello world" → Output: 11
#Hint: Use len(s)."""


print("\n string")
str=input("enter a string ")
print("the lenght of string is :",len(str))

#2. Uppercase & Lowercase
#Convert the input string to uppercase and lowercase.
#o Input: "Python3" → Output: "PYTHON3", "python3"
#Hint: Methods: s.upper(), s.lower().

print("\n next question")
str1=input("enter string is Python3 :")
print(str1.upper(),str1.lower())

# Count a Character
#Count how many times a given character appears in a string (case-sensitive).
#o Input: "banana", "a" → Output: 3
#Hint: Use s.count(ch).'''

print("\n next question")
s="banana"
print("number of a in banana is :",s.count("a"))

# First & Last Character
#Print the first and last character of a string; handle empty input.
#o Input: "drawer" → Output: First: d, Last: r
#Hint: Check empty with if not s; index via s[0] and s[-1]'''

print("\n next question")
str="drawer"
if str:
    print("First:",str[0],"Last:",str[-1])
else:
    print("string is empty")
# Check Substring Presence
#Check if a substring exists in a string.
#o Input: "data science", "science" → Output: True
#Hint: Use the in operator: sub in s.'''

print("\n next question")
str="data science"
print( "science" in str)

#Slice a String
#Print a substring from index start to end (exclusive).
#o Input: "programming", 3, 8 → Output: "gramm"
#Hint: Use slicing: s[start:end].'''

print("\n next question")
str="programming"
print("output:"+str[3:8:])

#Reverse a String
# Reverse the string.
#o Input: "Python" → Output: "nohtyP"
#Hint: Slicing trick: s[::-1].
print("\n next question")
str="Python"
rev_str=str[::-1]
print("output :"+rev_str)

#Replace Substring
#Replace all occurrences of a word with another (case-sensitive).
#o Input: "I love apples. Apples are great!", "apples", "oranges"
#o Output: "I love oranges. Apples are great!"
#Hint: s.replace(old, new) replaces exactly matching cases.
print("\n next question")
str2="I love apples. Apples are great! "
print(str2.replace("apples","oranges"))

#Split and Join
#Split a sentence on spaces and join with -.
#o Input: "split this sentence" → Output: "split-this-sentence"
#Hint: s.split() then "-".join(words).
print("\n next question")
ss="split this sentence"
world=ss.split(" ")
print("output:","-".join(world))

# Strip Whitespace
#Remove leading and trailing spaces.
#o Input: " padded text " → Output: "padded text"
#Hint: Use s.strip().
print("\n next question")
s="  padded text  "
print(s.strip())


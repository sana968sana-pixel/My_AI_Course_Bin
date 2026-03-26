# 1. Length of a String
#Write a program that reads a string and prints its length.
#o Input: "hello world" → Output: 11
#Hint: Use len(s)."""


print("\n string")
s=input("enter a string ")
print("the lenght of string is :",len(s))

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
s="drawer"
if s:
    print("First:",s[0],"Last:",s[-1])
else:
    print("string is empty")
# Check Substring Presence
#Check if a substring exists in a string.
#o Input: "data science", "science" → Output: True
#Hint: Use the in operator: sub in s.'''

print("\n next question")
s="data science"
print( "science" in s)

#Slice a String
#Print a substring from index start to end (exclusive).
#o Input: "programming", 3, 8 → Output: "gramm"
#Hint: Use slicing: s[start:end].'''

print("\n next question")
s="programming"
print("output:"+s[3:8:])

#Reverse a String
# Reverse the string.
#o Input: "Python" → Output: "nohtyP"
#Hint: Slicing trick: s[::-1].
print("\n next question")
s="Python"
rev_str=s[::-1]
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

#Count Vowels & Consonants
#Count vowels and consonants (letters only; ignore digits/punctuation).
#o Input: "Hello, World! 123" → Output: Vowels: 3, Consonants: 7
#Hint: Iterate characters; check ch.isalpha(); membership test like ch.lower() in
#"aeiou".
user_input="Hello, World! 123"
vowel=0
consonant=0
for ch in user_input:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel+=1
        else:
            consonant+=1
print(vowel)
print(consonant)

# Palindrome Check (Ignore Case & Non-alphanumerics) 
#Determine if a string is a palindrome ignoring case and non-alphanumeric characters. 
#o Input: "A man, a plan, a canal: Panama!" → Output: True 
#Hint: Normalize with ''.join(ch.lower() for ch in s if ch.isalnum()); compare to 
#its reverse.
s= "A man, a plan, a canal: Panama!"
l=''.join(ch.lower() for ch in s if ch.isalnum())
if l==l[ ::-1]:
    print(True)
else:

    print(False)


#Title Case (Manual) 
#Convert a sentence to title case without using .title(). 
#o Input: "hELLO wORLD from PYTHON" → Output: "Hello World From Python" 
#Hint: Split into words; for each word: word[0].upper() + word[1:].lower() 
#(guard empty words).
input= "hELLO wORLD from PYTHON"
r=" ".join( word[0].upper() + word[1:].lower() for word in input.split() )
print(r)


#Find All Indices of a Substring (Allow Overlaps) 
#Return a list of starting indices where a substring occurs. 
#o Input: s="aaaa", sub="aa" → Output: [0, 1, 2] 
#Hint: Loop i from 0 to len(s) - len(sub); compare slices s[i:i+len(sub)]. 
s="aaaa"
sub="aa"
result=[]
for i in range(len(s) - len(sub)+1):
    if s[i:i+len(sub)]==sub:

      result.append(i)
print(result)

#Character Frequency Dictionary 
#Build a frequency dictionary for characters (case-insensitive, skip spaces). 
#o Input: "Baa Baa Black Sheep" 
#o Output (order may vary): {'b':3,'a':5,'l':1,'c':1,'k':1,'s':1,'h':1,'e':3,'p':1} 
#Hint: Iterate for ch in s.lower(): and if ch != ' ': then count with a dict; 
#dict.get(ch, 0)+=1. 
s="Baa Baa Black Sheep"
dict={}
for ch in s.lower():
    if ch != ' ': 
        dict[ch]=dict.get(ch, 0)+1
print(result)

#Anagram Checker 
#Check if two strings are anagrams (ignore spaces, punctuation, and case). 
#o Input: "Listen", "Silent" → Output: True 
#Hint: Normalize to letters with ch.isalpha() and lower(), then compare 
#sorted(s1) vs sorted(s2) or frequency dicts. 
s1="Listen"
s2="Silent"
a=" ".join(ch.lower() for ch in s1 if ch.isalpha())
b=" ".join(ch.lower() for ch in s2 if ch.isalpha())
print(sorted(a)==sorted(b))


#Compress Repeated Characters (RLE-lite) 
#Compress runs of the same character as <char><count>. 
#o Input: "aaabbcaaaa" → Output: "a3b2c1a4" 
#Hint: Track current char and run length; flush when char changes or at the 
#end.
s = "aaabbcaaaa"
res, c = "", 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        c += 1
    else:
        res += s[i-1] + str(c)
        c = 1
res += s[-1] + str(c)
print(res)

#Longest Word in a Sentence 
#Find the longest word; if multiple, return the first. Consider words as alphabetic 
#sequences. 
#o Input: "Find the longest_word here!" → Output: "longest" 
#Hint: Filter to letters using ''.join(ch for ch in token if ch.isalpha()); track max 
#by length.

sentence = "Find the longest_word here!"

longest = ""
max_len = 0

for token in sentence.split():
    word = ''.join(ch for ch in token if ch.isalpha())  
    if len(word) > max_len:
        longest = word
        max_len = len(word)

print(longest)


# Remove Duplicate Characters but Keep Order 
#Remove duplicates while preserving the first occurrence order. 
#o Input: "banana" → Output: "ban" 
#Hint: Maintain a seen set; build result by adding chars not in seen.
s = "banana"

result = ""
seen = set()

for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)

print(result)



# Mask Email Username 
#Mask all but the first and last character of the username with *; keep domain intact. 
#o Input: "john.doe@example.com" → Output: "j******e@example.com" 
#Hint: Split on '@'; for the left part, if length ≥ 2, keep first and last and 
#replace middle with '*' * (len-2); if shorter, handle edge cases.
email = "john.doe@example.com"

username, domain = email.split('@')

if len(username) >= 2:
    masked_username = username[0] + '*' * (len(username) - 2) + username[-1]
else:
    masked_username = username  
masked_email = masked_username + '@' + domain

print(masked_email)
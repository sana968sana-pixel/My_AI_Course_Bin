# Given two sets, find elements that are in the first set but not the second. 
#Tip: Use the - operator. 
s={1,2,3,4,5,9}
s1={2,3,9,4,6}
print(s-s1)



#Find common items between three sets using intersection. 
#Tip: Use set1 & set2 & set3.
s={1,2,3,4,5,9}
s1={2,3,9,4,6}
s2={3,5,6}
print(s&s1&s2)

#Given a sentence, return all unique words in lowercase. 
#Tip: Split the string → lowercase → convert to set.
s=" Hello  i am Sana"
d=set(word.lower()   for word in s.split())
    
print(d)



# Convert a list with duplicates into a set, 
# then back to a sorted list. 
#Tip: Use sorted(set(list)). 
l=[ 1,3,9,2,1,3,1,4,2,5]
print(sorted(set(l)))

#Check if one set is a strict subset of another. 
#Tip: Use < operator
s={1,2,3,4,5,6}
s1={1,2,3,4,9}
print(s<s1)


#. Use a set comprehension to collect all squares 
# of numbers from 1–15 that are divisible by 3. 
#Tip: Write {x*x for x in ... if x % 3 == 0}. 

s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
s={x*x for x in s if x%3==0}
print(s)

#Count how many duplicate values exist in a list using sets. 
#Tip: Compare lengths: len(list) - len(set(list)).
list=[1,2,1,3,14,2,5,6,14,0]
print(len(list) - len(set(list)))

#Write a program to remove all vowels from
#  a string using a set. 
#Tip: Use a vowel set and filter characters. 
s="asad eats icecream ,orange .you also"
vowels={"a" ,"e", "i","o","u","A",'E','I','O','U'}
S="".join([c for c in s if c not in vowels])
print(S)

# Find the symmetric difference between two sets. 
#Tip: Use the ^ operator. 
s1={1,2,3,6,8}
s2={2,5,6,7,8}
print(s1^s2)


# Check if two strings are anagrams using 
# set comparison (unique characters only). 
#Tip: Compare set(str1) with set(str2).
str1="listen"
str2="silent"
print(set(str1)==set(str2))
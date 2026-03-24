#. Count word frequencies in a sentence and
#  store the results in a dictionary. 
#Tip: Use d[word] = d.get(word, 0) + 1. 

sentence=" this is a cat and this is a dog"
d={}
for word in sentence.split():
    d[word]=d.get(word,0) +1
print(d)   

#Invert a dictionary where all values are unique. 
#Tip: Swap key and value in a loop.

d={'a':1,'b':2,'c':3}
empty={}

for i,v in d.items():
   empty[v]=i
print(empty)

#Merge two dictionaries where second
#  dictionary overrides first. 
#Tip: Use {**dict1, **dict2} or dict1 | dict2 (Python 3.9+). 
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'b':100,'d':4}
#s={**dict1, **dict2}
s=dict1 | dict2 
print(s)

#Group words by their first 
# letter into a dictionary of lists. 
#Tip: Use setdefault. 
word=['apple','banana','apricot','blueberry']
d={}
for w in word:
    first=w[0]
    d.setdefault(first,[])
    d[first].append(w)
print(d)    

# Filter a dictionary to keep only
# entries with values greater than 50. 
#Tip: Use a dictionary comprehension. 

d={'a':10,'b':45,'c':60,'d':80}
new={}
for key,value in d.items():
    if(value>50):
        new[key]=value
print(new)

#Given a nested dictionary, 
#safely access a deeply nested key. 
#Tip: Chain .get() calls with default {}.
chain={
    'a':{
        'b':{
            'c':47
        }
    }
}
value=chain.get('a',{}).get('b',{}).get('c',None)
print(value)


# Write a dictionary comprehension that 
# maps numbers 1–10 to their cubes. 
#Tip: {x: x**3 for x in range(1,11)}.
cubes={x:x**3 for x in range(1,11)}
print(cubes)

# Find the key with the highest value in a dictionary. 
#Tip: Use max(d, key=d.get).
d={'a':12,'b':35,'c':96,'d':80}
max_value=max(d,key=d.get)
print(max_value)

#Combine two lists into a dictionary
#  (keys from first list, values from second). 
#Tip: Use zip().
first=["a","b","c","d","e"]
second=[1,2,3,4,5]
d={}
d=dict(zip(first,second ))
print(d)
#. Remove all keys from a dictionary whose values are None. 
#Tip: Check value before adding to new dict.
d={'a':10,'b':None,'c':56,'d':None,'e':122}
new={}
for key , value in d.items():
    if(value!=None):
        new[key]=value
print(new)


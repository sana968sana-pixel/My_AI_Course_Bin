#Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
d={'name': 'Ali', 'age': 25}
print(d['name'])

# Add key 'city': 'Lahore' to a dictionary.
d={'name': 'Ali', 'age': 25}
d["city"]="lahore"
print(d)

#Change 'age' in {'name': 'Ali', 'age': 25} to 30
d={'name': 'Ali', 'age': 25}
d['age']=30
print(d)


#Delete key 'age' from a dictionary.
d={'name': 'Ali', 'age': 25}
del d['age']
print(d)

# Check if key 'salary' exists in a dictionary.
d={'name': 'Ali', 'age': 25}
print("salary" in d)

# Print all keys from {'a': 1, 'b': 2}
d={'a': 1, 'b': 2}
print(d.keys())

#Print all values from a dictionary.
d={'a': 1, 'b': 2}
print(d.values())

#Iterate and print key‑value pairs from {'x': 10, 'y': 20}
d={'x': 10, 'y': 20}
for x,y in d.items():
    print(x,y)

# Use get() to safely read key 'score' from an empty dictionary
d={}
d.get("score")
print(d.get("score",0))

#. Create a dictionary from two lists: keys = ['a','b'], values = [1,2]

   
keys = ['a','b']
values = [1,2]
d=dict(zip(keys,values))
print(d)
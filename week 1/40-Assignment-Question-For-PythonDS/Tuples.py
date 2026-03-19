#Create a tuple t = (10, 20, 30) and print the second element.
t = (10, 20, 30)
print(t[1])

#Find the length of tuple ('a', 'b', 'c').
t=('a','b','c')
print(len(t))

#Unpack the tuple (4, 5) into variables x and y. 
t=(4, 5)
x,y=t
print("x",x)
print("y",y)
#Check if 'b' is in the tuple ('a', 'b', 'c')
t=('a', 'b', 'c')
if "b" in t :
    print(" b in the tuple")

#Create an empty tuple and print its type. 
tt=()
print(type(tt))

# Concatenate (1, 2) and (3, 4) into a new tuple. 
t1=(1, 2)
t2=(3, 4)
print(t1+t2)

# Repeat (7,) three times.
t=(7,)*3
print(t)

# Find the index of 2 in (1, 2, 3, 2).
t=(1, 2, 3, 2)
a=t.index(2)
print(a)

#Count how many times 2 appears in (1, 2, 3, 2)
t=(1, 2, 3, 2)
print(t.count(2))

#. Create a single‑ element tuple containing the value 5. 
t=(5,)
print(t)
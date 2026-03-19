# Create a set from [1, 2, 2, 3] and print it.
s=set([1, 2, 2, 3]) 
print(s)

#Add element 4 to the set {1, 2, 3}. 
s= {1, 2, 3}
s.add(4)
print(s)


#Remove element 2 from the set {1, 2, 3}
s= {1, 2, 3}
s.remove(2)
print(s)


#Check if 5 is in the set {1, 3, 5}
s={1, 3, 5}
print(5 in s)


#Find the length of set {10, 20, 30}
s={10, 20, 30}
print(len(s))


#Clear all elements from the set {1, 2, 3}
s= {1, 2, 3}
s.clear()
print(s)


# Create a set {'a', 'b'} and add 'c' only if it’s missing. 
s= {'a', 'b'}
if 'c'not in s:
    s.add("c")
    print(s)

#Convert list ['a', 'a', 'b'] into a set to remove duplicates
l=set( ['a', 'a', 'b'])
print(l)

#Create two sets and print their union.
s={1,2,3}
s2={"we",12.5,True}
s3=s|s2
print(s3)


# Create two sets and print their intersection
s1={1,2,3,4,8}
s2={3,5,1,7,8}
s3=s1&s2
print(s3)
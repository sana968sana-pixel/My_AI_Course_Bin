#Convert the list [1, 2, 3, 4] into a tuple 
# and then unpack it into four variables. 
#Tip: Use tuple() and simple unpacking
list = [ 1, 2, 3, 4]
t=tuple(list)
a,b,c,d=t
print(a,b,c,d)


#Given t = (('a', 1), ('b', 2), ('c', 3)),
#  create a list of all second elements. 
#Tip: Use a comprehension: x[1].
t = (('a', 1), ('b', 2), ('c', 3))
for i in t:
    print(i[1])

#Write a function that returns multiple 
# values (sum, min, max) using a tuple. 
#Tip: Return (..., ..., ...) and unpack later.
def stats(numbers):
   return sum(numbers),min(numbers),max(numbers)
result=stats([4,7,5,2,3,9])
print(result)
s,mi,mx=stats([4,7,5,2,3,9])

print(s,mi,mx)

#Combine two tuples (1, 2, 3) and (4, 5) 
# then convert the result to a list. 
#Tip: Use + to join them
t1 = ( 1, 2, 3)
t2 = ( 4, 5)
print(t1+t2)

#Given a tuple of numbers, find the 
# element with the highest frequency. 
#Tip: Loop through unique items using set(t)
t = (1, 2, 2, 3, 4, 2, 3, 1)
high=max(set(t), key=t.count)
print(high)


#Check if two tuples contain the 
# same elements regardless of order. 
#Tip: Compare sorted(tuple) values.
t1=(1,2,3,4)
t2=(4,2,3,1)
if sorted(t1)==sorted(t2):
    print("tuple have same elements")
else:
   print("tules are different")

#Extract the last three items from 
# a tuple using slicing. 
#Tip: Use negative indexing: t[-3:].
t=(1,2,3,4,5,6)
print(t[-3:])

# Concatenate a tuple with itself 
# three times (repeat operation). 
#Tip: Use tuple * 3.
t = ( 2, 3, 5)
print((t)*3)

#Convert a nested tuple ((1,2),(3,4))
#  into a flat tuple (1,2,3,4). 
#Tip: Use a comprehension inside tuple().
t = ((1,2),(3,4)) 
flat = tuple(num for sub in t for num in sub)

print(flat)


# Store coordinates in tuples and 
# calculate the Manhattan distance. 
#Tip: Use absolute difference formula: 
# abs(x1-x2) + abs(y1-y2).
p1=(1,2)
p2=(3,4)
distance=abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])
print(distance)
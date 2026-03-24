# Create a list comprehension that returns 
# the squares of only the even numbers from 0–20. 
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l1=[]
for i in l:
    n=i*i
    if i%2==0 :
        l1.append(n)
print(l1)

#Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original. 
#Tip: Use sorted() instead of .sort().
nums= [3, 1, 4, 1, 5, 9]
n=[]
n=sorted(nums)
print(n)
        

# Remove duplicates from a list while preserving the original order. 
#Tip: Track seen values in a new list.
l =  [3, 1, 4, 1, 5, 9, 4, 6]
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)       
print("original list", l)
print(unique)

#Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension. 
#Tip: Use a nested loop inside the comprehension. 
main_list= [[1, 2], [3, 4], [5]]
new_list=[]
for i in main_list:
    for j in i:
        new_list.append(j)

print(new_list) 
#Given names = ['alice', 'Bob', 'charlie', 'DAVID'],
#  sort them alphabetically but ignore case. 
#Tip: Use key=str.lower. 
names=['alice','Bob','DAVID','charlie']

print(sorted(names,key=str.lower))

#Replace items from index 2–4 in a list with [100, 200] using slice assignment. 
#Tip: Use a[2:5] = [...].
a=[2,34,45,50,67,70,89,90]
a[2:5]=[100,200]
print(a)

#Write a program to find all indices of a value in
#  a list (e.g., all indices of 7). 
#Tip: Use enumerate. 
a=[7,2,5,7,4,7]
b=[]
for i,value in enumerate(a):
    if value==7:
        b.append(i)
        
print(b)
# Create a new list containing only elements
#  that appear exactly once in the original list. 
#Tip: Use list.count() inside a comprehension. 
original_list=[7,2,5,7,4,7]
l=[]

for i in original_list:
    n= original_list.count(i)==1
    if n:
        l.append(i)
print(l)

#Rotate a list right by one position
#  (e.g., [1,2,3,4] → [4,1,2,3]). 
#Tip: Use slicing: lst[-1:] + lst[:-1].
lst=[1,2,3,4] 
print(lst[-1:]+lst[ :-1])


# Split a list into two lists: 
# one with even numbers,one with odd numbers. 
#Tip: Create two comprehensions.
l=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
print("original list",l)
for i in l:
    if i%2==0:
        even.append(i)

    else:
        odd.append(i)
print("even numbers in the list",even)
print("odd numbers in the list",odd)

#Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements
nums=[3,1,4,1,5]
print("first element :",nums[0])
print("last element :",nums[-1])


#Find the length of the list colors = ['red', 'blue', 'green']
colors=['red','blue','green']
print(len(colors))

#Append 'yellow' to the list colors = ['red', 'blue'].
colors=['red','blue']
colors.append('yellow')
print(colors) 

#Insert 'orange' at index 1 in fruits = ['apple', 'banana'].
fruits=['apple','banana']
fruits.insert(1,"orange")
print(fruits)

#Remove 'banana' from fruits = ['apple', 'banana', 'grapes'].
fruits = ['apple', 'banana', 'grapes']
fruits.remove("banana")
print(fruits)

# Pop the last element from items = [10, 20, 30] and print the popped value
items = [10, 20, 30]
popped =items.pop(-1)
print(popped)

#Check if 3 is in the list nums = [1, 2, 3, 4].
nums = [1, 2, 3, 4]
print(3 in nums)

#Print the slice [2, 3] from the list [0, 1, 2, 3, 4].
l= [0, 1, 2, 3, 4]
print(l[2:4])

#Replace the element at index 1 in a = [5, 10, 15] with 12.
a = [5, 10, 15]
a[1]=12
print(a)
#Count how many times 2 appears in [1, 2, 2, 3, 2]
num=[1, 2, 2, 3, 2]

print(num.count(2))
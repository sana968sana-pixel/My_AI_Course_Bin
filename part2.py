# Create an integer variable age and a float variable height. Print their types.
age=20
height=5.3
print(type(age))
print(type(height))

# Store the value 3 + 4j in a variable. Print the variable and its type.
compvar=3+4j
print(compvar,type(compvar))


# Create a boolean variable is_python_fun and set it to True.
is_python_fun=True

# Method 1: Assign three different values to three variables in a single line
x,y,z=2,3,5
print(x,y,z)

# Method 2: Assign the same value to three different variables in a single line.
a,b,c=2,2,2
print(a,b,c)

# Take a numeric input from a user and convert it to a float.
number=int(input("integer number is "))
print(float(number))

# Take a string input "100" and convert it to an int.
number="100"
print(type(number))
number=int(100)
print(type(number))

# Create a variable with a complex number and print only its real part.
complex_number=complex(3+4j)
print(complex_number.real)

# Define a string variable containing a paragraph and print its length.
paragraph="hello world"
print("the length of this is:",len(paragraph))

# Swap the values of two variables a and b without using a third variable.
a=2
b=5
a,b=b,a

print("a:",a,"b:",b)

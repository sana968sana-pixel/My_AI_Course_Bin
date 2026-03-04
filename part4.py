# Compare two numbers entered by the user and print if the first is greater than the second
num1=int(input("Enter first number is"))
num2=int(input("Enter second number is"))
print("if the first number is greater than second ",num1>num2)

# Check if a user-entered number is even (Number % 2 == 0) and print the Boolean result.
number=int(input("enter a even number"))
print("number is even",number%2==0)

#  Write a program that checks if a number is between 10 and 50 (inclusive) using and
num =int(input("enter number:"))
number = num>=10 and num<=50
print("is the number is between 10 and 50?:",number)

# Check if a string entered by the user is equal to "Python"
text=input("Enter a string:")
print(text=="python")

#  Use the or operator to check if a user is either "Admin" or "Superuser"
name=input( "enter your role ")
print(name=="superuser" or name=="admin" )

# Demonstrate the not operator by reversing a Boolean variable
print(not True)


# . Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result.
num=0.1+0.2
print(num==0.3)
print(num)

# Take a user's age and check if they are NOT under 18.
age=int(input("enter your age"))
print ( not age<18)

# Check if a number is positive and odd using logical operators.
num=int(input("enter a number"))
print(num>0 and num%2!=0)

# Compare the lengths of two strings provided by the user
str1=input("Enter first string:")
str=input('Enter thr 2nd string')
print(len(str1)<len(str))
print(len(str1)>len(str))
print(len(str1)==len(str))
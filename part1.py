# Write a program to print "Hello, World!" and your name on two separate lines.
print("Hello, World!")
print("Sana")

# Ask the user for their favorite color using input() and print "Your favorite color is [color]".
color=input("what is your favorite color: ")
print("Your favourite color is",color)

# Use a single print() statement to display three different words separated by a hyphen (-).
print("Hello-hi-hey")

# Prompt the user for their birth year and print their age (assume the current year is 2026).
birthYear=int(input("what is your birth year:"))
currentYear=int(2026)
print("your age is ",currentYear-birthYear)

# Print the result of 5 + 5 such that the output is: The sum of 5 and 5 is 10.
print("The sum of 5+5 is", 5+5)

# Use the end parameter in print() to join two separate print statements with a space.
print("hello",end=" ")
print("sana")

# Write a program that takes two strings from the user and prints them joined together.
firstname=input("write your first name :")
lastname=input("write your last name:")
print("your full name is ",firstname+lastname)


# Create a greeting that takes a user's name and prints "Welcome, [Name]!" in all uppercase.
name=input("user name is ")
print("Welcome,",name .upper())

# Ask for a user's city and country, then print them in the format: "City, Country".
city=input("your city ")
country=input("your country name ")
print(city,country)

'''Experiment: What happens if you try to add 
a string and an integer in a print statement?
 Write a code snippet that fixes this using str().'''
print("Age is"+str(20))

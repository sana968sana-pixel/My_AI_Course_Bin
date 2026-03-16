# Write a program to calculate the area of a rectangle (Length × Width).
lenght=5
width=6
area=lenght*width
print("Area of rectangle is ",area)

# Take two numbers and print the result of the first raised to the power of the second (a^b)
a=2
b=3
print("power ",a**b)


# Demonstrate the difference between / (division) and // (floor division) with the numbers 10 and 3.
a=10
b=3
print("division",a/b)
print("floor division",a//b)

# Use the modulus operator % to find the remainder when 25 is divided by 4
a=25
b=4
print("modulus",25%4)

#  Calculate the average of five numbers entered by the user.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
num4=int(input("Enter fourth number:"))
num5=int(input("Enter fifth number:"))
total=num1+num2+num3+num4+num5
avg=total/5
print("avg of five number is :",avg)

#  Create a program that converts minutes into hours and remaining minutes.

minutes=int(input("Enter minutes"))

hour=minutes//60
remaing_min=minutes%60
print(hour,"hours and",remaing_min,"minutes")
#  . Calculate the area of a circle where Area = \pi r^2 (Use 3.14 for \pi).
pi=3.14
r=2
area_of_circle=pi*r*r
print("area of circle is :",area_of_circle)


#  Find the cube of a number entered by the user
number=int(input("Enter a number :"))
print("cube of a number is :",number*number*number)

print("cube of number is:",number*number*number)
#  Perform the calculation 10 + 5 * 2. Does Python follow PEMDAS? Prove it with code.
print(10+5*2)

#  Write a program to calculate simple interest: (P \times R \times T) / 100.
p=1000
r=2
t=60
simple_interest=(p*r*t)/100
print("simple interest ",simple_interest)
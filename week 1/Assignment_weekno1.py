#Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
#(Celsius * 9/5) + 32)
celsius=float(input("enter celsius:"))
fahrenheit=(celsius * 9/5) + 32
print(fahrenheit)

#Calculate Area of a Rectangle 
length=float(input("enter length of rectangle:"))
width=float(input("enter width of rectangle:"))
rec=length*width
print(rec)

#Calculate Compound Interest 
#CI = P * (1 + R/100)**T - P 
#Where P = principal, R = rate, T = time 
P=float(input("principal:"))
R=float(input("rate:"))
T=float(input("time:"))
CI = P * (1 + R/100)**T - P 
print("compond interest:",CI)

#Perimeter of a Rectangle - Take length and width as input and calculate the perimeter. 
l=float(input("enter length of rectangle:"))
w=float(input("enter width of rectangle:"))
perimeter=2*(l+w)
print("perimeter",perimeter)

#Average of Three Numbers - Input three numbers and print their average.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
avg=(a+b+c)/3
print("Average of Three Numbers",avg)

#Square and Cube of a Number - Ask the user for a number and display its square and cube
a=int(input("enter a number:"))
square=a*a
cube=a*a*a
print("square od number:",square)
print("cube:",cube)

#Distribute Items Equally - You have n candies and k students. 
#Write a program to find: 
#how many candies each student gets 
#how many are left
n=int(input("candies:"))
k=int(input("students:"))
print("how many gets",n//k)
print("how left",n%k)

#Calculate Profit or Loss 
#Input cost price and selling price. Display either: 
#Profit and amount, or 
#Loss and amount, or 
#No Profit No Loss 
# Profit or Loss
cp = float(input("Cost Price: "))
sp = float(input("Selling Price: "))

if sp > cp:
    print("Profit:", sp-cp)
elif cp > sp:
    print("Loss:", cp-sp)
else:
    print("No Profit No Loss")

#Total Marks and Percentage 
#Input marks of 5 subjects. Print: 
# Total marks 
# Percentage 
# Average
total=0
for i in range(5):
    total+=float(input("enter marks of subject:"))
print("total",total)
print("percentage",total/5)
print("average:",total/5)

#Salary Calculator 
#Input basic salary. Calculate: 
# HRA = 20% of basic 
# DA = 15% of basic 
# Total Salary = Basic + HRA + DA
basic = float(input("Basic Salary: "))
hra = 0.2 * basic
da = 0.15 * basic
print("Total Salary:", basic + hra + da)

#Age in Months and Days 
#Input your age in years. Calculate and print age in: 
# Months  Days (approximate)
# Age conversion
age = int(input("Age in years: "))
print("Months:", age*12)
print("Days:", age*365)

#Currency Converter (USD to PKR) 
#Input amount in USD. Convert using a fixed exchange rate.
usd = float(input("USD: "))
rate = 280  
print("PKR:", usd * rate)

#Sum of First N Natural Numbers 
#Input a number n, calculate sum of first n natural numbers. 
#Formula: sum = n * (n + 1) / 2
n=int(input("enter number:"))
sum = n * (n + 1) / 2
print("sum of natural number:",sum)

#Percentage of Correct Answers 
#Input total questions and correct answers,
#and calculate the percentage score. 

total = int(input("Total Questions: "))
correct = int(input("Correct Answers: "))
print("Percentage:", (correct/total)*100)

#Speed, Distance, and Time 
#Input distance and time, and calculate speed.
# Speed
d = float(input("Distance: "))
t = float(input("Time: "))
print("Speed:", d/t)

#Calculate Body Mass Index (BMI) 
#Input weight (kg) and height (m), then calculate: 
#BMI = weight / (height ** 2) 
# BMI
w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
print("BMI:", w/(h**2))

#Convert Minutes to Hours and Minutes 
#Input number of minutes and convert to hours and remaining minutes. 
#Example: 130 minutes → 2 hours 10 minutes
m = int(input("Minutes: "))
print("Hours:", m//60)
print("Remaining Minutes:", m%60)
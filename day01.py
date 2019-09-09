
#1
C = float(input("Enter a degree in Celsius:"))
F = (9 / 5) * C + 32
print("%.1f Celsius in %.1f Fahrenhrit"%(C,F))

#2
import math
radius = float(input("请输入半径："))
length = float(input("请输入高："))
area = radius * radius * math.pi
volume = area * length
print("面积为%.4f"%area)
print("体积为%.1f"%volume)

#3
feet = float(input("Enter a value for feet:"))
meters = feet * 0.305
print("%.1f feet is %.4f meters"%(feet,meters))

#4
M = float(input("Enter the amount of water in kilograms:"))
initial = float(input("Enter the initial temperature:"))
final = float(input("Enter the final temperature:"))
Q = M *(final - initial) * 4184
print("The energy needed is %.1f"%Q)

#5
balance,rate = eval(input("Enter balance and interest rate (e.g., 3 for 3%):"))
interest = balance * (rate / 1200)
print("The interest is %.5f"%interest)

#6
v0,v1,t = eval(input("Enter v0, v1 and t:"))
a = (v1 - v0) / t
print("The avergea acceleration is %.4f"%a)

#7
saving = float(input("Enter the monthly saving amount:")) 
num = 0
while num < 1:
    account = saving * (1 + 0.00417) 
    saving = account
    saving += 100
    num += 1
print("After the sixth month, the account value is %f"%account)

#8
num = int(input("Enter a number between 0 and 1000："))
bai = num // 100
shi = (num % 100) // 10
ge = num % 10  
he = bai + shi + ge
print("The sum of the digits is %d"%he)

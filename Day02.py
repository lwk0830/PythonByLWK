#1
import math
a,b,c = eval(input("Enter a, b, c:"))
d = b * b - 4 * a* c
if d > 0:
    r1 = (-b + math.sqrt(d)) / 2 * a
    r2 = (-b - math.sqrt(d)) / 2 * a
    print("The Roots are %f and %f"%(r1,r2))
elif d == 0:
    r1 = (-b + math.sqrt(d)) / 2 * a
    print("The roots is %.0f"%r1)
else:
    print("The equation has no real roots")
    
#2
import random
value1 = random.randint(0, 100)
value2 = random.randint(0, 100)
value3 = value1 + value2
print(value3)
value4 = int(input("输入你猜的数："))
if value4 == value3:
    print("程序为真")
else:
    print("程序为假")

#3
value1 = int(input("Enter today's day："))
value2 = int(input("Enter the unmber of days elapsed since today:"))
if value1 == 0:
    today = "sunday"
elif value1 == 1:
    today = "monday"
elif value1 == 2:
    today = "Tuesday"
elif value1 == 3:
    today = "wednesday"
elif value1 == 4:
    today = "thursday"
elif value1 == 5:
    today = "friday"
elif value1 == 6:
    today = "saturday" 
value3 = value2 % 7
value4 = value1 + value3
if value4 == 0:
    day2 = "sunday"
elif value4 == 1:
    day2 = "monday"
elif value4 == 2:
    day2 = "Tuesday"
elif value4 == 3:
    day2 = "wednesday"
elif value4 == 4:
    day2 = "thursday"
elif value4 == 5:
    day2 = "friday"
elif value4 == 6:
    day2 = "saturday"
print("today is %s and the future day is %s"%(today,day2))

#4
v1,v2,v3 = eval(input("请输入三个数："))
temp = 0
if v2 > v1:
    temp = v1
    v1 = v2
    v2 = temp
if v3 > v1:
    temp = v1
    v1 = v3
    v3 = temp
if v3 > v2:
    temp = v3
    v3 = v2
    v2 = temp
print("大小顺序为%d,%d,%d"%(v3,v2,v1))

#5
weight_1,price_1 = eval(input("Enter weight and price for package 1:"))
weight_2,price_2 = eval(input("Enter weight and price for package 2:"))
value_1 = price_1 / weight_1
value_2 = price_2 / weight_2
if value_1 > value_2:
    print("Package 2 has the better price")
else:
    print("Package 1 has the better price")

#6
month,year = eval(input("请输入月和年："))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("%d,%d月份有31天"%(year,month))
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("%d,%d月有30天"%(year,month))
elif month == 2 and ((year % 4 == 0  and year % 100 != 0) or (year % 400 == 0)):
    print("%d,%d月有29天"%(year,month))
else:
    print("%d,%d月有28天"%(year,month))

#7
import numpy
guest = str(input("请给出你的猜测:"))
num = numpy.random.choice(["正","反"])
print("实际正反：%s"%num)
if guest == num:
    print("猜测正确")
else:
    print("猜测错误")

#8
import random
#这个是闭区间
computer = random.randint(0,2)

user = int(input("scissor(0),rock(1),paper(2):"))
if computer == 0:
    com_gesture = "scissors"
elif computer == 1:
    com_gesture = "rock"
else:
    com_gesture = "paper"
print(com_gesture)
if user == 0:
    user_gesture = "scissors"
elif user == 1:
    user_gesture = "rock"
else:
    user_gesture = "paper"

if computer == user:
    print("The computer is %s. You are %s too.It is a draw"%(com_gesture,user_gesture))
elif user == 0 and computer == 2:
    print("The computer is %s. You are %s.You won"%(com_gesture,user_gesture))
elif user == 1 and computer == 0:
    print("The computer is %s. You are %s.You won"%(com_gesture,user_gesture))
elif user == 2 and computer == 1:
    print("The computer is %s. You are %s.You won"%(com_gesture,user_gesture))
else:
    print("The computer is %s. You are %s.You lose"%(com_gesture,user_gesture))

#9

#10
import numpy
import random
size = str(random.randint(1,12))
color = numpy.random.choice(["梅花","红桃","方块","黑桃"])
if size == "1":
    size = "ace"
if size == "11":
    size = "Jack"
if size == "12":
    size = "Queen"
if size == "13":
    size = "King"
print("你选的这张牌大小是 “%s”,花色是 “%s”"%(size,color))

#11
num = input("Enter a three-digit integree:")
if num[0] == num[-1]:
    print("%s is a palindrome"%num)
else:
    print("%s is not a palindrome"%num) 

#12
side1,side2,side3 = eval(input("Enter three edges:"))
if (side1 + side2 >= side3) and (side1 +side3 >= side2) and (side2 +side3 >= side1):
    sum = side1 + side2 + side3
    print("The perimeter is %.0f"%sum)
else:
    print("Incorrect input")

#13
num = 1
count_just = 0
sum_just = 0
count_back = 0
sum_back = 0
while num != 0:
    num = int(input("Enter an integer, the input ends if it is 0:"))
    if num > 0:
        sum_just += num
        count_just += 1
    else:
        sum_back += num
        count_back += 1
count = count_just + count_back - 1
print('just number sum are %d,back number sum are %d.sum are %d,number are %d'%(sum_just,sum_back,sum_back + sum_just,count))

#14
sum = 10000
count = 0
for i in range(10):
    sum = sum * (1 + 0.05)
    if i < 4:
        count = count + sum
print("十年后的学费为：%.2f"%sum)
print("四年后的总学费为：%.2f"%count)

#15
count = 0
for i in range(100,1001):
    if i % 5 == 0 and i % 6 == 0:
        print(i,end="\t")
        count += 1
        if count % 10 == 0:
            print("")

#16
n = 0
while n*n < 12000:
    n += 1
print("n^2 > 12000的最小整数为：%d"%n)
n = 0
while n*n*n < 12000:
    n += 1
print("n^3 < 12000的最大整数为：%d"%(n-1))

#17
sum_ = 0
for i in range(1,50000):
    sum_ += 1/i
print(sum_)

#18
sum_ = 0
for i in range(1,98,2):
    x = i + 2
    sum_ += i/x 
print(sum_)

#19
sum = 0
for i in range(1,10000):
    flag = (-1 )** (i + 1)
    sum += flag  / ((2*i)- 1)
pi = 4 * sum
print(pi)

#20
for i in range(1,10000):
    sum = 0
    for j in range(1,i):
        if (i % j == 0):
            sum += j
    if sum == i:
        print(sum)

#21
count = 0
for i in range(1,8):
    for j in range(i+1,8):
        print(i,j,end="\t")
        count += 1
    print("")        
print(count)    

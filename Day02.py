# user = str(input("请输入用户名："))
# pwd = int(input("请输入密码："))
# if(user == "liweikang"):
#     if(pwd == 123456):
#         print("登录成功")
#     else:
#         print("密码输入有误")
# else:
#     print("用户名输入有误")

# score = float(input("请输入你的分数："))
# if score > 60 and score < 70:
#     print("您的成绩为A")
# elif score >= 70 and score < 80:
#     print("您的成绩为B")
# else:
#     print("您的成绩为C")


# user = str(input("请输入用户名："))

# if user[0] != "@" and user[0] != "#" and user[0] != "$" and user[0] != "%":
#     pwd = str(input("请输入密码："))
# # print("不能以特殊字符开头！")
# elif pwd.
    

# num = int(input("请输入一个数字："))
# if num > 1:
#     c = 3 * num - 5
# elif num >= -1 and num <= 1:
#     c = num + 2
# else:
#     c = 5 * num + 3

# print("这个数的结果为：%d"%c)

# a = float(input("请输入第一个数字："))
# b = float(input("请输入第二个数字："))
# c = str(input("请输入运算方式（+ - * /）："))
# if c == "+":
#     print("%.2f + %.2f = %.2f"%(a,b,a+b))
# elif c == "-":
#     print("%.2f - %.2f = %.2f"%(a,b,a-b))
# elif c == "*":
#     print("%.2f * %.2f = %.2f"%(a,b,a*b))
# else:
#     print("%.2f / %.2f = %.2f"%(a,b,a/b))

###真正的计算机
# a = float(input("请输入第一个数字："))
# b = float(input("请输入第二个数字："))
# c = str(input("请输入运算方式（+ - * /）："))
# while c != "=":
#     if c == "+":
#         d = a + b
#         b = float(input("请再输入一个数字："))
#     elif c == "-":
#         print("%.2f - %.2f = %.2f"%(a,b,a-b))
#         b = float(input("请再输入一个数字："))
#     elif c == "*":
#         print("%.2f * %.2f = %.2f"%(a,b,a*b))
#         b = float(input("请再输入一个数字："))
#     else:
#         print("%.2f / %.2f = %.2f"%(a,b,a/b))
#         b = float(input("请再输入一个数字："))
    


# import numpy 
# c = input("你的手势为：>>(剪刀，石头，布))")
# res = numpy.random.choice(["剪刀","石头","布"])
# print("系统产生的手势为：")
# print(res)
# if c == res:
#     print("平局")
# elif c == "剪刀" and res == "石头":
#     print("你输了")
# elif c == "剪刀" and res == "布":
#     print("你赢了")
# elif c == "石头" and res == "剪刀":
#     print("你赢了")
# elif c == "石头" and res == "布":
#     print("你输了")
# elif c == "布" and res == "剪刀":
#     print("你输了")
# else:
#     print("你赢了")

#判断回文数
# num = input("请输入一个五位数:")
# if(num[0] == num[-1])and(num[1] == num[-2]):
#     print("是一个回文数")
# else:
#     print("这不是一个回文数") 

#播放音乐
#https://www.cnblogs.com/ocean1100/p/9319891.html
# import pygame
# import time
# file = 'D:\多媒体\音乐\爱最大.mp3'
# pygame.mixer.init()
# print("音乐播放1")
# track = pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(3600)
# pygame.mixer.music.stop()

# _sum = 0
# for i in range (1,101):
#     _sum = _sum + i
# print(_sum)

# _sum = 0
# for i in range (0,101,2):
#     _sum = _sum +i
# print(_sum)

# _sum1 = 0
# for i in range (1,101,2):
#     _sum1 = _sum1 + i
# print(_sum1)

# _sum1 = 0
# _sum2 = 0
# for i in range (101):
#     if i % 2 == 0:
#         _sum1 = _sum1 + i
#     else:
#         _sum2 = _sum2 + i
# print("偶数和为%d"%_sum1)
# print("奇数和为%d"%_sum2)

# import time
# start = time.time()
# sum_ = 0
# for i in range(1000000):
#     sum_ += i
# end = time.time()
# print(end - start)

#99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d"%(j,i,i*j),end="\t")
#     print(end="\n")

#99乘法表置反
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print("%d * %d = %d"%(j,i,i*j),end="\t")
#     print(end="\n")


# num = int(input("请输入一个数："))
# for i in range(2,num):
#     if num % i == 0:
#         sum = 1
#     else:
#         sum = 0
# if sum == 1:
#     print("这个数不是素数")
# else:
#     print("这个数是素数")


# st = "abdlkjgjlkr"
# i = 0
# while i < 11:
#     print(st[i])
#     i += 1














#1
# import math
# r = float(input("Enter the length from the center to a vertex:"))
# s = 2 * r * math.sin (math.pi / 5)
# Area = 5 * s * s / (4 * math.tan(math.pi / 5))
# print("The area of the pentagon is %.2f"%Area)

#2
# import math
# point1_x,point1_y = eval(input("Enter point 1 (latitude and longitude) in degree:"))
# point2_x,point2_y = eval(input("Enter point 2 (latitude and longitude) in degree:"))
# radius = 6371.01
# point1_x = math.radians(point1_x)
# point1_y = math.radians(point1_y)
# point2_x = math.radians(point2_x)
# point2_y = math.radians(point2_y)
# d = radius * (math.acos((math.sin(point1_x) * math.sin(point2_x) + math.cos(point1_x) * math.cos(point2_x) * math.cos(point1_y - point2_y))))
# print("The distance between the two points is % km"%d)

#3
# import math
# side = float(input("Enter the side:"))
# area = (5 * side * side) / (4 * math.tan(math.pi / 5))
# print("The area of the pentagon is %f"%area)

#4
# import math
# num = int(input("Enter the number of sides:"))
# side = float(input("Enter the side:"))
# area = (num * side * side) / (4 * math.tan(math.pi / num))
# print("The area of the polygon is %f"%area )

#5
# code = int(input("Enter an ASCII code:"))
# letter = chr(code)
# print("The character is %c"%letter)

#6
# name = str(input("Enter employee's name:"))
# work_hours = float(input("Enter number of hours worked in a work:"))
# hourly_pay = float(input("Enter hourly pay rate:"))
# federal_tax_rate = float(input("Enter federa tax withholding rate:"))
# state_tax_rate = float(input("Enter state tax withholding rate:"))
# #工资总额
# gross_pay = work_hours * hourly_pay
# #联邦扣税
# federal_withholding = gross_pay * federal_tax_rate
# #州扣税
# state_withholding = gross_pay * state_tax_rate
# #总扣税
# total_withholding = federal_withholding + state_withholding
# #余额
# net_pay = gross_pay - total_withholding
# print("Employee Name: %s"%name)
# print("Hours Worked: %.1f"%work_hours)
# print("Pay Rate: %.2f"%hourly_pay)
# print("Cross Pay: %.1f"%gross_pay)
# print("Deduction:")
# print("  Federal Withholding (20.0%%): $%.2f"%federal_withholding)
# print("  State Withholding (9.0%%): $%.2f"%state_withholding)
# print("  Total Deduction: $%.2f"%total_withholding)
# print("Net Pay: $%.2f"%net_pay)

#7
# integer = input("Enter an integer:")
# print(len(integer))
# inter = integer[::-1 ]
# print("The reversed number is %s"%inter)

#8


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

9

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
# def lwk(value):
#     if value % 2 == 0:
#         print("这是偶数")
#     else:
#         print("这是奇数")
# lwk(4)

# def lwk(value):
#     for i in range(2,value):
#         if value % i == 0:
#             print("这不是一个素数！")
#             break
#     else:
#             print("这是素数")
# lwk(5)


    # if name == "liweikang":
    #     print("请输入密码")
    #     if pwd == "123456":
    #         print("登录成功")
    #     else:
    #         print("密码错误")
    # else:
    #     print("用户名输入错误")

# import random
# def lwk(name,pwd):
#     yzm = random.randrange(1000,9999)
#     # print("验证码是%d"%yzm)
#     res = int(input("验证码是%d,请输入："%yzm))
#     if res == yzm:
#         if name == "admin" and pwd == "123123":
#             print("success")
#         else:
#             print("Error")
#     else:
#         print("验证码错误")
# lwk('admin','123123')

# 1
COUNT = 0
def getPentagonalNumber(n):
    global COUNT
    for i in range(1,n+1):
        COUNT += 1
        sum = i * (3*i - 1) / 2
        print("%.0f"%sum,end="\t")
        if COUNT % 10 == 0:
            print("")
getPentagonalNumber(100)

#2
def sumDigits(n):
    sum = 0
    digit = len(str(n))
    temp = n
    for _ in range(1,digit+1):
        single = temp % 10
        sum = sum + single
        temp1 = temp // 10
        temp = temp1
    print(sum)
num = int(input("请输入一个数："))
sumDigits(num)

#3
def displaySortNumbers(num1,num2,num3):
    if num2 > num1:
        temp = num1
        num1 = num2
        num2 = temp
    if num3 > num1:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 > num2:
        temp = num2
        num2 = num3
        num3 = temp
    print("%d %d %d"%(num3,num2,num1))
num1,num2,num3 = eval(input("Enter three numbers: "))
displaySortNumbers(num1,num2,num3)

#4
def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
    yearlyRate = monthlyInterestRate * 12
    for _ in range(1,years + 1):
        temp = investmentAmount * (1 + yearlyRate)
        investmentAmount = temp
    print(temp)
amount,rate,years = eval(input("请输入投资金额，月利率，多少年"))
futureInvestmentValue(amount,rate,years)

#5
def future(investe,rate):
    print("Years",end="\t")
    print("Future Value")
    for i in range(1,31):
        year_money = investe * (1 + rate/100) 
        investe = year_money
        print(i,end="\t")
        print("%.2f"%year_money)
investe = int(input("The amount invested: "))
rate = int(input("Annual interest rate: "))
future(investe,rate)

#6
COUNT = 0
def printChar(ch1,ch2,numberPerLine):
    global COUNT
    value1 = ord(ch1)
    value2 = ord(ch2)
    for i in range(value1-1,value2):
        if 48 <= value1 <= 57:
            print(chr(int(ch1) + i),end=" ")
            COUNT = COUNT + 1
        elif 65 <= value1 <= 90:
            print(chr(int(ch1) + i),end=" ")
            COUNT = COUNT + 1
        elif 97 <= value1 <= 122:
            print(chr(int(ch1) + i),end=" ")
            COUNT = COUNT + 1
        # else:
        #     print("")
        if COUNT % numberPerLine == 0:
            print("\n")
ch1 = input("请输入开头的字符打印：")
ch2 = input("请输入结尾的字符打印：")
numberPerLine = int(input("请输入每行个数："))
printChar(ch1,ch2,numberPerLine)

#7
def numberPerLineOfDayInAYear(year1,year2):
    print("年份    天数")
    for i in range(year1,year2 + 1):
        print(i,end="\t")
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(366)
        else:
            print(365)
numberPerLineOfDayInAYear(2010,2020)

#8
import math
def distance(x1,y1,x2,y2):
    c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print(c)
x1,y1,x2,y2 = eval(input("请输入坐标:"))
distance(x1,y1,x2,y2)

#9
COUNT = 0
def meishengsushu(num):
    print("p    2^p-1")
    global COUNT
    for i in range(2,num):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            for k in range(1,COUNT):
                if 2 ** (i -1) = i:
                    COUNT = COUNT + 1
                    print(i)

num = int(input("请输入一个数："))
meishengsushu(num)

10
import time
def CurrenTtime():
    print(time.strftime("Current date and time is %m %d, %Y %H:%M:%S",time.localtime(time.time())))
CurrenTtime()

#11
import numpy
import random
def point_sum_1():
    point_1 = numpy.random.choice(["1","2","3","4","5","6"])
    point_1 = int(point_1)

    point_2 = random.randint(1,6)
    point_sum1 = point_1 + point_2 
    print(point_sum1)
    return point_sum1

def point_sum_2():
    point_1 = numpy.random.choice(["1","2","3","4","5","6"])
    point_1 = int(point_1)
    point_2 = random.randint(1,6)
    point_sum2 = point_1 + point_2
    print(point_sum2) 
    return point_sum2

point_sum_1()
point1 = point_sum_1()
if point1 == 2 and point1 == 5 and point1 == 13:
    print("你输了")
elif point1 == 7 and point1 == 11:
    print("你赢了")
else:
    point_sum_2()
    point2 = point_sum_2()
    if point2 == 7:
        print("你输了")
    else:
        print("你赢了")
            



from math import *

# def marks(names):
#     mark={}
#     while names:
#         name=names.pop()
#         mrk = input(f"Talaba {name.title()}ning bahosini kiriting:")
#         mark[name]=int(mrk)
#     return mark
# students = ["Kamoladdin", "Sayilxon", "Hamid", "Sardor", "Mirjalol"]
# mark= marks(students[:])
# print(mark)
#
# x = lambda a , b : a+b
# print(x(5, 6))
# import math
# numbers = list(range(11))
# ildiz = list(map(math.sqrt,numbers))
# print(numbers)
# print(ildiz)
from urllib.request import install_opener

# r1=int(input())
# r2=int(input())
# r3=int(input())
# print((r1**2)*3.14)
# print((r2**2)*3.14)
# print((r3**2)*3.14)

# import math
# r1,r2,r3 = map(int,input().split())
# s1= (r1**2) * math.pi
# s2= (r2**2) * math.pi
# s3= (r3**2) * math.pi
# print('{:.2f}'.format(s1),'{:.2f}'.format(s2),'{:.2f}'.format(s3),)



# s , h = map(float,input().split())
# print('{:.2f}'.format((s*2)/h))

# from math import *
# r = int(input())
# print('{:.2f}'.format((r**2)*(4*pi)))

# a,b,c = map(int,input().split())
# print('{:.2f}'.format((a+b+c)/2))


#
# h,r = map(int,input().split())
# print('{:.2f}'.format(1/3*pi*(r**2)*h))

# import math
# h = int(input())
# print('{:.2f}'.format(sqrt(2*h/9.8)))


from math import *

from attr.validators import min_len

# x = int(input())
# print(x*31536)
#1min = 60ml
#1s = 3600ml
#24s = 86400
#86400 * 730



# n = int(input())
# numbers = range(1, n +1)
# print(sum(numbers))


# m , a = map(int,input().split())
# print(m*a)
#
# r1,r2,r3 = map(int,input().split())
# print('{:.2f}'.format(1/(1/r1+1/r2+1/r3)))

# from math import *
# x, y= map(float, input().split())
# c1=(x+y)/(y**2+fabs(((y**2)+2)/(x+((x**3)/5))))+exp(y+2)
# print(c1)


# from math import *
# x, y= map(float, input().split())
# f1=(2 * tan(x + (pi / 6)) /
#     ((1/3)+cos(y+(x**2))**2) +
#     log((x**2)+2)/log(2))
# print('{:.2f}'.format(f1))



# from math import *
# x, y= map(float, input().split())
# f2=((((1 / (x + (2 / (x ** 2)) + (3 / (x ** 3)))) + (exp ((x**2)+3*x)))/
#         (atan(x+y)+fabs(5+x)**2)) -
#         (cos((y**2)+((x**2)/2))**2))
# print('{:.2f}'.format(f2))


# from math import *
# x, y= map(float, input().split())
# z=(log(fabs((x+y)**2 + sqrt(fabs(y)+2) - (x- ((x*y) / (((x**2)/2)-5))))) + ((cos(x+y)**2)/(x+y)**(1/3)) )
# print('{:.2f}'.format(z ))

# from math import *
# x, y= map(float, input().split())
# T11= (
#         (((x**2)+1) / ((x**2) + ((x*y+(y**2)) / ((y**2) + (y + (x * y)) / (fabs(x * y) + 5)))))
#     + (1/(1+cos(x)+(1/sin(x))))
# )
# print('{:.2f}'.format(T11))

# from math import *
# a,b,h = map(float,input().split())
# l = sqrt((((a/2)-(b/2))**2)+(h**2))
# sy = pi*((a/2)+(b/2))*l
# sa = pi*(((a/2)**2)+((b/2)**2))
# s= (pi*((a/2)+(b/2))*l ) + (pi*(((a/2)**2)+((b/2)**2)))
# s = sy + sa
# print('{:.2f}'.format(s))


# from math import *
# x1,x2 , c, d= map(float, input().split())
# s = sin(fabs(c*x2**3 + d*x1**3 - c*d))**2
# m = sqrt(c*x1**2 + d*x2**2 + 7)
# F = fabs(s/m)   + tan(x1 * (x2 ** 2) + (d ** 3))
# print('{:.2f}'.format(F))


# from math import *
# a,b, c, d, x= map(float, input().split())
# y2= ((a*x**2 + b*x + c) / (x*a**3 + a**2 + a**b-c)) + cos(fabs((a*x + b) / (c*x+d+2**c)))
# print('{:.2f}'.format(y2))

# from math import *
# a, b, c, x= map(float, input().split())
# W1= 0.75+  ( (8.2*x**2 + sqrt(fabs(x**3 + 3*x) + cos(x-2))) /
#              (a/4 + b/3 + c/2 + 1))
# print('{:.2f}'.format(W1))


# from math import *
# a, x = map(float, input().split())
# TT = ( sqrt(x - 1) + sqrt(x + 2) + log(sqrt(a * (x **2) ) + 2 ) )  / sqrt(sqrt(x+2) + sqrt(x+24) + x**5)
# print('{:.2f}'.format(TT))


# from math import *
# a, x, y= map(float, input().split())
# W1= sqrt(exp(x*y) - x * sin(a*x) - ((x**2 + 2)/ (fabs(x)+5))) + sqrt(log(x**2+2)+5)
# print('{:.2f}'.format(W1))

# from math import *
# x = float(input())
# AA = sqrt((2*tan(x+2) - cos(x+(2**x))) / (1 + cos(x + 2) ** 2)) + ((sin(x ** 2)) / ((x ** 2) + 3))
# print('{:.2f}'.format(AA))

# from math import *
# a, x= map(float, input().split())
# BB1 = ( x * sin(x/2 + x/3 + x/4)) + ((log((x**2) - 2) + (3**a)) / (cos(x+3) * sin(x+3) + 8) )
# print('{:.2f}'.format(BB1))

# from math import *
# a, x, y= map(float, input().split())
# TT = sqrt((y**2) + (exp()**x) + sqrt((exp()**x) + (a/ x**2 + 2) + ((cos(x)**2)/sin(x**2) )) ) + cos(x)**3
# print('{:.2f}'.format(TT))


# x, y, z= map(float, input().split())
# print(format(max(x + y+ z,x,y,z), '.2f'),"",format(min(x+ y/2,x, y, z)**2, '.2f'))

# a,b= map(int, input().split())
# if a<=b:
#     print(a-a,b)
# else:
#     print(a,b)

# x, y= map(int, input().split())
# if x!=y:
#     kichik = min(x,y)
#     katta = max(x,y)
#     print('{:.1f}'.format((kichik+katta)/2))
#     print('{:.1f}'.format(kichik*2 * katta*2))

# x, y, z = map(int, input().split())
# if x>0:
#     x = x**2
# if y>0:
#     y = y**2
# if z>0:
#     z = z**2
# print(x,y,z)


# x, y= map(int, input().split())
# if x != y:
#     kichik = (x + y) / 2
#     katta = x * 2 * y * 2
#     if x < y:
#         x, y = kichik, katta
#     else:
#         x, y = katta, kichik
#     print('{:.1f}'.format(x),'{:.1f}'.format(y))






























# print("Hello World!")
# print(10/2)
# print(5*2)
# print(12+3)
# print(15-5)

 #O'ZGARUVCHILAR
 #ozgaruvchi bu pythonda malumot saqlash uchun ajratiladigan biror qism
 #name = "Data types"
 #ozgaruvchi 'name' - esa shu qismning nomi(Xohlagan nom)
 # 'Data types' - shu qismga yuklanadigan malumot turi(str, int , float)
# name = "Kamoladdin" #str - matn. yani so'z
# ag = 15    #int - butun son
# price = 100.00  #float - haqiqiy son


# age = 15
# # data type lani turini shundab gorsa boladi
# print(type(age))





















































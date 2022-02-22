#!/usr/bin/env python
# coding: utf-8

# # Program to find the roots of quadratic equation

# In[1]:


import math
a=float(input("enter the coefficient a"))
b=float(input("enter the coefficient b"))
c=float(input("enter the coefficient c"))
d=b*b-4*a*c;
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Roots are real and unequal",r1,"and",r2)
elif d==0:
    r1=-b/(2*a)
    print("Roots are real and same",r1)
else:
    print("No real numbers are there")


# # Program to check a given number is prime or not

# In[4]:


a=int(input("Enter a number"))
if (a>1):
    for i in range(2,a):
        if(a%i==0):
            print(a,"is not a prime number")
            break
        else:
            print(a,"is a prime number")
            break
else:
    print(a,"is not a prime number")


# # Program to print fibonacci series

# In[6]:


n=int(input("enter how many numbers you want in series"))
first=0;
second=1;
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+second


# # Program to check armstrong number or not

# In[7]:


num=int(input("enter a number"))
temp=num
cnt=0
while temp>0:
    cnt=cnt+1
    temp=temp//10
sum=0
temp=num
while temp>0:
    rem=temp%10
    sum=sum+pow(rem,cnt)
    temp=temp//10
if num==sum:
    print("The number",num,"is an armstrong number")
else:
    print("The number",num,"is not an armstrong number")


# # Program to print the pyramid

# In[9]:


num=int(input("Enter the number of rows you want"))
for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()


# # Program to check strong number or not

# In[ ]:


n=int(input("Enter the number"))
s=0
num=n
while(num>0):
    digit=n%10
    fact=1
for i in range(1,digit+1):
    fact=fact*1
s=s+fact
n=n//10
if(s==num):
    print("strong number")
else:
    print("not a strong number")


# # Program to check perfect number or not

# In[3]:


num=int(input("enter the number"))
result=0
for i in range(1,num):
    if(num%1)==0:
        result=result+i
if result==num:
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")


# # Program to check number is palindrome or not

# In[2]:


num=str(input("enter the number"))
if num==num[::-1]:
    print("yes its a palindrome")
else:
    print("No,its not a palindrome")


# # Program to find the factors of a number

# In[3]:


num=int(input("enter the number"))
for i in range(1,num+1):
    if num%i==0:
        print(i)


# In[ ]:





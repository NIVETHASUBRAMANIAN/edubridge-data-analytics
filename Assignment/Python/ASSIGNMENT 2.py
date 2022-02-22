#!/usr/bin/env python
# coding: utf-8

# # Program to find sum of two numbers:

# In[1]:


num1=int(input("enter the number"))
num2=int(input("enter the number"))
sum=num1+num2
print("sum is",sum)


# # Program to find difference of two numbers

# In[6]:


num1=int(input("enter the number"))
num2=int(input("enter the number"))
diff=num1-num2
print("difference is",diff)


# # Program to find multiplication,division,remainder

# In[4]:


a=int(input("enter the number"))
b=int(input("enter the number"))
m=a*b
d=a/b
r=a%b
print(m,"",d,"",r)


# # Program to find simple interest

# In[14]:


p=int(input("enter the number"))
r=int(input("enter the number"))
t=int(input("enter the number"))
si=(p*r*t)/100
print(si)


# # Swapping using third variable

# In[9]:


x=int(input("enter the number"))
y=int(input("enter the number"))
temp=x
x=y
y=temp
print(x,y)


# # Swapping without using third variable

# In[10]:


x=int(input("enter the number"))
y=int(input("enter the number"))
x=x+y
y=x-y
x=x-y
print(x,y)


# # Average of three numbers

# In[16]:


x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
average=(x+y+z)/3
print(average)


# # Area and perimeter of rectangle

# In[17]:


x=int(input("enter the number"))
y=int(input("enter the number"))
peri=2*(x+y)
area=x*y
print("perimeter",peri)
print("area",area)


# # Salary of an employee,hr-10% da-5%

# In[18]:


num=int(input("enter the number"))
hr=num*10/100
da=num*5/100
salary=num+hr+da
print("salary of an employee",salary)


# In[ ]:





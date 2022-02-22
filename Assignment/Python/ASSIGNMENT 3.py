#!/usr/bin/env python
# coding: utf-8

# # Program to check whether a given year is leap year or not

# In[1]:


year=int(input("Enter the year"))
if(year%4==0)and(year%100==0):
    print("leap year")
else:
    print("not leap year")


# # Program to print the respective day according to number 1 to 7

# In[5]:


day=int(input("enter the number"))
if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("please enter the weekday between 1 to 7")
        


# # Program to print the three numbers in ascending order

# In[1]:


num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1<num2 and num1<num3:
    if num2<num3:
        x,y,z=num1,num2,num3
    else:
        x,y,z=num1,num3,num2
elif num2<num1 and num2<num3:
    if num3>num1:
        x,y,z=num2,num1,num3
    else:
        x,y,z=num2,num3,num1
else:
    if num1<num2:
        x,y,z=num3,num1,num2
    else:
        x,y,z=num3,num2,num1
print("numbers in ascending order:",x,y,z)


# # Write a program to create a calculator

# In[1]:


choice=input('''
please select the type of operation you want to perform:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
if choice=='+':
    print('{}+{}='.format(num1,num2))
    print(num1+num2)
elif choice=='-':
    print('{}-{}='.format(num1,num2))
    print(num1-num2)
elif choice=='*':
    print('{}*{}='.format(num1,num2))
    print(num1*num2)
elif choice=='/':
    print('{}/{}='.format(num1,num2))
    print(num1/num2)
else:
    print('enter a valid operator')


# # Write a program to print the respective month according to number 1 to 12

# In[2]:


num=int(input("enter the number"))
if num==1:
    print("january")
elif num==2:
    print("february")
elif num==3:
    print("march")
elif num==4:
    print("april")
elif num==5:
    print("may")
elif num==6:
    print("june")
elif num==7:
    print("july")
elif num==8:
    print("august")
elif num==9:
    print("september")
elif num==10:
    print("october")
elif num==11:
    print("november")
elif num==12:
    print("december")
else:
    print("enter a valid number")


# # Write a program to print greatest number between three numbers

# In[2]:


num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>=num2 and num1>=num3:
    print("the greatest number is",num1)
elif num2>=num1 and num2>=num3:
    print("the greatest number is",num2)
else:
    print("the greatest number is",num3)


# # Write a program to print smallest number between the numbers

# In[3]:


num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1<=num2 and num1<=num3:
    print("the smallest number is",num1)
elif num2<=num1 and num2<=num3:
    print("the smallest number is",num2)
else:
    print("the smallest number is",num3)


# # Program to print the grade of student according to given criteria
# # >90=A,>75=B,>65=C,>50=D else fail

# In[2]:


num=int(input("enter the number"))
if num>90:
    print("the grade is A")
elif num>75:
    print("the grade is B")
elif num>65:
    print("the grade is C")
elif num>50:
    print("the grade is D")
else:
    print("fail")


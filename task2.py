##Create a Python program that takes a student's marks as input and displays their grade using if, elif, and else.
grade=int(input("enter your grade out of 100{values should not be negative}-:"))
if(grade>=90 and grade<=100):
    print("A+")
elif(grade>=80 and grade<=89):
    print("A")
elif(grade>=70 and grade<=79):
    print("B")
elif(grade>=60 and grade<=69):
    print("C")
elif(grade>=50 and grade<=59):
    print("D")
elif(grade<50 and grade>=0):
    print("Fail")
else:
    print("Invalid input")

##Loops & Number Patterns
##num from 1 to num
num=int(input("enter a number -:"))
for num in range(0,num,1):
    print(num+1) 

##num from num to 1 (in reverse order)by using for loop
num=int(input("enter a number -:"))
for num in range(num,0,-1):
    print(num)     

##num from num to 1 (in reverse order)by using while loop
num=int(input("enter a num-:"))
while num >0:
    print(num)
    num -=1

##table of num
num=int(input("enter a num-:"))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

##Create a Calculator using Functions
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b==0:
        return("Error: division by zero")
    return(a/b)
def calculator():
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Choose operation (1-4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice=="1":
        print(f"Result:{add(a,b)}")
    elif choice=="2":
        print(f"Result:{subtract(a, b)}")
    elif choice=="3":
        print(f"Result:{multiply(a, b)}")
    elif choice=="4":
        print(f"Result:{divide(a, b)}")
    else:
        print("Invalid choice")
calculator()

##scope of variable
college = "CCSU Meerut"
def student_info():
    college = "IIT Delhi"
    print("local variable:", college)
student_info()
print("global:", college)

##Python program using builtin modules 
import math
import random
import datetime

number = 16
print("Square root of", number, "is", math.sqrt(number))

dice_roll = random.randint(1, 6)
print("You rolled a dice and got:", dice_roll)

today = datetime.datetime.now()
print("Today's date and time is:", today)
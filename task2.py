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

# #Loops & Number Patterns
# #num from 1 to num
num=int(input("enter a number -:"))
for num in range(0,num,1):
    print(num+1) 

##num from num to 1 (in reverse order)
num=int(input("enter a number -:"))
for num in range(num,0,-1):
    print(num)     
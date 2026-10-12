### file handling
with open("internship.txt","w") as f:
    data=input("enter a data you want to write in file-:")
    f.write(data)

##reading a file
with open("internship.txt","r") as f:
    print(f.read())

## appending a newdata 
with open("internship.txt","a") as f:
    data=input("enter a data you want to append in file-:")
    f.write(f"\n{data}")

### Exception Handing
try:
    age=int(input("enter your age-:"))
    print(f"your age is:{age}")
except ValueError:
    print("error:invalid input.please enter a number only")

try:
    a=int(input("enter numerator-:"))
    b=int(input("enter denominator-:"))
    print("result a/b:",a/b)
except ZeroDivisionError:
    print("error : division by zero is not allowed")

try:
    with open("missing.txt","r") as f:
        print(f.read())
except:
    print("error: file was not fount")

##Libraries
import random #use to gessing randomayl
import math#in buil mathematical function 
from datetime import datetime
now=datetime.now()
print("ramdom number:",random.randint(100,500))
num=int(input("enter a num-:"))
print(f"square root of num {num}={math.sqrt(num)}")
print("current date and time:",now)

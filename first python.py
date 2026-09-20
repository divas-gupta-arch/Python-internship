print("hello world")

# age=int(input("enter your age:"))
# if (age>=0 and age<18):
#     print("you are minor")
# elif (age>=18 and age<60):
#     print("you are adult")
# elif age>=60:
#     print("you are a senior citizen")
# else:
#     print("invalid input please give the valid input")

# num1=float(input("enter a frist no. :"))
# num2=float(input("enter a second no. :"))
# if num1>num2:
#     print(f"frist no {num1} is grater ")
# elif num2>num1:
#     print(f"second no {num2} is grater")
# elif num1==num1:
#     print(f"frist and sencond no. are equal {num1}={num2}")
# else:
#     print("try again invalid input12")

# gender=input("entere your gender,\n for male(m) and for female(f):")
# if gender=="m"or gender=="M":
#     print("good morning sir")
# elif gender=="f"or gender=="F":
#     print("good morninig ma'am")
# else:
#     print("invalid input")

# checking year is leap year or not
year=int(input("enter year:"))
if year%100==0 and year%400==0:
    print("leap year")
elif year%100 !=0 and year%4==0:
    print("leap year")
else:
    print("not a leap year")
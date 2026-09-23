##variables
a=2 
print(type(a))
b=2.28 
print(type(b))
c="divas_gupta" 
print(type(c))
lis=[8,9,4,22]
print(type(lis))
h=True
print(type(h))
f=3+3j
print(type(f))

##input output and type casting

name=(input("enter your name:"))
age=(int(input("entere your age:")))
city=(input("enter you city name:"))
print("hello ,My name is",name)
print("I am ", age, "year old" )
print("I am from",city)

##operators
a=int(input("enter frist no:"))
b=int(input("enter second no:"))
print("addition of there two no. are",a+b)
print("subtrcation of there two no. are",a-b)
print("multiplication of there two no. are",a*b)
print("division of there two no. are",a/b)
print("modulus of there two no. are",a%b) #gives remainder 
print("exponent of there two no. are",a**b)

##Temperature Converter into fahrenheit
cel=float(input("enter temperature in Celsius:"))
far=(cel*9/5)+32
print("the conversion of",cel,"into fahrenheit is:",far)

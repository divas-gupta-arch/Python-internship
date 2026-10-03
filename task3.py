### list
fruits=["banana","apple","peach","mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(len(fruits))
fruits.append("date")
fruits[3]="grapes"
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
print(len(fruits))

### tuples
tup=(1,22,4,6,2,5,4,4,4)
print(tup[2])
print(tup[8])
print(tup[1:3])#slicing
print(len(tup))
print("frist accurace index is:",tup.index(2))#indes of 1st accurnce of item
print(tup.count(4))
#unpacking of tuple
def student():
    return ("divas",19,"divas@gmail.com")
info=student()
name,age,gmail=info
print(name)

### set
s={1,2,5,7,2,8,1,4,6}
p={6,2,1,4}
print(f"set is:{s};{p}")
s.add(22)
print(f"on adding single item in set:{s}")
p.update([20,30])
print(p)
print(f"on adding multiple item in set:{p}")
s.discard(2)
print(s)
print(f"union set are:{s|p}")
print(f"intersection of set are: {s&p}")
print("difference of set are:",s-p)
print(f"symmetric dofference:{s^p}")

### dictionary
student = {
    "name": "divas",
    "age": 20,
    "course": "computer science",
    "city": "meerut"
}
print(student)
print(student.get("age"))
student.setdefault("cgpa", "8.9")
print(student)
student.pop("city")
print(student)
print(student.keys())
print(student.values())
student.clear()
print(student)
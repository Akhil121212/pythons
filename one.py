'''print("Hello world")

first = input("Enter the first number:")
second = input("Enter the second number:")

sum = int(first) + int(second)
print("The sum is:" + str(sum))
'''
from dataclasses import replace
name = "Akhilesh Kumar"
'''
print(name.upper())
print(name.lower())
'''

'''
#find
print(name.find('sh'))
#replace
print(name.replace("Kumar","Tirumala"))

print("Ironman" in name)
print("Tirumala" in name)

print(5 *2)
print(5+2)
print(5-2)
print(5/2)
print(5//2)
print(5%2)  
print(5**2)

result = 2 + 3 * 5
print(result)
#hey this is line comment

#conditions
print(3>2)
print(3<2)
print(3<=2)
print(3==3)
print(3!=3)
print(2>3 or 2>1)
print(3>2 and 2>3)
print(not 2>3)

#If conditions
age = 30

if age >= 19:
    print("You are an adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("You are a teenager")    
else:
    print("you are a child")
print("Thank you")

#calculator
first = input("enter first number:")
operator = input("Enter operator (+,-,*,/,%):")
second = input("Enter second number:")
first = int(first)
second = int(second)
if operator == "+":
    print(first+second)
elif operator  == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("Invalid Operation")    
    
#Range

numbers = range(5)
print(numbers)     
           
#While loop

i = 5
while i >=0 :
    print(i * "*")
    i = i-1

i = 1
while i <=0 :
    print(i * "*")
    i = i+1
    
#for
for item in range(5):
    print(item+1)


#list[]

marks = [35,78,89,56]
print(marks[-2])
print(marks[1])
print(marks[-3])
print(marks[0:2])
print(marks[1:3])

for score in marks:
    print(score)

marks.append(99)
print(marks)   
marks.insert(0,99)
print(99 in marks)
print(marks)
print(len(marks))

marks = [98,76,88]

i= 0 
while i<len(marks):
    print(marks[i])
    i= i+1
marks.clear()
print(marks)   


students = ["Akhli","Tirumala","Adeeb","Sharan"]

for student in students:
    if student == "Tirumala":
        continue
    print(student)


for student in students:
    if student == "Tirumala":
        break
    print(student)    

#Tuple ()   
marks = (98,68,89,57,78)

print(marks.index(68))
print(type(marks))

#Set {}
marks = {98,67,78,89,78}
 
for score in marks:
    print(score) 

mark = {"english" : 98, "chemistry":87}
print(mark["chemistry"])  
mark["physics"] = 98
print(mark)
mark["physics"] = 99
print(mark)

#Functions
#1)In built Fun
#  inr(),str(),bool()
#2)Module Fun
import math
print(dir(math))
'''
#3) Fun
def print_sum(first,second=8):
    print(first+second)
print_sum(1)    
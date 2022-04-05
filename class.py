#Indentation
if 5 > 2:
   print("Five is greater than two!")

#Variables
x = 4 # x is of type int
#x = "Sally" # x is of type str
print(x)

#CAsting

x = 5
y = "John"
print(type(x)) 
print(type(y)) 

#Comments
#2myvar = "John"
#my-var = "John"
#my var = "John"

#Many values to MUltiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Unpacking variables
fruits = ["Apple","banana","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#OUTPUT VARIABLES
#first define the variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#if 5 > 2 :
   #print("Five is greater than two")
#if 5 > 2 :
      #print("Five is greater than two")

#One value to multiple variables

x=y=z="orange"
#print the variables separately
print(x)
print(y)
print(z)
#For numbers ,the "+" character works as a mathematical operator
x = 5
y = 10
print(x + y)

# if you try to combine a string and an int pythin will give you an error
x = 5
y = "John"
print(x,y)

#Global Variables
#they are used both inside and outsides of functions

#create a variable outside the fun ad use it inside the fun
x = "awesome"
def myfunc():
   print("Python is" + x)

myfunc()

#Area of a rectangle
x = 15
y = 10
def myfunc():
   print(x* y)

myfunc()

#create a var inside the fun with the same name as the global variable
#
x = "awesome"
def myfunc():
   x = "fantastic"
   print("python is" + x)
myfunc()
print("python is" + x)

def Milly():
   #if you use the global keyword the var becomes a global scope
   global y
   y = "Joy"

Milly()
print(y + " is great")

#integers
x = 1
y = "Selina"
z = bool
#this will print what type the var is

print(type(x))
print(type(y))
print(type(z))

#complex
#this are numbers and letters
#they are written with a"j" as the imaginary part
x = 2
y = "Selina"
z = bool
a = 5j
b = 5.9
c ="Joy"
print(type(x))
print(type(y))
print(type(z))
print(a, b, c)

#type conversion
x = 1 # int
y = 2.8 #float
z = 1j #complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)
 
 #convert from int to complex
 #you cant convert a complex into any other number type
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Number
#we use the "random module" to makwe a random number
import random
print(random.randrange(0,3))

#String
#Multiline strings
   #three double quotes
a ="""Lorem ipsum
lorem lorem lorem 
lorem lorem lorem"""
print(a)

#Slicing
#you return the range characters by using the "slice syntax"

b = "Hello, World!"
#You specify the start index and the end index separated by a colon to return part of a string
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#This is where my code begins
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
'''This is where
 my code ends'''
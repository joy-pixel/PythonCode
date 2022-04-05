#Define a set named sample_set
sample_set = {1.98,98.9,74.95,2.5,1, 16.3}

print(sample_set)

ss2 = sample_set.copy()
print(ss2)

#CONDITIONS AND IF STATEMENTS

a = 60
b = 90
#the if statement
#the if statement withot indentation will raise an error
if a >= b:
    print("a is greater than b")
    #if this is not true you use the else statement
else:
    print("b is greater than a")

#ELIF KEYWORD
#ELSE STATEMENT
a = 50
b = 50
if a < b:
    print("a is less thn b")
    #the elif statement is used if the previous conditions were not true
elif a > b:
    print("a is greater than b")
elif a != b:
   print("a is not equals to b")
else:
    print("a and b are equals")

#Using the "if","elif" and the "else" conditions to make a grading scheme
#define the variable
    marks = 59
    if marks <= 40:
        print("E")
    elif marks <= 50:
        print("D")
    elif marks <= 60:
        print("C")
    elif marks <= 70:
        print("B")
    else:
        print("A")


#SHORT HAND IF
#Define the variables
a = 2
b = 330
#this will have them executed in the same line
print("A") if a > b else print("B")

#SHORT HAND IF...ELSE
#define the variables
a = 2
b = 330
#this will execute them in one line
#one for if, one for else
print("A") if a > b else print("B")

#you can also have multiple stats on the same line
#by using the if else statement
#define the variables
a = 330
b = 330
print("A") if a > b else print("=") if a ==b else print("B")

#THE AND KEYWORD
#define the variables
a = 200
b = 33
c = 500
#by using the and keyword it will combine the statements
if a >b and c > a:
    print("Both conditions are true")

 #OR KEYWORD
a - 200
b = 33
c = 500
#this will help know which is greater than the other
#by help of the or keyword
if a > b or a > c:
    print("Atleast one of the conditions is true")
 

 #READ ABOUT FORM VALIDATION

 #Nested if
 #Using an if statement inside an if statement

x = 40
if x > 10:
    print("Above ten,")
#if this is not true we use the nested if to know otherwise
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


#the pass statement
#this is mostly used if you dont have content for the if statement
a = 20
b = 70

if b > a :
    #because this camt be empty we use the pass statement
    pass

#PYTHON LOOPS 
 #While Loop

#you have to define a n indexing variable
i = 1
#this will execute a set of statement so long a s the conditions are true
while  i < 101:
     print(i)
     #Always rem to increment i ,or else the loop will never stop
     i += 1 

     #Break Statement
i = 1
while i <6:
       print(i)
       if i == 3:
       #this will help stop the loop even if the whilke condition is true
         break
       i += 1

        #THE CONTINUE STATEMENT 
        #this stops the current iteration of the loop and continues the next
fruits = ["apple","banana","cherry"]
for x in fruits :
    if x == "banana":
        continue
    print(x)

    #THE RANGE FUN()
    #To loop through a set of code a specified number of times we use the range fun()
    for x in range(6):
        #this will return a sequence of numbers starting from 0 by default and increments 1 by default
      print(x)



# Else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
    

    #for loops

    fruits = ["apple", "banana","cherry"]
    for x in fruits:
        print(x)

        #Break statement
fruits = ["apple", "banana","cherry"]
for x in fruits:
  if x == "banana":
      break
  print(x)
  #NESTED LOOPS 
  #THIS IS A LOOP INSIDE A LOOP 
  adj  = ["red", "big", "tatsty"]
fruits = ["apple","banana","cherry"]

for x in adj:
    #THIS WILL BE EXECUTED ONE TIME ITERATION FOR THE OUTER LOOP
    for y in fruits:
        print(x,y)

        #THE PASS STATEMENT 
        #for loops cant be empty
        for x in [0,1,2]:
            pass

        #Functions 
        #this are block of codes which only runs when called 
        #CREATING FUNCTION 

        #We create a fun using the def keyword
def my_function():
      print("Hello from a function")

            #CALLING A FUNCTION
def my_function():
      print("Hello from a function")

my_function()

  
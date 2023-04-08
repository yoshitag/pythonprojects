#1Print (10pts)

#1. (3pts) Create a string variable (Hello Python!), print it.
strval1 = "Hello Python!"
print (strval1)

#2. (3pts) Create a string variable (Let’s write code.), print it.
strval2 = "Let's write code"
print (strval2)

#3. (4pts) Create a string variable (multi-line string) and print:

strval3 = '''Python is a high-level, general-purpose,
          dynamic programming language. Its design
          philosophy emphasizes code readability
          with the use of significant indentation.'''
print(strval3)

#2 Operator (15pts)
#Define a = 100, b = 9, c = 23, calculate the results of the following problems. (1pts)

a=100
b=9
c=23
#(2pts) Assign the result of (a + c)b to d, print d out.

d = (a + c)*b
print(d)
#(2pts) Print the integer part of d/b . (Hint: modulo operations)

modulo = d//b
print(modulo)

#(2pts) Print the result of c/b.

result = c/b
print (result)

#(2pts) Print the remainder part of d/b . (Hint: modulo operations)

remainder = d % b
print (remainder)
#(2pts) Print the result of a^2.

sqr = a ** 2
print(sqr)

#(2pts) Determining if b is unequal to c and print the True using logic operators.

if (b != c):
    print(True)

#(2pts) Determining if a is less or equal to b and print the False using logic oper- ators.

if (a <= b):
    print(False)

#3 List Practice (20pts)
#Please apply the required operations by the following order.
#1. (2pts) Define a 10-element list with consecutive integers starting from 0. Name it as list a. Hint: Use range()

list_a = list(range(10))
print(list_a)
#2. (3pts) Using extend to concatenate another list ([10, 11]) to list a, conclude the difference between .append() and .extend()

b = [10,11]
list_a.extend(b)
print("List after extend:", list_a) # extend adds all the elements of the list at the end of the list

#c= [10,11]
#a.append(c)
#print("List after append:", a) #append adds an item to the end of the list

#3. (3pts) Insert a string (’FE520’) to the second place of list a, and delete it after that.

list_a.insert (1,'FE520')
print(list_a)
del list_a[1]
print(list_a)
#4. (3pts) Create a sub-list from list a which doesn’t contain the last element of it. Name it list b.

list_b = list_a[0:11]
print(list_b)
#5. (3pts) Slice list b from the end to the 3rd element. Override the list b with this sub-list.

list_b = list_b[-9::]
print(list_b)
#6. (3pts) Create a copy of list b, name it list c. Concatenate list b and list c to form list d

list_c = list_b
list_d = list_c+list_b
print(list_d)
#7. (3pts) Reverse the sequence of list d.

list_d.reverse()
print(list_d)

#4 Practice Dictionary (20 pts)
#(2pts) Define a string of ‘python is an interpreted dynamic programming lan- guage’

strval4 = "python is an interpreted dynamic programming language"
print(strval4)
#(3pts) Create a list (list A) of single-character strings out of the above string in 1 (e.g., ’hello’->[’h’, ’e’, ’l’, ’l’, ’o’]).

list_A = list(strval4)
print(list_A)
#(8pts) Write a loop to count the number of each unique character (ignore spaces) into dictionary, where your keys are characters in the list A, and value is the count corresponding to each character. Your result should look like : {’h’: 1, ’e’: 1, ’l’: 2, ’o’: 1}.

dict = {}
for item in list_A:
    if item != ' ':
        dict[item] = list_A.count(item)
print(str(dict))
#(7pts) Print the characters which shows up more than 1 time. (Hint: use loop and if statement).

for key in dict:
    if dict[key] > 1:
        print (key, end =" ")
print("\n")
#5 Loop Practice: Sum (15 pts)
#Write a loop for calculate the average of a list.
#For example: if you have a list A = [1, 2, 3, 4, 5, 6], after your loop calculation,
#you need to get a total num equals to 3.5.

list_A = [1,2,3,4,5,6]
#list_A=[]
#n =int(input("Input the Size of the list:"))
#for i in range(0,n):
#    print ("Enter number at index:",i)
#    item = int(input())
#    list_A.append(item)
#print(list_A)
sum=0
for i in range(0, len(list_A)):
    sum = sum + list_A[i]
average = sum / len (list_A)
print(average)


#6 Control Flow Practice: Element-wise logical operations (20 pts)
#1. 10 pts) Given two same-length lists of bool-type variables (True/False),
# you need to implement the element-wise and, or, and not operations.
# Element-wise means the operations are applied to each pair of two element,
# and the results form another list. In the following sample code,
# the first element in result and is False because x[0] and y[0]
# equals False (True and False == False).
# Complete the following code to obtain the three lists.
# return three lists: result_and, result_or, result_not_x which are
# respectively the result of element-wise AND, element-wise OR,and element-wise NOT
# result_and is [False, True, False, False, False, False, True]
# result_or is [True, True, True, True, True, False, True]
# result_not_x is [False, False, True, True, False, True, False]

x = [True, True, False, False, True, False, True]
y = [False, True, True, True, False, False, True]

#zipped = zip (x,y)
#print(list(zipped))

result_and = [a and b for a,b in zip(x,y)]
print(result_and)
result_or = [a or b for a,b in zip(x,y)]
print(result_or)
result_not_x = [not a for a in x]
print(result_not_x)

#2. (10 pts) Implement another operation: given a list of bool-type variables.
# If True takes 40% or more of the total number of element of this list,
# give True as the result, otherwise give False. For an example,
x = [True, True, False, False, True]
y = [True, False, False, False, False]

    # your code gives True for x, as True takes 3/5 (60%>=40%)
    # your code gives False for y, as True takes 1/5 (20%<40%)
    # Use the following code to generate a list of True/False,
    # Test your code with this list and report the result.
    #Use FOR loop to determine True or False for list z.

from random import randint
z = [bool(randint(0,1)) for _ in range(40)]# This function is generating a random list of 40 true and false
count =0
for i in z:
    if i ==True: count+=1
if (count/40) >=.4: print(True)
else: print(False)

#(Bonus 5pt) Investigate and understand how list z is created.
# Write another block of code to do the same task without FOR loop
# (one line of code is sufficient for this).

if (y.count(True)/len(y) >= .4):
    print(True)
else: print(False)


#Use FOR loop to determine True or False for list z.
#(Bonus 5pt) Investigate and understand how list z is created.
#Write another block of code to do the same task without FOR loop
#(one line of code is sufficient for this).





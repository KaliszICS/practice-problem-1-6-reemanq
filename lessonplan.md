# Lesson plan
  
'''
	Error Checking
	Author: Mr.Kalisz
	Date Created: September 16, 2021
	Date Last Modified: February 14, 2022
'''

#Three types of errors - Syntax, Runtime, Logical

#Syntax - not following the basic rules of your code.
#This is checked BEFORE your code actually executes.  The whole code is checked, then it is started.

#Examples:
#Spelling mistakes
#accidental indentation of your code
#incorrect punctuation
#forgetting quotes, starting or ending
#incorrect number of brackets - too many open or close brackets


#prin("hello")

#	sword = "hello"
#num = 4 = 5
#word = "hello
#num = (4 * (5 + 4) #Error will always appear as if it is on the next line of code


#Runtime errors - These are checked WHILE your code is run

#Examples
#division by zero
#performing an operation on incompatible types
#using an identifier which has not been defined
#identifier is a variable or a function


num3 = 7
print(4) #Proving its a runtime error
#print(num) #num does not exist
#num2 = 0
#num = 5 / num2
#word = "hello"
#word = word / 7


#Logical errors - These are errors that dont stop your code from running but give a different result than desired

#Examples
#the code output is different from what you want
#Spelling in your string value is incorrect
#Using the wrong variable
#Using the wrong type of division (/ or //)
#Incorrect use of order of operation

#assign 4 to num and add 3 and output.
num = 4
num2 = 7
print (num2)


#Add 2 to 5, then multiply by 10
print(5 + 2 * 10) #25
print((5 + 2) * 10) #70
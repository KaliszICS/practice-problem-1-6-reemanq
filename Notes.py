'''
	File Name: Errors
	Author: Mr. Kalisz
	Date Created: Sept 24, 2024
	Date Last Edited: Sept 24, 2024
'''

print(5)

#Errors

#Syntax Errors - You didn't follow basic programming rules of python
#Happen before your code runs

#num = 3 = 5
'''
File "/workspaces/ics2o1-02-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 15
    num = 3 = 5
          ^
SyntaxError: cannot assign to literal
'''

# num = (3 + (5-4) * 5
'''
  File "/workspaces/ics2o1-02-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 23
    num = (3 + (5-4) * 5
          ^
SyntaxError: '(' was never closed
'''

# Runtime Errors - Errors will be based on a value
# Runtime errors happen while the code is running

num = 0

# print(5 / num)
'''
  File "/workspaces/ics2o1-02-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 34, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
'''

print(3 + "word")
'''
  File "/workspaces/ics2o1-02-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 44, in <module>
    print(3 + "word")
          ~~^~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

# Logical Errors - Program executes flawlessly but with the wrong outcome
#Error that happens "after" it runs - based on the result
#

#Add 2 and 2 together, output the result
print(2 + 1) #Wrong values

#Add 3 and 5 together then multiply by 2, output the result
print(3 + 5 * 2) #Order of operations
#print((3 + 5) * 2) #fixed

#Add 2 and 2 then multiply by 1, output the result
print(2 + 2 * 1) #Order of operations
#produces the same answer even though its wrong

# Add 2 and 2
print(2 + 2) #Doesn't asked to be output
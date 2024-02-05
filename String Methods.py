#len - returns the number of characters in a string.

course = 'Python for Beginners'
print (len(course)) #show total 

#upper - returns the string in upper case.
#upper - returns the string
#upper - is a (.)method  NOT a function

print (course.upper()) #2nd print the string in upper case

print (course.find('o')) #method showing index of the character

print (course.replace('Beginners', 'Absolute Beginners')) #method to replace the string (or part of the string)

print (course.title()) #method to print the string in evry first leter in capital case

print ('Python' in course) #looking for 'string' in course and return (print in boolean) True or False 


#when you run this code, you will see that output
"""
20 
PYTHON FOR BEGINNERS
4
Python for Absolute Beginners
Python For Beginners
True
"""
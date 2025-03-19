#len - returns the number of characters in a string.
#.upper - is a (.)method  NOT a function

course = 'Python for Beginners'

print (len(course)) #show total 
#Example of python output 20 

print (course.upper()) #2print the string in upper case
#Example of python output PYTHON FOR BEGINNERS

print (course.lower()) # print the string in lower case
#Example of python output python for beginners

print (course.find('o')) #method showing index of the character
#Example of python output 4

print (course.replace('Beginners', 'Absolute Beginners')) #method to replace the string (or part of the string)
#Example of python output

print (course.title()) #method to print the string in evry first leter in capital case
#Example of python output Python for Absolute Beginners

print ('Python' in course) #looking for 'string' in course and return (print in boolean) True or False 
#Example of python output True

print (course.split()) #method to split the string into a list
#Example of python output ['Python', 'for', 'Beginners']
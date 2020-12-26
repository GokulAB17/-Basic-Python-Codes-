


# Functional programming is all about expressions. 
  # We can say that the Functional programming is an expression oriented programming.



# Expression oriented functions of Python provides are:

    # map(aFunction, aSequence)
    # filter(aFunction, aSequence)
    # reduce(aFunction, aSequence)
    # lambda
    # list comprehension


# By using Python you to create anonymous function 
   # i.e function having no names using a facility called lambda function.
   
# lambda is one tool were we can use instead of 'def' for building function or building function objects.
   
# The lambda function is to create anonymous(unknown) without a name.
   # Lambda functions are mainly used in combination with the functions filter(), map() and reduce().

# Like def, the lambda creates a function to be called later. 
 # But it returns the function instead of assigning it to a name. 
  # This is why lambdas are sometimes known as anonymous functions.  
   
   
   
# lambda operator can have any number of arguments, but it can have only one expression.
  # It cannot contain any statements and it returns a function object which can be assigned to any variable. 

#  function i.e function having no names using a facility called lambda function. 
    # lambda functions are small functions usually not more than a line.
    # It can have any number of arguments just like a normal function.
# lambda is designed for coding simple functions, and def handles larger tasks.
     
    
# inorder to get oneline syntax as we use lambda(anonymous function).
 
   #  Syntax of Lambda Function in python
    
   #--- lambda arguments: expression---#
    
lamb = lambda x: x ** 2
print(lamb(5))


def func(x): return x ** 4
print(func(4))

  
double = lambda x: x*6    
print(double(5))


# f is assigned the function object the lambda expression creates. 
# This is how def works, too. But in def, its assignment is an automatic

def f(x, y, z): return x + y + z
f(4, 60, 300)

# Default arguments in lambda

title = (lambda a = ' mango', b = '  grapes', c = ' apple': a + b + c)
title('mango ', 'grapes')


def writer():
    title = 'king'
    name = (lambda x:title + ' ' + x)
    return name
who = writer()
who('John')





L = [lambda x: x ** 3,lambda x: x ** 10,lambda x: x ** 15]
for f in L:
    print(f(3))
 
    
# In the above example,a list of three functions was built up by embedding 
  # lambda expressions inside a list. A def won't work inside a list literal
   # because it is a statement, not an expression. If we really want to use def for the same result, 
  # we need temporary function names and definitions outside:

def f1(x): return x ** 2
print(f1(3))
def f2(x): return x ** 3
print(f2(4))
def f3(x): return x ** 4
print(f3(5))

# using dictionarie formate 


key = 'quadratic'
{'square': (lambda x: x ** 3),
     'cubic': (lambda x: x ** 6),
     'quadratic': (lambda x: x ** 4)}[key](20)


key = 'kiran'
{'kalyan':(lambda y: y ** 4),
 'kiran': (lambda y: y ** 5),
 'karthik': (lambda y: y ** 6)}[key](10)



# If we know what we're doing, we can code most statements as expressions:


min = (lambda x, y: x if x < y else y)
min(100*10, 200*10)

max = (lambda x, y: x if x >y else y)
max(100*10, 200*10)


  # sample as above without lambda functions the output is same.

min(100*10,200*10)

 # lambda with built-in function sorted(): 
    
         # sorted(iterable[, key][, reverse])

death = [
    ('James', 'john', 50),
    ('Jack', 'charry', 29),
    ('jacky', 'charms', 48),
    ('karthik','navin',60)
]
sorted(death, key=lambda age: age[1])



# Mostly lambda functions are passed as parameters to a function 
 # which expects a function objects as parameter like map, reduce, filter functions

# A parameter is a variable in a method definition.
 #  When a method is called, the arguments are the data you pass into the method's parameters.
  #  Parameter is variable in the declaration of function. 
   # Argument is the actual value of this variable that gets passed to function.


# map functions expects a function object and any number of iterables like list, dictionary, etc. 
 # It  will executes the function object for each element in the sequence and returns 
   # the list of elements that modified by the function object.

  #  map(function_object, iterable1, iterable2,...) #
# the reduce function reduces a list to a single value by combining elements via a supplied function. 

# The filter() method constructs an iterator from elements of 
  # an iterable for which the  function returns true.


  #-----filter(function, iterable)----#


def multiply2(x):
    return x * 2
map(multiply2, [1, 2, 3, 4])

map(lambda x : x*2, [1, 2, 3, 4])


map_output = map(lambda x: x*2, [2, 4, 6, 8])
print(map_output)
list_map_output = list(map_output)
print(list_map_output)


list_a = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 2 == 0, list_a) # filter object <filter at 0x4e45890>

even_num = list(filter_obj) # Converts the filter object to a list

print(even_num)


list_a = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 1 == 0, list_a) # filter object <filter at 0x4e45890>

even_num = list(filter_obj) # Converts the filter object to a list

print(even_num)




list_a = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 2 != 0, list_a) # filter object <filter at 0x4e45890>

odd_num = list(filter_obj) # Converts the filter object to a list

print(odd_num)


# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)



# list of alphabets
alphabets = ['k', 'a', 'r', 'e', 'i', 'j', 'm']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['k', 'a', 'r', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)


#  Reduce function is defined in “functools” module.
#  importing functools for reduce() 

import functools 
from functools import reduce
reduce( (lambda x, y: x * y), [1, 6, 3, 4] )
reduce( (lambda x, y: x / y), [1, 2, 3, 4] )





# List comprehensions aren’t the only way to work on lists. Various built-in functions 
 # and lambda functions can create and modify lists in less lines of code.

# ---list_variable = [x for x in iterable]---#

# ---[expression for item in list]---#
 # for example : letter for letter in human
   # Here letter is Expression.
   # item is letter.
   # list is human.

k_letters = [ letter for letter in 'human' ]
print( k_letters)


squares = [x**2 for x in range(10)]
print (squares)

number_list = [ x for x in range(40) if x % 2 == 0]
print(number_list)


numbers = range(10) # Even Squares
new_list = []
for n in numbers:
    if n%2==0:
        new_list.append(n**2)
print(new_list)


numbers = range(10) # Odd squares
new_list = []
for n in numbers:
    if n%2!=0:
        new_list.append(n**2)
print(new_list)

new_list = [n**2 for n in numbers if n%2==0]
print(new_list)

new_list = [n**2 for n in numbers if n%2!=0]
print(new_list)







# Tuples #

# creating tuples
# a) python tuple packing
# b) pyhton tuple unpacking
# c) creating tuple with a single item.


# creating tuple
totalages = (40,39,12)
print(type(totalages))

simple= ('python','program','value')
print(type(simple))


number = ['python','java','coding']
print(type(number))

# python tuple packing
totalages = 40,39,12
print(totalages)
type(totalages)
# pyhton tuple unpacking
totalages = (90,30,40,20,25)
apple,b,c,d,e = totalages
b
c
e
apple

# creating tuple with a single item
a = (2)
type(a)
b=(3,)
type(b)
b
a = (2,)*3
a
type(a)
a=("kiran")
a
type(a)
b = ("karthik",)
type(b)

value=("3,4.5,complete",)
print(type(value))

c = (2,3.5,'singer',)
print(c)
type(c)



# Accessing python tuple
# a) Accessing Entire tuple

totalages
a
c
b

# b) Accessing a single item
totalages[1]
c[2]
b



# Slicing a tuple
totalages = (20,30,40,50,70,80,26,45)
totalages[2:5]
totalages[2:]
totalages[:4]

karthik = (1,2,3,4,5,6,7)
karthik[1:5]
set = ('a,b,c,d,e,f')
set[1:3]
set[2:]
set[:3]


fruits = ('mango','apple','bannaa')
print(fruits)
len(fruits)

# functions in tuple
my_tuple=(2344,45,66,88)
len(my_tuple)
a = (2,4,5,8,1,0,7,10,15)
max(a)
min(a)
max('Hi','here','Their')
max("vineeta","chandra","karthik")
max("Three","Five","one")

# The any() function returns True if any item in the given input are true, 
 # otherwise it returns False.
any()

any(('','',''))
any(('',3,''))
any(('one','spy',''))
any([0,1,2,3,4])
any(['find','finds','finding'])
any(['find','finds','finding',''])
any([0,0,0,0])
any([])
value=['king','queen','prince','emperor']
any(n in 'king and prince' for n in value)
any(n in 'king and queen' for n in value)
any(n in 'send' for n in value)
any(n in 'king' and 'emperor' for n in value)


locals()['__builtins__']
while True:
    try:
        x = int(input("Please enter a valid number: "))
        print ("hello")
        break
    except ValueError:
        print(" Their was no valid number.  Try again...")

try:
    x=2+5
except:
        print("it will not work")
else:
        print("it will run")


a = (0,2,4,3,6,9,10,16,13)
sorted(a)

list1 = [1,2,3]
list1
tuple(list1)
string1 = ('one','praveen','ashok')
print(string1)
tuple(string1)
print(list1)



a = (1,2,350,60,47,90,100,200)
a.index(100)

# operators in tuple

# membership

'a' in tuple("python")
'a' in tuple("karthik")
'e' in tuple("elephant")
'e' in tuple("important")
# concatinating in python tuple

(20,40,38,10) + (1,3,4,5,6)
(20,40,38,10) + ('kishore','ashok','shreya','kiran','vineeth')

# Logical operators

(20,40,38,10)>(1,3,4,5,6)
(20,40,38,10)<(1,3,4,5,6)



# Identity



a=(1,2)
id(a)
b=(1,3)
id(b)
b is a
a is b
a is not b
c=50
id(c)
d=50
d
c is d
d=50
id(d)
c is d

karthik1 = '1,2,3'
karthik1
id(karthik1)
kishore1 = '1,2,3'
kishore1
id(kishore1)
karthik1 is kishore1

karthik1 in kishore1

karthik1 = 1,2,3
karthik1
kishore1 = 1,2,3
kishore1
karthik1 is not kishore1

karthik1 = 1,2,3
karthik1
kishore1 = 1,2,3
kishore1
karthik1 is kishore1



karthik1 = 'its my name'
kishore1 = 'its my name'
karthik1 in kishore1
karthik1=kishore1
karthik1 is kishore1



# Iterating with for loop in tuple
#
# Nested tuple

a = (1,2,3)
a= (1,2,(2,3))
a = ((1,2,3),(4,(5,6)))
a[1]
a[1][1]
a[1][1][1]


# some string characters in python tuple

names = 'python','scripting','coding','multimedia','business'
print(names)
print(names[1])
print(names[4])
print(names[2])
print('most trending business in society:-' + names[2]);
print(names[1:4])



colors = ('red','blue','black','white','yellow')
print(colors)


# Exceptions in python #
# Exceptions #
# Assertions #
# When we run a program error happens during execution,whenever error occurs
 # Python generates exception that could be handled 

# An assertion is a sanity-check(calculation true) that you can turn on or 
 # turn off when you are done with your testing of the program.
# The goal of using assertions is to let developers 
 # find the likely root cause of a bug more quickly. 
 # An assertion error should never be raised unless there’s a bug in your program.


anil = 'coming to office'
print(anil)

print(0/0))
print(0/0)
locals()['__builtins__']

x = 15
if x > 10:
    raise Exception('x should not exceed 10 . the value of x was: {}'.format(x))


try: 
    print (1/0)
except ZeroDivisionError:
        print("You can't divide by zero, you're silly.")

while True:
    try:
        x = int(input("Please enter a  valid number: "))
        print ("hello")
        break
    except ValueError:
        print(" Their was no valid number.  Try again...")
        
try:
    x = 2+5
except:
    print('it does\'t work!')
else:
    print('will run when there is no exception')

try:
    y =10
    print('True')
except:
    print('wrong information')



#Demo1
def greet(name):
    """This function greets to
    the person passed in as
    parameter"""
    print('Hello, ' + name + '. Good morning!')

greet('Amit')

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))


#Demo2
def greet(name, msg):
    """This function greets
    to the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")

def greet2(name, msg = "Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If message is no provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", name + ', ' + msg)

greet2("Kate")
greet2("Bruce", "How do you do?")
greet2(name = "Rohit", msg = "Are you okay?")

def greet3(*names):
    """This function greets all
    the person in the names tuple"""
    for name in names:
        print("Hello", name)

greet3("Monica", "Luke", "Steve", "John")


#Demo3
def no_return(x,y):
    c = x + y
res = no_return(4,5)
print(res)

def empty_return(x,y):
    c = x + y
    return
print(empty_return(4,5))

def return_sum(x,y):
    c = x + y
    return c
print(return_sum(4,5))

def squares():
    sq = []
    for i in range(10):
        sq.append(i*i)
    return sq
print(squares())


#Demo4
def f():
    s = "Python"
    print(s)
f()

def fun():
    s = "Perl"
    print(s)

s = "Python"
fun()
print(s)

def foo():
    global s
    s = "Perl"
    print(s)
s = "Python"
foo()
print(s)


#Demo5
my_list = [4, 7, 0, 3]
for val in my_list:
    print(val)

my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))

def my_gen():
    n = 1
    print("This is printed first")
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed last")
    yield n

a = my_gen()
next(a)
next(a)
next(a)

#Demo6
sum = lambda arg1, arg2: arg1 + arg2;
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

def fahrenheit(T):
    return((float (9)/5)*T + 32)
temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
print(temperatures_in_Fahrenheit)

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)
print("A")

fahrenheit(10)

x = 10
y = 20
from _functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
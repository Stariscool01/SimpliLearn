#1
x,y = 5,6
if x > y:
    print("x is greater")
else:
    print("y is greater")
print("have a nice day")

#2
x = 10                  #integer
y = 3.14                #float
strg = 'Hello'          #string
sw = True               #bool

print(x)
print(y)
print(strg)
print(sw)

print(x, 'is of type', type(x))

#List
a = [5, 10, 15, 20, 25, 30, 35, 40]
print('a[2] = ', a[2])
print('a[0:3] = ',a[0:2])

#Tuple
t = (5, 'program', 1+3j)
print('t[1] = ', t[1])
print('t[0:3] = ', t[0:3])

#Sets
c = {5, 2, 3, 1, 4}
print('c = ', c)
print(type(c))

#Dictionary
d = {1:'value', 'key':2}
print(type(d))
print('d[1] = ', d[1])
print("d['key'] = ", d['key'])

#3
s = 'Hello World!'
print('s[4] = ', s[4])
print('s[6:11] = ', s[6:11])

#rough
a = 25
print(a % 3 == 0 and a % 5 == 0)

#4 (Operators)
x = 15
y = 4
print('x + y = ', x + y)
print('x - y = ', x - y)
print('x * y = ', x * y)
print('x / y = ', x / y)
print('x // y = ', x // y)
print('x ** y = ', x ** y)

x = 10
y = 12
print('x > y is ', x < y)
print('x < y is ', x > y)
print('x == y is ', x == y)
print('x != y is ', x != y)
print('x >= y is ', x >= y)
print('x <= y is ', x <= y)

x = True
y = False
print('x and y is ', x and y)
print('x or y is ', x or y)
print('not x is ', not x)
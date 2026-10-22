#Demo1
num = 3
if num > 0:
    print(num, ' is a positive number.')
print('This is always printed.')

num = -1
if num > 0:
    print(num, ' is a positive number.')
print('This is also always printed.')

num = 3.4
if num > 0:
    print('Positive number')
elif num == 0:
    print('Zero')
else:
    print('Negative number')

#nested if
num2 = float(input('Enter a number: '))
if num2 >= 0:
    if num2 == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative number')


#Demo2
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sums = 0
for val in numbers:
    sums = sums + val
print('The sum is ', sums)

sums = 0
i = 1
n = 10
while i <= n:
    sums = sums + i
    i = i+1
print('The sum is ', sums)
# #Demo1
# num = 3
# if num > 0:
#     print(num, ' is a positive number.')
# print('This is always printed.')

# num = -1
# if num > 0:
#     print(num, ' is a positive number.')
# print('This is also always printed.')

# num = 3.4
# if num > 0:
#     print('Positive number')
# elif num == 0:
#     print('Zero')
# else:
#     print('Negative number')

# #nested if
# num2 = float(input('Enter a number: '))
# if num2 >= 0:
#     if num2 == 0:
#         print('Zero')
#     else:
#         print('Positive number')
# else:
#     print('Negative number')


# #Demo2
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sums = 0
# for val in numbers:
#     sums = sums + val
# print('The sum is ', sums)

# sums = 0
# i = 1
# n = 10
# while i <= n:
#     sums = sums + i
#     i = i+1
# print('The sum is ', sums)


# #Demo3
# for val in 'string':
#     if val == 'i':
#         break
#     print(val)
# print('The end')

# for val in 'string':
#     if val == 'i':
#         continue
#     print(val)
# print('The end')

# #Demo4
# to_be_guessed = 5
# guess = 0
# while guess != to_be_guessed:
#     guess = int(input('New number: '))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print('Number is too large')
#         elif guess < to_be_guessed:
#             print('Number is too small')
#     else:
#         print("Sorry you're giving up")
#         break
# else:
#     print("Congratulations. You made it! ")

#Demo4B
edibles = ["ham", "meat", "eggs", "nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious, " + food)
else:
    print("I am so glad! No spam!")
print("Finally, I finished stuffing myself")

#Demo5
genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print('I like', genre[i])

i = sum = 0
while i <= 4:
    sum += 1
    i = i+1
    print(sum)

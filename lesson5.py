arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[1])
print(arr[2])

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
num_brands = len(brands)
print(num_brands)

add = ["a", "b", "c"]
add.append ("d")
print(add)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4]
colors.remove ("blue")
colors.pop(3)
print(colors)

#Demo2
my_list = ['p', 'r', 'o', 'b', 'e']
print(my_list[0])
print(my_list[2])

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
print(my_list[2:5])

odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)

odd = [1, 9]
odd.insert(1, 3)
print(odd)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
del my_list[2]
print(my_list)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list.remove('p')
print(my_list)

#Demo3
my_tuple = (1, 'Hello', 3.4)
print(my_tuple)

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[-1])

my_tuple = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
print(my_tuple[1:4])

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('p'))

for name in ('Kate', 'John'):
    print('Hello', name)


#Demo4
my_dict = {1: 'applle', 2: 'ball'}
print(my_dict)

my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])

my_dict = {'name': 'Jack', 'age': 26}
my_dict['age'] = 27
print(my_dict)

squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.pop(4))
print(squares)

squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print(1 in squares)

squares = {1:1, 3:9, 5:25, 7:49, 9:81}
for i in squares:
    print(squares[i])

squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print(len(squares))


#Demo5
my_set = {1, 2, 3}
print(my_set)

my_set = {1, 3}
print(my_set)
my_set.add(2)
print(my_set)

my_set = {1, 3, 4, 5, 6}
print(my_set)
my_set.discard(4)
print(my_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A|B)      #Union: | (pipe)
print(A&B)      #Intersection: & (ampersand)
print(A-B)      #Difference: - (minus sign)


#Demo6
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

h_letters = [ letter for letter in 'human' ]
print(h_letters)

number_list = [ x for x in range(20) if x % 2 == 0 ]
print(number_list)

num_list = [ y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

obj = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)]
print(obj)
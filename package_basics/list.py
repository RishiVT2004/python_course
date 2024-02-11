'''mutable in nature'''

list_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in list_name:
    print(i, end="->")
print()

print(list_name[1:5])
print(list_name[:4])
print(list_name[2:])
print()

for x in list_name[:4]:
    for y in list_name[5:]:
        print(f'{x, y}', end=" ")
    print()

number = ['1', '4', '2', '5', '3']
max_num = number[0]
for x in number:
    if max_num < x:
        max_num = x
print(max_num)

'''2-d list '''
matrix = [[1, 2, 3],
          [1, 4, 9],
          [1, 8, 27]
          ]

for row in matrix:
    for x in row:
        print(x)
    print()

'''list method'''

num = [1, 8, 5, 3, 6, 0]
num.insert(3, 2)  # adds object in given index
num.sort()  # sort the list in ascending order
num.reverse()  # makes the list in reverse
num.pop()  # remove last item
num2 = num.copy()  # copy the initial list
num.remove(2)  # remove given item
num.index(3)  # prints index of item
num.count(1)  # returns no. of time the element is list
print(num)
print(4 in num)  # checks if num is in list(returns in boolean)
num.clear()  # erases everything

num = [1, 1, 1, 4, 4, 5, 2, 3, 2]

for x in num:
    if num.count(x) > 1:
        num.remove(x)
print(num)

num = []
n = int(input('enter size of list '))
for i in range(n):
    j = input()
    num.append(j)
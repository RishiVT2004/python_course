
def print_odd(n1, n2):
    count = 0
    for item in range(n1, n2):
        if item % 2 != 0:
            print(item)
            count += 1
    print(f"no of odd no {count}")


(print_odd(2, 11))



def sum_list(list):
    sum = 0
    for item in list:
        sum += item
    print(sum)


l1 = [10, 20, 30, 40, 50]
sum_list(l1)

for x in range(5):
    for y in range(10):
        if x >= y:
            print(f'{x,y}')
    print()

set1 = [5,2,5,2,2]
for x in set1:
    print('x'*x)
print()

set2 = [6,3,6,3,6]
for y in set2:
    print('y'*y)


'''
 def calc(num1, num2):
    command = str(input(f'enter operator : '))
    if command == '+':
        print(f'result{num1 + num2}')
    elif command == '-':
        print(f'result is {num1 - num2}')
    elif command == '*':
        print(f'result is {num1 * num2}')
    elif command == '/':
        print(f'result is {num1 / num2}')
    else:
        return 'invalid'


n1 = float(input('enter number 1: '))
n2 = float(input('enter number 2: '))

calc(n1, n2)
'''
import math

'''

try:
    def bonus_calc(hours):
        salary = float(input(f'enter salary : '))
        if hours<100:
            return salary
        elif 100<hours<150:
            print(f'{salary*0.2}')
        else:
            print(f'{salary*0.33}')
except ValueError:
    print(f'invalid value')


bonus_calc(180)


'''

'''''' -> docstrings != comments , can be printed by python
'''


def square(n):
    '''this is square function (always below the defn of function)'''
    print(n ** 2)
    '''this docstring is not printed'''


square(10)
print(square.__doc__)

'''pep - 8 -> makes python readable and makes it effiecient '''


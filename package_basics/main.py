# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def cal_bonus(salary, time):
    bonus = 0
    if time <= 160:
        print(f'salary is {salary}$')
    elif 160 < time < 180:
        bonus = salary * 0.2
        print(f'salary is {salary + bonus}$')
    elif 180 < time < 200:
        bonus = salary * 0.3
        print(f'salary is {salary + bonus}$')
    elif time > 200:
        hour_excess_coefficient = (time - 200)*0.01
        bonus = (0.4 + hour_excess_coefficient) * salary
        print(f'salary is {salary + bonus}$')


cal_bonus(150000,160)
cal_bonus(150000,170)
cal_bonus(150000,192)
cal_bonus(150000,208)



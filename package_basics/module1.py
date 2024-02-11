import math
class Health:
    def calc_pound(weight):
        weight_pound = weight*2.2
        print(f'weight of person in kg is {weight_pound}')

    def calc_BMI(weight,height):
        bmi = weight/math.pow((height/100),2)
        print(f'BMI of person is {bmi}')

class Bonus:
    def calc_bonus(salary,time):
        if time <= 160:
            print(f'no bonus')
        elif 160<=time<=180:
            print(f'bonus is {salary*0.15} $ ')
        else:
            print(f'bonus is {salary*0.25}')        

class Max:
     
     def find_max(numbers):
        max = numbers[0]
        for i in numbers:
            if i > max:
                max = i
        print(f'max element in list is {max}')

        



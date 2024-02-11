'''
Inheritence 

'''

'''
class Schedule:
    def study(self, subject, time):
        print(f'study {subject} for {time} hour')


class Break(Schedule):
    def take_break(self, time):
        print(f'take a break of {time} hours')


s1 = Schedule()
s2 = Break()
s1.study('physics', 2)
s2.take_break(1)
'''

'''
class Task1:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f'run {self.name}')

    def walk(self):
        print(f'walk {self.name}')


class Task2(Task1):
    def sleep(self):
        print(f'sleep {self.name}')


t = Task2('rishi')
t.run()
t.sleep()
t.walk()

v = Task1('adam')
v.walk()
v.run()
v.sleep()
'''

'''MULTILEVEL INHERITANCE'''

'''
class list_score:
    def __init__(self, dsa, dbms, os):
        self.dsa = dsa
        self.dbms = dbms
        self.os = os


class mark_score(list_score):
    def print_mark_score(self):
        print(f'mark in DSA is {self.dsa}')
        print(f'mark in DSA is {self.dbms}')
        print(f'mark in DSA is {self.os}')


class total_score(mark_score):
    def tot_score(self):
        print(f'{self.dsa + self.dbms + self.os}')


A = total_score(10,12,9)
A.tot_score()
A.print_mark_score()
print(A.dsa)
'''

'''Multiple Inheritence


class is_student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def student_mark(self):
        print(f'{self.name} has received {self.mark}')


class S1(is_student):
    def print_age(self):
        age = int(input())
        print(f'{self.name} is {age} years old')


class S2(is_student):
    pass


student1 = S1('rishi', 100)
student2 = S2('ankit', 90)
student1.print_age()
student1.student_mark()
student2.student_mark()

'''
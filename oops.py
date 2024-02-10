'''
 oops
'''

'''
Inheritence 

class Task_List:
    def walk(self, name):
        print(f'walk {name}')

    def run(self, name):a
        print(f'run {name}')

    def swim(self, name):
        print(f'swim {name}')


# to add walk method in this class we use inheritance
class Task1(Task_List):
    def sleep(self):
        print(f'sleep')


class Task2(Task_List):
    pass


t1 = Task1()
t2 = Task2()
t1.swim('rishi')
t1.sleep()
t2.walk('rishi')

'''
class Schedule:
    def study(self,subject,time):
        print(f'study {subject} for {time} hour')

class Break(Schedule):
    def take_break(self,time):
        print(f'take a break of {time} hours')


s1 = Schedule()
s2 = Break()
s1.study('physics', 2)
s2.take_break(1)

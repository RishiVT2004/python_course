'''Inheritence'''
class Info:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'you are allowed to talk : {self.name}')


i1 = Info('rishi')
print(i1.name)
i1.talk()

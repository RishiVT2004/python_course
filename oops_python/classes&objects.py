'''
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        print(f'name')

    def age(self):
        print(f'age')


user1 = User('rishi', 19)
user2 = User('ashish', 20)
print(f'user name 1 : {user1.name}')
print(f'age of user 2 : {user2.age}')
# self is used to reference the current object

user1.x = 'rishi'
user2.x = 'ihsir'
print(user1.x, user2.x)

'''

class Info:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'you are allowed to talk : {self.name}')


i1 = Info('rishi')
print(i1.name)
i1.talk()



class Player:
    def __init__(self, name, score, position):
        self.name = name
        self.score = score
        self.position = position

    def player_info(self):
        print(f'the player named {self.name} has scored {self.score} points and has achieved {self.position} position')


player1 = Player('rishi',95,3)
player1.player_info()

import random
import time

list_operators = ['+','-','*','/']
MIN = 1
MAX = 10
no_problems = int(input("enter no. of questions to be gernerated : "))

def create_problem():
    left = random.randint(MIN,MAX)
    middle = random.randint(MIN,MAX)
    right = random.randint(MIN,MAX)
    correct = 0

    operator1 = random.choice(list_operators)
    operator2 = random.choice(list_operators)

    question = str(left) + " " + operator1 + " " + str(middle) + " " + operator2 + " "+str(right)
    answer = eval(question) #evaluate string as python code
    
    print(question)
    user_answer = float(input(f'enter answer to above question : '))

    if user_answer == answer:
        print(f'correct answer')
        correct+=1  
    else:
        print(f'wrong answer')
    


input('Press to start')
print('---- QUIZ STARTED ----')

start_time = time.time()


for x in range(1,no_problems+1):
    print(f'Problem number {x} : ')
    create_problem()
    print()

end_time = time.time() #timer 

print('------------')

print(f'you finished the quiz in {round(end_time-start_time,3)} seconds ')




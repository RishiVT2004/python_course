'''strings'''
name = 'rishi mishra'
print(name.upper(), name.lower(), name.capitalize(), name.isalpha(), name.isdigit(), name.isalnum())
print(name.index('r'), name[0:7], name[:8], name[4:])
print(name.count('i'), name.replace('r','d'), name.find('s'))
print('rishi'in name)

'''logical operator'''

sal = float(input("salary : "))
print(sal > 100 or sal < 50)
print(sal > 100 and sal >200)
print(sal > 100, not sal>100)


weight = float(input("weight: "))
unit = input("kg (k) or lbs(l) ")
if unit == 'k':
    print(f"weight in pounds : {weight*2.2}")
elif unit == 'l':
    print(f"weight in kg: {weight*0.45}")
else:
    print("0")

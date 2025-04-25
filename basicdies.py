import random
a=input("roll the dies(yes,no)")
numbers = [1, 2, 3, 4, 5,6]
sample = random.sample(numbers, 1)
if a=='yes':
   print('the number that poped is',sample)
else:
    print('pls roll the dies')

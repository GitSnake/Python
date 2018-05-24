import random

n=random.randint(1,20)
g=0

while(g!=n):
    g=input('Guess my number ')
    g=int(g)
    if(g>n):
        print('Too big')
    if(g<n):
        print('Too small')
print('Correct!')
a=[1,4,9,26,25,36,49,64,81,100]

op=[a[i] for i in range(len(a)) if a[i]%2==0 ]
print (op)

import random

numlist = []
list_length = random.randint(5, 15)

print (list_length)

while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))



evenlist = [number for number in numlist if number % 2 == 0]

print(numlist)
print(evenlist)

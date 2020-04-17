#to print F in a special format
numbers = [5,2,5,2,2]
'''
for i in numbers:
    print('x' * i)
'''

#using nested loop
for i in numbers:
    for j in range(i):
        print('x', end = '')
    print('')


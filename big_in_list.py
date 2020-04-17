numbers = [4, 7, 23, 54, 2, 56]

big = numbers[0]

for number in numbers:
    if big < number:
        big = number
print('largest: ', big)

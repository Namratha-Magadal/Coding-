#16th November 2026
#Learing Nested if statements (Notes)

number = input('enter a number:')
number = float(number)
if number >0:
    if number % 2 == 0:
        print(number , 'is a positive even number')
    else:
        print(number , 'is a positive odd number')
elif number < 0:
    if number % 2 == 0:
        print(number , 'is a negative even number')
    else:
        print(number , 'is a negative odd number')
else:
    if number == 0:
        print(number , 'is an even number')
print('program finished')
        
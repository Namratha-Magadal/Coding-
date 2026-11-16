#09th November 2026
#Nested statements

c = 50
if c < 25:
    if c % 2 == 0:
        print('c is an even number less than 25')
    else:
        print('c is an odd number less than 25')
else:
    print('c is greater than 25')
    
a = input('enter weather, day or date:')
if a == 'weather':
    x = input('enter sunny or rainy:')
    if x == 'sunny':
        print('happy days!')
    else:
        print('sad days')
elif a == 'day':
    m = input('enter the day of the week:')
    if m == 'saturday' or m == 'sunday':
        print('happy days!')
    else:
        print('sad days')
else:
    if a == 'date':
        n = input('enter the date:')
    elif n%2 == 0:
        print('happy days!')
    else:
        print('sad days')
    

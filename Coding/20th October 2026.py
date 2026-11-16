#20th October 2026

#Question 1
number = input('enter a number:')
number = int(number)
if number>0:
    print(number, 'is a positive number')
elif number <0:
    print(number, 'is a negetive number')
else:
    print(number,'is zero')
print('program finished')

#Question 2
grade = input('enter your test grades:')
grade = int(grade)
if grade>=90:
    print('you got A in your test')
elif grade>=80:
    print('you got B in your test')
elif grade>=70:
    print('you got C in your test')
elif grade>=60:
    print('you got D in your test')
else:
    print('you failed you test')
print('program finished')

#Question 3
season = input('enter a season of the year:')
if season == 'spring':
    print('March, April, May')
elif season == 'summer':
    print('June, July, August')
elif season == 'august':
    print('September, October, November')
elif season == 'Winter':
    print('December, January, February')
else:
    print('you have not entered a valid season')
print('program finished')

#Question 4
number = input('enter a number between 1 and 7:')
number = int(number)
if number == 1:
    print('monday')
elif number == 2:
    print('tuesday')
elif number == 3:
    print('wednesday')
elif number == 4:
    print('thursday')
elif number == 5:
    print('friday')
elif number == 6:
    print('saturday')
elif number == 7:
    print('sunday')
else:
    ('error message')
print('program finished')

#Question 5
length = input('enter the length of the rectangle:')
length = int(length)
width = input('enter the width of the rectangle:')
width = int(width)
area = length * width
perimeter = 2*length + 2*width
if area>perimeter:
    print('the area is greater than the perimeter')
elif perimeter>area:
    print('the perimeter is greater the the area')
else:
    print('the area is the same as the perimeter')
print('program finished')

#Question 6
late = input('the number of days the book went past the due date:')
late = int(late)
if late <=5:
    print('you have to pay 50 cent')
elif late<=6:
    print('you have to pay 1 euro')
elif late<=10:
    print('you have to pay 5 euro')
else:
    print('membership cancelled')
print('progam finished')


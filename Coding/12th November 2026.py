#12th November 2026
#Revising for November assessments

name = input('enter your name:')
age = input('enter you age:')
age = float(age)
print('hello!' , name , 'you are' , age , 'years old')
age_next = age + 1
print('next your age will be' , age_next)

number = input('enter a number:')
number = float(number)
num = (number + 5) * 2
print('the calculated result is' , num)

letter = input('enter a, b or c:')
if letter == 'a':
    print('the first letter of the alphabet')
elif letter == 'b':
    print('the second letter of the alphabet')
elif letter == 'c':
    print('the third letter of the alphabet')
else:
    print('invalid input')
    
numb = input('enter any one of the first 5 whole numbers expect 0:')
numb = float(numb)
if numb == 1:
    print('one')
elif numb == 2:
    print('two')
elif numb == 3:
    print('three')
elif numb == 4:
    print('four')
elif numb == 5:
    print('five')
else:
    print('invalid input')

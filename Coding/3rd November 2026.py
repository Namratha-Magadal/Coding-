#03rd November 2026

name = input('enter your name:')
print('hello' , name)

number_1 = input('enter a number:')
number_1 = float(number_1)
number_2 = input ('enter a number:')
number_2 = float(number_2)
total = number_1 + number_2
print('the sum of' , number_1 , 'and' , number_2 , 'is' , total)

ticket = 6
movie = input('enter the number of tickets needed:')
movie = float(movie)
money = movie * ticket
print('you have to pay' , money , 'for' , movie , 'tickets')

marks = input('enter marks obtained:')
marks = float(marks)
total_marks = input('enter the total markes of the test:')
total_marks = float(total_marks)
total = marks / total_marks * 100
print('you got' , total , 'percent')

gender = input('enter your gender:')
if gender == 'male':
    print('good morning sir')
elif gender == 'female':
    print('good morning madam')
else:
    print('not a valid gender')
    
number = input('guess a number from 1 to 10:')
number = float(number)
if number == 1:
    print('close enough to the correct number')
elif number == 2:
    print ('bingo! correct answer')
elif number == 3:
    print ('close enough to the correct number')
elif number == 4:
    print('not close enough')
elif number == 5:
    print('not close enough')
elif number == 6:
    print('not close enough')
elif number == 7:
    print('not close enough')
elif number == 8:
    print('not close enough')
elif number == 9:
    ('not close enough')
else:
    print('not close enough')
    
number = input('enter a number:')
number = float(number)
if number%3 == 0:
    print('the number you have entered is divisible by 3')
else:
    print('the number you have entered is not divisible by 3')
    
number_1 = input('enter a number:')
number_1 = float(number_1)
number_2 = input('enter a number:')
number_2 = float(number_2)
number_3 = input('enter a number:')
number_3 = float(number_3)
if number_1 + number_2 == number_3:
    print(number_1 , '+' , number_2 , '=' , number_3 )
elif number_2 + number_3 == number_1:
    print(number_2 , '+' , number_3 , '=' , number_1)
elif number_3 + number_1 == number_2:
    print(number_3 , '+' , number_1 , '=' , number_2)
else:
    print('the sum of two numbers is not equal to the third number')
    
season = input('in what season are you buying the flowers?:')
chrysanthemums = input('enter how many chrysanthemums you need:')
chrysanthemums = float(chrysanthemums)
roses = input('enter how many roses you need:')
roses = float(roses)
tulips = input('enter how many tulips you need:')
tulips = float(tulips)
if season =='spring'or season =='summer':
    total = chrysanthemums * 2 + roses * 2 + tulips * 2
elif season == 'winter' or season =='autumn':
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulip = 4.15
else:
    print('unknown season entered')
total_chrysanthemums_cost = chrysanthemums * price_chrysanthemums
total_roses_cost = roses * price_roses
total_tulips_cost = tulips * price_tulip
final_cost = total_chrysanthemums_cost + total_roses_cost + total_tulips_cost + 2
print('total cost:' , final_cost)



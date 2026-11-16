#09th November 2026

#Question 1
name = input('enter your name:')
print('hello' , name , 'how are you?')

#Question 2
celsius = input('enter the temperature in celsius (C):')
celsius = float(celsius)
fahrenheit = (celsius * 1.8) + 32
print(celsius , 'degrees celsius is equal to' , fahrenheit , 'degrees fahrenheit')

#Question 3
car = input('enter the car brand you need:')
if car == 'ford':
    print('we stock lots of Fords')
elif car == 'hyundai':
    print('we stock lots of hyundai')
elif car == 'BMW':
    print('we stock lots of BMW')
else:
    print('we do not stock any of that brand of car')
    
#Question 4
age = input('enter your age:')
age = float(age)
if age == 1:
    print('you are 1')
elif age == 11:
    print('you are 11')
elif age == 21:
    print('you are 21')
elif age == 31:
    print('you are 31')
else:
    print('you are not 1, 11, 21 or 31')
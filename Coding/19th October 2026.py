#19th October 2029

#Question 1
number_1 = input('enter a number:')
number_1 = int(number_1)
if number_1 <0:
    print('it is a negetive number')
else:
    print('it is a positive number')
print('program finished')

#Question 2
password = input('enter the password:')
if password == 'admin':
    print('access granted')
else:
    print('password invalid')
print('program finished')

#Question 3
height = input('enter your height:')
height = float(height)
if height >= 1.2:
    print('you can go on the ride')
else:
    print('you are too short, you can not go on the ride')
print('program finished')
      
#Question 4
age_of_user = input('enter your age:')
age_of_user = int(age_of_user)
if age_of_user >=18:
    print('you can vote')
else:
        print('sorry, you can not vote')      
print('program finished')

#Question 5
number_2 = input('enter a number:')
number_2 = int(number_2)
if number_2%5==0:
    print('it is multiple of 5')
else:
    print('it is not a multiple of 5')
print('program finished')

#Question 6
number_3 = input('enter a number:')
number_3 = int(number_3)
if number_3%7==0:
    print('it is multiple of 7')
else:
    print('it is not a multiple of 7')
print('program finished')

#Question 7
user_age = input('enter your age:')
user_age = int(user_age)
if user_age >=65:
    print('you are a senoir citizen')
else:
    print('you are not a senior citizen')
print('program finished')

#Question 8
favourite_fruit = input('enter your favourite fruit:')
if favourite_fruit == 'apple':
    print('you have a great choice')
else:
    print('your choice is not bad, but not the best')
print('program finished')

#Question 9
number_1 = input('enter you first number:')
number_1 = int(number_1)
number_2 = input('enter your second number:')
number_2 = int(number_2)
if number_1 < number_2:
    print('accending order:')
    print(number_1, number_2)
else:
    print('accending order:')
    print(number_2, number_1)
print('program finished')


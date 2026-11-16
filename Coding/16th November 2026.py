#16th November 2026

#Question 1
name = input('enter your name:')
if name == 'admin':
    password = input('enter your password:')
    if password == '1234':
            print('Welcome, you have Administrator access')
    else:
        print('Incorrect password for Admin, you will have standard user access')
else:
    print('unknown user')
    
#Question 2
age = input('enter youe age:')
age = float(age)
if age >= 12:
    height = input('enter you height:')
    height = float(height)
    if height >= 140:
        print('you can go on the ride!')
    else:
        print('you are too small')
else:
    print('you are too young')
    
#Question 3
pool = input('is the pool open?:')
if pool == 'yes':
    wb = input('do you have a wristband?:')
    if wb == 'yes':
        print('enjoy swiming')
    else:
        print('you need to go to the counter and get a wristband')
else:
    print('you can not swim as the pool is close')
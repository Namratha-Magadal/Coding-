#15th September 2026

#program 3
user = input('enter a number:')
user = int(user)
user_second = input('enter a second number:')
user_second = int(user_second)
total_user = (user*user_second)
print(total_user)

#program 4
base = input('enter the length of the base of a triangle:')
base = float(base)
height = input('enter the height of a triangle:')
height = float(height)
area = 0.5*base*height
print(area)

#program 5
kirby = input('enter the name of the football team:')
wins = input('enter the number of wins:')
wins = float(wins)
draws = input('enter the number of draws:')
draws = float(draws)
losses = input('enter the number of losses:')
losses = float(losses)
win_points = wins*3
draw_points = draws*1
loss_points = losses*0
total_points = win_points + draw_points + loss_points
print('The total points for kirby so far:',total_points)

#program 6
chicken = input('enter the number of chickens they have:')
chicken = int(chicken)
cows = input('enter the number of cows they have:')
cows = int(cows)
pigs = input('enter the number of pigs they have:')
pigs = int(pigs)
chicken_legs = chicken*2
cow_legs = cows*4
pig_legs = pigs*4
total_legs = chicken_legs + cow_legs + pig_legs
print('the total number of legs in their far:',total_legs)
           
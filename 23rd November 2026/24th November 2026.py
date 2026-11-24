#24th November 2026

#Question 1
name = input('enter your name:')
length_name = len(name)
print('there are' , length_name , 'letters in your name')

#Question 2
name = input('enter your name:')
surname = input('enter your surname:')
name_1 = name +' '+ surname
print(name_1)
name_2 = len(name_1)
print('there are' , name_2 , 'letters when you combaine your name and surname')

#Question 3
name = input('enter your name:')
surname = input('enter your surname:')
name_1 = name.title()
surname_1 = surname.title()
full_name = (name_1 +' '+ surname_1)
print(full_name)

#Question 4
line = input('enter the first line of a nursery rhyme:')
line_1 = len(line)
print('ther are' , line_1 , 'letters in' , line)

#Question 5
word = input('enter a word:')
word_1 = len(word)
print(word_1)

#Question 6
name = input('enter your name:')
surname = input('enter your surname:')
fn = name+' ' +surname
name_1 = len(name)
if name_1 <5:
    v = fn.upper()
    print(v)
else:
    m = fn.lower()
    print(m)

#Question 7

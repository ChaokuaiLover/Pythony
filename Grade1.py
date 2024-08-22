point = 0
point = int(input('Your grade : '))
if 80 <= point <=100 :
    print('Your grade is 4.0')
elif 75 <= point < 80 :
    print('Your grade is 3.5')
elif 70<= point < 75 :
    print('Your grade is 3.0')
elif 65 <= point < 70 :
    print('Your grade is 2.5')
elif 60 <= point < 65 :
    print('Your grade is 2.0')
elif 55 <= point < 60 :
    print('Your grade is 1.5')
elif 50 <= point < 55 :
    print('Your grade is 1.0')
elif 0 <= point < 50 :
    print('Your grade is 0')
else:
    print('ERROR')
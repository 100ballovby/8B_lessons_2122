age = int(input('Сколько тебе лет? '))

if age <= 4:
    print('Бесплатно!')
elif age < 18:
    print('$5 гони')
else:
    print('$10 гони')

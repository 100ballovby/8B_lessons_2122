# .upper(), .lower()
phrase = 'привет, Андрей!'
phrase2 = 'Привет, Андрей!'
print(phrase == phrase2)
print(phrase.lower() == phrase2.lower())
print('привет'.upper())

# .isupper(), .islower(), .isdigit()
print('f'.islower())  # True
print('F'.isupper())  # True
print('4.56'.isdigit())  # False

# .replace(x, y)
phrase3 = 'Привет! Я разработчик!'
print(phrase3.replace('а', '@'))
print(phrase3.replace('разработчик', 'пианист'))
print(phrase3.replace('?', 'пианист'))

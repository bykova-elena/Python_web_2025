lst = []

while (word := input('Введите слово: ').strip()) != '':
    lst.append(word[0].upper())

print('Получилась аббревиатура', end=': ')
print(*lst, sep='')
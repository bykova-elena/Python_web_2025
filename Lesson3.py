num = 3 #число, котрое надо угадать
flag = True # флаг, изменяет значение по событию
var = ''

print (' загадал число, угадай!')

while flag:
    var = int(input('Ваше значение:'))
    if var == num:
        print('Ура, угадал!')
        flag = not flag

print ('Приходи ещё!')
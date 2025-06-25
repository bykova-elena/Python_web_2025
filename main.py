# name = input('Как тебя зовут?')  # str
#
#
# print('Привет' , name)
# print('Приятно познакомиться')


# donut = int(input('Стоимость пончика:'))
# coffee = int(input('Стоимость кофе:'))
#
# print('С Вас', donut + coffee, 'руб.')


# number = int(input('Введите число'))
# print('Число', number , 'заканчивается на', number % 10)

# number = int(input('Введите число'))
# print('Число', number , 'в третей степени' , ** 3)
# print('Квадратный корень от вашего числа', number ** (1/2))



# print('mIU2')
# name = 'Bob'  # str
# surname = 'Bibsey'
# age = 84  # int
# print('Привет,', name, surname, ', тебе', age , 'лет.')
# print('Привет,', name, surname, ', тебе', age , 'лет.')
# print('Температура на улице,', temper,  'лет.')
#
# temper = 13.4  # float (floating point)
# print('mIU4')

# print('Дарова Биск')
#
# prompt = """Витязь на распутье
# 'Налево (L) пойдешь, вольну-волю обретешь...
# 'Направо (R) пойдешь, коня потеряешь...
# 'Прямо (F) пойдешь, сыт и весел будешь..."""
# print(prompt)
# choice = input('Куда идем (L, R или F): ')
# if choice == 'L' or choice == 'l':
#     print('Волная воля ')
# elif choice == 'R' or choice == 'r':
#     print('Конь сбежал')
# elif choice == 'F' or choice == 'f':
#     print('Квемпи и перке')
# else:
#     print('Выбор не ясен')


# a = 5
# if a ==5:
#     print('а равно 5')
#     print('Условие выполнилось')
# elif a==3:
#     print('а равно 3')
#     print('Условие выполнилось')



hour = 22

# 0 - 23
# Если время между 7 утра и 11 утра, то доброе утро
# Если время между 12 дня и 17 дня, то добрый день
# Если время между 18 вечера и 22 вечера, то добрый вечер
# В остальных случаях - доброй ночи

# проверка корректности
if hour > 23:
    hour = 23
if hour < 0:
    hour = 0

if hour >= 7 and hour < 12:
    print('доброе утро')
elif hour >= 12 and hour < 18:
    print('добрый день')
elif hour >= 18 and hour < 22:
    print('добрый вечер')
else:
    print('доброй ночи')
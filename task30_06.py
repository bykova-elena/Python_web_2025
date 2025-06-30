# Списки (list)
from operator import itemgetter

# lst = [1, 7, 3, 5, 6, 4, 2]
# lst.sort()
# lst.pop(5)
#
# print(lst)

# okroshka = []
# while (item := input('Введите ингредиенты: ')) != '':
#     lst.append(item)
#
#
#
# print(f'У нас есть {len(lst)} ингредиентов: ')
# lst.sort()
#
# for i in range(len(lst)):
#     print(f'\t{i+1}. {lst[lst[i]]}')

N = 5

lst = [] # пустой список

for i in range (N):
    print(f'Кладем книгу {i + 1} в стропку.')
    lst.append(i+1)

while lst:
    item = lst.pop()
    print(f'Берем книгу {item} из стопки.')
# Строки (immutable,iterable)
# Начало и окончание строки
# startswith и endswith
from itertools import count
from operator import index

s = 'синхрофазотрон'
ch = 'о'

if ch in s:
    count = s.count(ch)
    print(f'Буква {ch} встречается в слове {s} {count} раз.')
    print('Её позиция/позиции:')
else:
    print(f'буквы {ch} нет в слове {s}')


# предзаполненный словарь

d = {
    'table': ['таблица', 'стол'],
    'well': ['хорошо', 'колодец', 'скважина'],
    'chair': 'хорошо',
    'apple': 'яблоко',
    1: 'один',
}

print(d['well'][0])
if type (d['well']) == list:
    (d['well'].append('скважина'))
d['plum']='слива'
print(d['plum'])
del d['well']

for key in d:
    print(key, '->', d[key])


print(d)


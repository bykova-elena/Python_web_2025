  # ООП  (encapsulation)
  # Свойства классов

a = 3
print(a.__class__.__name__)

class Fruit:
    pass


a = Fruit()
b = Fruit()
с = Fruit()

a.name = 'Яблоко'
a.weight = 120
print(a.name)
print(a.weight)

b.name = 'Банан'
b.weight = 170
print(b.name)
print(b.weight)

print(a.__class__)
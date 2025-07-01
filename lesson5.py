# Списочные выражения (list comprehension)


# squares.append(i**2)

# список квадратов чисел
# squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(*squares, sep=',')
squares = []

# произведение i и j
print([i * j for i in range(3) for j in range(3)])
for i in range(10):
    squares.append(i **2)

print(*squares, sep=', ')


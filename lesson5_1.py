# Вложенные списки
from lesson_30_06 import count

matrix = [[1] * N for _ in range (N)
print(matrix)
# обход 2-мерного списка (матрицы)
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        matrix[row] [col] = count
        count += 1

print(matrix)

# matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#]

matrix = [[1] * 3 for _ in range (3)]
print(matrix)

# обход 2-мерного списка (матрицы)
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col])
print(matrix)























# Списочные выражения (list comprehension)

# text = 'Списочные выражения применяются для эффективности кода'

# res = [a for a in text.split() if (text.index(a)+1) % 3 == 0]
# res = [a for a in text.split()[2::3]]

# print(res)







# произведение i и j

# print([i * j for i in range(3) for j in range (3)])

# n = '100 200 300 400 500 600 700 800 900'
# approved = ['500', '800']
# a = [int(i) for i in n.split() if i in approved]
# какие-то действия со списком a
# print(a)
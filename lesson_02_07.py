




















# # Функция, с переменным числом аргументов
# from ctypes import HRESULT
#
#
# def multy(first *args):
#     # print(len(args))
#     # print(args)
#     # if len(args) == 0
#     #     return 0
#     if not args:
#         return first
#     result = first
#     for arg in args:
#         result *= arg
#     return result
#
# def fio(name, surname):
#     return f'{name} {surname}'
#
# print(fio(surname='Бендер', name='Остап'))
# print(multy('args: 1, 2, 3, 4,))
















# # Возврат нескольких значений из функции
# # При расстановке '+' может быть только одна
#
# def coordinates() -> tuple:
#     return 5.4, 3.2, 3.8, 7.2, 4.6
#
# x, y, *rest = coordinates()
# print(f'x = {x}, y = {y}, rest = {rest},')
#
# *names, surname = 'Остап Сулейман Бендер'.split()
# print(names,surname)






# def print_array(array: list, start: int = None):
#     if start is not None and start > len(array):
#         return
#         if start is None:
#             start = 0
#             for i in range(start,len(array)):
#                 return
#         for i in array:
#             print()
#     else:
#         for i in range
# a = [1,2,3]
# print_array(a, 1)
#
#









# # Оператор is: a is b -> когда a и b - один и тот же объект
#
# my_refregirator = ['колбаса', 'сыр', 'масло']
# # his_refregirator = ['колбаса', 'сыр', 'масло']
# his_refregirator = my_refregirator.copy()
# # my_refregirator += ['мясо']
# print(his_refregirator)
# print(my_refregirator is his_refregirator)
# print(my_refregirator == his_refregirator)
# print(id(my_refregirator)) == (id(his_refregirator))
# temp = None
#
# print(type(temp))
# print(temp is None)
# if temp is None:































# return vs yield

# def print_goodbye(arg):
#     print('Goodbye', end=' ')
#
# def print_cruel(arg):
#     print('cruel', end=' ')
#
# def print_world(arg):
#     print('world', end=' ')
#
# def main():
#     print_goodbye(1)
#     print_cruel(1)
#     print_world(1)
#
# main()

# def generate_list():
#     for i in range(5):
#         yield i
#
# array = tuple(generate_list())

























# # Области видимости
# # PI = 3.1415
# # Shadows name 'square' from outer scope
# square = 'Дворцовая площадь'
#
#
# def greet(name):
#     print('Привет,', name)
#     name = 'друг'
#     print('Здравствуй', name)
#
# def square_area(lenght: int, width: int) -> None:
#     area = lenght * width
#     print(f'Площадь площади "{square}" = {area}')
#
#
# def circle_lenght(radius: float):
#     perimetr = 2 * PI * radius
#     print(f'Длина окружности с радиусом {radius} = {perimetr:.2f}')
#
#
# def print_array(array: list) -> None:
#     for item in array:
#         print(item)
#
#
#
# words = ['Привет', 'мир']
# PI = 3.14
# greet('Пётр')
# print('Давай встретимся, где', square)
# square_area(320, 240)
# print('Ну что? Встречаемся, где', square)
# circle_lenght(5)
# print_array(words)
# print_array(['a','b','c'])

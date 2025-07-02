# Области видимости
# PI = 3.1415
# Shadows name 'square' from outer scope
square = 'Дворцовая площадь'


def greet(name):
    print('Привет,', name)
    name = 'друг'
    print('Здравствуй', name)

def square_area(lenght: int, width: int) -> None:
    area = lenght * width
    print(f'Площадь площади "{square}" = {area}')


def circle_lenght(radius: float):
    perimetr = 2 * PI * radius
    print(f'Длина окружности с радиусом {radius} = {perimetr:.2f}')


def print_array(array: list) -> None:
    for item in array:
        print(item)



words = ['Привет', 'мир']
PI = 3.14
greet('Пётр')
print('Давай встретимся, где', square)
square_area(320, 240)
print('Ну что? Встречаемся, где', square)
circle_lenght(5)
print_array(words)
print_array(['a','b','c'])

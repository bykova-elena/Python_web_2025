# алфавит
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# сдвиг
shift = 3

# пользователь выбирает действие
choice = input('Здравствуйте, если вы хотите расшифровать текст - нажмите 1, а если зашифровать - 2: ')

# если выбрали расшифровку
if choice == '1':
    word = input('Введите слово для расшифровки: ')
    new_word = ""        # создаём пустую строку для результата
    error = False        # флажок ошибки, сначала False (всё хорошо)

    for letter in word:
        letter_index = alphabet.find(letter)

        if letter_index == -1:  # если буква не найдена в русском алфавите
            print('Вы ввели неверный формат данных')
            error = True        # флаг ошибки переключается на True
            break               # прерываем цикл
        else:
            new_letter = alphabet[letter_index - shift]  # сдвигаем букву назад
            new_word += new_letter

    if not error:  # если всё хорошо — выводим результат
        print(f'Ваше расшифрованное слово: "{new_word}"')

# если выбрали зашифровать
elif choice == '2':
    word = input('Введите слово для шифровки: ')
    new_word = ""        # обнуляем строку для результата
    error = False        # флажок ошибки

    for letter in word:
        letter_index = alphabet.find(letter)

        if letter_index == -1:  # если буква не из алфавита
            print('Вы ввели неверный формат данных')
            error = True
            break
        else:
            new_letter = alphabet[letter_index + shift]  # сдвигаем букву вперёд
            new_word += new_letter

    if not error:
        print(f'Ваше зашифрованное слово: "{new_word}"')

# если пользователь ввёл что-то не то
else:
    print('Вы ввели некорректное значение')



# Задание 5:
# Создайте функцию world() которая возвращает вам "Hello World"
# Создайте функцию kyrgyzstan() которая возвращает вам "Hello Kyrgyzstan"
# Создайте функцию bishkek() которая возвращает вам "Hello Bishkek"
# ОБЯЗАТЕЛЬНО НЕ ИСПОЛЬЗОВАТЬ IF!
# Спросите у пользователя какую из функций запустить и пусть пользователь c Терминала напишет код который запустит одну из трёх функций.
# Подсказка: Встроенные Функции.



def world():
    print('Hello World')


def kyrgyzstan():
    print('Hello Kyrgyzstan')


def bishkek():
    print('Hello Bishkek')


function_mapping = {
        'world': world,
        'kyrgyzstan': kyrgyzstan,
        'bishkek': bishkek
    }

f = input('Какую функцию запустить? Напечатайте одно из трех названий: 1)world, 2)kyrgyzstan, 3)bishkek: ')
result = eval(f+"()")
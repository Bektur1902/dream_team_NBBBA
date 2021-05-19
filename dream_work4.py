# Задание 4:
# Создайте функцию которая принимает SET.
# data_set = {('login', 'password', 'codeword'), 1988, 32, 'Python', 'Kyrgyzstan', ('October', 'November', 'December'), 'Senior', 'TeamLead'}
# Сделайте так чтобы из набора данных который пришёл вам в SET функция была способна вытаскивалть элементы по индексу в обратной последовательности.
# Выведите все элементы из набора данных в обратной последовательности. Обязательно сделать это РЕКУРСИВНО!


def somefunc(someset,i):
    someset = list(someset)
    print(someset[i])
    if i == 0:
        return
    somefunc(someset,i - 1)


data_set = {('login', 'password', 'codeword'), 1988, 32, 'Python', 'Kyrgyzstan', ('October', 'November', 'December'), 'Senior', 'TeamLead'}
print(data_set)
somefunc(data_set,len(data_set) - 1)
"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


def uniq_hash(str_in):
    len_str = len(str_in)
    res_set = set()
    for i in range(1, len_str):
        res_set = res_set.union([hash(str_in[k:k + i]) for k in range(len_str)])
    # выводим результат
    print(res_set)


# Протестируем три раза, чтобы проверить идентичность созданных хешей
uniq_hash(input('Введите текст:'))
uniq_hash(input('Введите текст:'))
uniq_hash(input('Введите текст:'))

# проверка по условию - papa ==> {'pa', 'pap', 'ap', 'p', 'a', 'apa'}

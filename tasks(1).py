from functools import reduce

'''
Задача 1.
На основе строки, представляющей из себя предложение, построить вложенный список,
содержащий символы всех слов в предложении. Пример: строка 'Eeny, meeny, miney, moe;
Catch a tiger by his toe.' будет преобразована в: [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n',
'e', 'y'], ['m', 'o', 'e'], ['C', 'a', 't', 'c', 'h'], ['a'], ['t', 'i', 'g', 'e', 'r'], ['b', 'y'], ['h', 'i', 's'], ['t', 'o', 'e']]
'''


def task1(string):
    string = string.replace(';', ' ').replace(',', ' ').replace('.', ' ').replace('  ', ' ')
    string = string.split(' ')
    string = filter(lambda el: True if el != '' else False, string)
    string = map(list, string)
    print(list(string))


task1("Eeny, meeny, miney, moe. Catch a tiger's by his toe.")

'''
Задача 3.
В строке, содержащей последовательность слов, разделенных запятыми, удалить все
нечетные слова. Ответ представить в виде строки. Пример: строка
'SIX,SEVEN,EIGHT,NINE,TEN' будет преобразована в: 'SIX,EIGHT,TEN'''

string = 'SIX, SEVEN, EIGHT, NINE, TEN'.split(',')
new_string = ','.join(string[0::2])
print(new_string)

'''
Задача 8.
Реализовать функцию st_reverse(a_string), которая при помощи стека инвертирует строку
(меняет порядок букв на обратный). Пример: st_reverse(‘abcd’) -> ‘dcba’.'''

string = 'abcd'


def str_reverse(s_string):
    stack = list()
    for i in s_string:
        stack.append(i)
    newstring = ''
    while len(stack) != 0:
        newstring += stack.pop()
    return newstring


print(str_reverse(string))

'''Задача 6.
Дан список целых чисел. При помощи механизма map/filter/reduce рассчитать остаток от
деления на 17 для каждого из чисел списка и получить произведение тех остатков,
величина которых больше 7.'''
i = [17, 9]
mod_17 = map(lambda el: el % 17, i)
new_i = filter(lambda el: True if el > 7 else False, mod_17)
finish = reduce(lambda accumulate, elem: accumulate * elem, new_i, 1)
print(finish)

'''Задача 7.
Дано предложение без знаков препинания. Превратить предложение в список слов. При
помощи механизма map/filter/reduce отбросить у каждого слова последнюю букву и
склеить в одну строку те обрезанные слова, длина которых больше 5'''

string = "Eeny meenyу miney moeууууу Catch a tigerss by his toe".split()
i = map(lambda el: el[0: len(el) - 1:1], string)
new_i = list(filter(lambda el: True if len(el) > 5 else False, i))
f = reduce(lambda x, y: x + y, new_i)
print(f)

'''Задача 5.
Используя генератор словарей (и не используя код вне него) инвертировать словарь, т.е.
сделать ключи словарая его значениями и наоборот. Значения, которые в исходном
словаре повторяются, не добавлять в итоговый словарь. Пример: {'a':1, 'b':3, 'c':4, 'd':3} ->
{1:'a', 4:'c'}
'''
import itertools

dic = {'a': 1, 'b': 3, 'c': 4, 'd': 3}

new_dic = {key: grouped_list[0]
           for key, grouped_list in
           [(k, list(grouped_iter))
            for k, grouped_iter in itertools.groupby(sorted(dic, key=lambda k: dic[k]), key=lambda k: dic[k])]
           if (len(grouped_list) == 1)
           }

print(new_dic)

'''Задача 9.
Используя генератор списков (и не используя код вне него) преобразовать два списка (в
первом содержатся целые числа, во втором строки, содержащие один символ) в словарь, в
котором соответствующие друг другу пары значений из исходных списков преобразованы
в целочисленный ключ и строку состоящую из повторенных символов (количество
повтарений равно значению ключа). Пример [2, 4, 1, 3], ['a', 'b', 'c', 'd'] -> {2:'aa', 4:'bbbb',
1:'c', 3:'ddd'}
'''

one, two = [2, 4, 1, 3], ['a', 'b', 'c', 'd']
rez = {k: v * k for k, v in zip(one, two)}
print(rez)


'''Задача 14.
Реализовать декораторы:
1) с именем not_none, который генерирует исключительную ситуацию,
если декорируемая функция вернула значения None.
2) c именем print_type, который печтает тип возвращаемого значения декорируемой функции. '''

def not_none(funk):
    def wrapper():
        f = funk()
        if f is None:
            raise Exception('Генерируется исключительная ситуация!')
        else:
            print('Тест, исключение не вызвано.')

    return wrapper


def print_type(funk):
    def wrapper():
        f = funk()

        print(f'Тип возвращаемого значения: {type(f)}')

    return wrapper


@print_type
def f():
    return 1


f()

'''Задача 13.
Реализовать функцию repl , которая принимает на вход строку и набор заранее
неизвестных параметров. Результатом функции является строка, в которой слова
совпадающие с именами параметров заменены на значения параметров. Пример: строка:
'replace my val abc', параметры my='s1', abc='fff' -> Результат: 'replace s1 val fff'
'''

st = 'replace my val abc'


def repl(string, **args):
    for k, v in args.items():
        if k in string:
            string.replace(k, v)
    return string


a = repl(st, my='s1', abc='fff')

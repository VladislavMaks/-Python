# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_name = input('Введите необходимый файл: ')
file = open(file_name, 'w')
line = input('Cтрока: ')
file.write(line)
file.close()

# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open("my_file.txt") as my_file:
    i = 0
    for line in my_file.readlines():
        print(line)
        i += 1
        l_split = line.split()
        print(f'Количество слов: {len(l_split)}')
    print(f'Количество строк: {i}')

# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from functools import reduce


def poor(name, rate):
    """
    Функция определяет кто из работников получает меньше 20 000
    """
    if rate < 20000:
        print(f'{name} получает меньше 20000')


def mid_salary(arg_1, arg_2):
    """
    Функция считает всю зарплату сотрудников
    """
    return arg_2 + arg_1


with open("emp1.txt") as emp_file:
    money_list = []
    numb = 0
    for line in emp_file.readlines():
        numb += 1
        s_line = line.split()
        name = s_line[0]
        rate = float(s_line[1])
        poor(name, rate)
        money_list.append(rate)
    print('Средняя зарплата всех сотрудников:', reduce(mid_salary, money_list) / numb)

# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open("geek.txt", encoding='utf-8') as defolt_file:
    rus_trans = []
    for line in defolt_file.readlines():
        l_split = line.split()
        l_split[0] = translate[l_split[0]]
        rus_trans.append(' '.join(l_split))
    content = '\n'.join(rus_trans)

with open("geek1.txt", 'w', encoding='utf-8') as rus_geek:
    rus_geek.write(content)

# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce


def sum(arg_1, arg_2):
    arg_1, arg_2 = float(arg_1), float(arg_2)
    return arg_1 + arg_2


with open("some_numbers.txt", 'w') as numbers_write:
    content = input('Введите набор чисел, разделенных пробелами: ')
    numbers_write.write(content)

with open("some_numbers.txt") as numbers_read:
    numbers = numbers_read.readline()
    num_list = numbers.split()
    print('Сумма чисел в файле:', reduce(sum, num_list))

# 6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce


def isdig(string):
    """
    Функция ищет числа в строке и возвращает список чисел в ней, преобразуя числа в класс int
    """
    str_list = string.split()
    num_list = []
    for item in str_list:
        a = list(item)
        num = ''
        for i in a:
            if i.isdigit():
                num += i
        if num != '':
            num_list.append(int(num))
    return num_list


def sum(arg_1, arg_2):
    return arg_1 + arg_2


sub_dict = {}
with open("subj.txt", encoding='utf-8') as subjects:
    for line in subjects.readlines():
        items_line = line.split()
        sub_dict[items_line[0]] = reduce(sum, isdig(line))
print(sub_dict)

# 7) Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json


def income(profit, expense):
    profit, expense = float(profit), float(expense)
    return profit - expense


def middle_inc(inco):
    sum = 0
    i = 0
    for item in inco:
        if item > 0:
            i += 1
            sum += item
    return sum / i


with open("Firms.txt", encoding='UTF-8') as firms_file:
    inc_list = []
    big_list = []
    inc_dict = {}
    middle_dict = {}
    for line in firms_file.readlines():
        l_split = line.split()
        profit = l_split[2]
        expense = l_split[3]
        inc_list.append(income(profit, expense))
        inc_dict[l_split[0]] = income(profit, expense)
        middle_dict['average_profit'] = middle_inc(inc_list)
    big_list.append(inc_dict)
    big_list.append(middle_dict)

with open("big_list.json", 'w', encoding='UTF-8') as big_jason:
    json.dump(big_list, big_jason)

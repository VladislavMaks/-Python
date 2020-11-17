# 1)
# voc = {'Vlad': 'maksim@yandex.ug',
#       'Adel': 'ad@mail.ru',
#       'spammer': 'TrumpVote@gm.com'}
# my_list = [1, 'Ховер', 2.4, {1, 3, 7}, ['Vova', 'Sasha', 'Vika'], voc]
# for item in my_list:
#    print(type(item))

# 2
# change_list = input('Введите элементы списка: ').split()
# k = 0
# for i in range(int(len(change_list)/2)):
#     change_list[k], change_list[k+1] = change_list[k+1], change_list[k]
#     k +=2
# print(change_list)

# 3)
#month = int(input('Введите месяц: '))
# list
#month_list = ['брябрь', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
#              'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#if month_list[month] == 'февраль' or month_list[month] == 'декабрь' or month_list[month] == 'январь':
#    print(month_list[month], 'это зима')
#elif month_list[month] == 'февраль' or month_list[month] == 'март' or month_list[month] == 'май':
#    print(month_list[month], 'это осень')
#elif month_list[month] == 'июнь' or month_list[month] == 'июль' or month_list[month] == 'август':
#    print(month_list[month], 'это лето')
#elif month_list[month] == 'сентябрь' or month_list[month] == 'октябрь' or month_list[month] == 'ноябрь':
#    print(month_list[month], 'это осень')
#else:
#    print('Нет такого месяца')
    #dict
#month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
#              7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
#if month_dict[month] == 'февраль' or month_dict[month] == 'декабрь' or month_dict[month] == 'январь':
#    print(month_dict[month], 'это зима')
#elif month_dict[month] == 'февраль' or month_dict[month] == 'март' or month_dict[month] == 'май':
#    print(month_dict[month], 'это осень')
#elif month_dict[month] == 'июнь' or month_dict[month] == 'июль' or month_dict[month] == 'август':
#    print(month_dict[month], 'это лето')
#elif month_dict[month] == 'сентябрь' or month_dict[month] == 'октябрь' or month_dict[month] == 'ноябрь':
#    print(month_dict[month], 'это осень')
# else:
#     print('Нет такого месяца')

# 4)
# user_str = input('Введите строку, разделяя слова пробелами: ').split()
# t = 1
# for i in user_str:
#     print(t, i[:10])
#     t +=1

# 5)
# rate_list = [7, 5, 3, 3, 2]
# user_number = int(input('Введите число: '))
# rate_list.reverse()
# i = 0
# for a in rate_list:
#     if user_number < a:
#         break
#     i +=1
# rate_list.insert(i, user_number)
# rate_list.reverse()
# print(rate_list)




"""
    Ваша задача дописать функции, чтобы они проходили все тесты
    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.
    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    return number + (20 - number % 20)


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    lst = string.split()
    output = ''
    for word in lst:
        output += word[::-1] + ' '
    output = output.strip()
    return output


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    output = ''
    for key in dictionary:
        output += f'{key}: {dictionary[key]}; '
    return output[:-2]


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return sub_string[::-1] in string


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    dictionary = dict()
    for i in range(len(strings)):
        dictionary[i] = strings[i]
    keys = []
    for i, string in enumerate(strings):
        lst = string.split()
        if int(lst[0]) * int(lst[1]) * int(lst[2]) != int(lst[3]):
            keys.append(i)
    for i in keys:
        del dictionary[i]
    output = []
    for i in dictionary:
        output.append(dictionary[i])
    return output

def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки
    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    output = ''
    for elem in string:
        if elem != '#':
            output += elem
        else:
            output = output[:-1]
    return output

def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.
    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    output = 0
    for elem in lst:
        if lst.count(elem) == 1:
            output += int(elem)
    return output


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число
    gh12cdy695m1 -> 695
    """
    import re
    lst = re.findall('[0-9]+', string)
    max_value = int(lst[0])
    for value in lst:
        if int(value) > max_value:
            max_value = int(value)
    return max_value


def t9(number):
    """
    Приведите число number к пятизначному виду.
    Т.е. для числа 5 верните `00005`
    """
    number = str(number)
    if len(number) < 5:
        return '0'*(5-len(number)) + number
    else:
        return number


def t10(string):
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет
    Комбинации цветов:    G G     B G    R G   B R
    Результирующий цвет:   G       R      B     G
    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод
    """
    def mixer(string):
        colors = {'R', 'G', 'B'}
        new_string = ''
        for i in range(len(string)-1):
            to_mix = {string[i], string[i+1]}
            if len(to_mix) == 2:
                new_string += (colors - to_mix).pop()
            else:
                new_string += to_mix.pop()
        return new_string
    
    while len(string) > 1:
        string = mixer(string)
    
    return string


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    for i in range(1, len(lst)-1):
        sum1 = sum([int(x) for x in lst[:i]])
        sum2 = sum([int(x) for x in lst[i+1:]])
        if sum1 == sum2:
            return i
    return -1 

def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]
    """
    import re
    output = []
    for string in lst:
        groups = re.findall('\+?\d[( -]?(\d{3})[) -]?(\d{3})[ -]?(\d{2})[ -]?(\d{2})', string)[0]
        number = '8'
        for group in groups:
            number += group
        output.append(number)
    return output

def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    number_1 = str(number_1)
    number_2 = str(number_2)
    if len(number_1) < len(number_2):
            number_1 = '0'*(len(number_2) - len(number_1)) + number_1
    else:
            number_2 = '0'*(len(number_1) - len(number_2)) + number_2
    output = ''
    for i in range(len(number_1)):
        output += str(int(number_1[i]) + int(number_2[i]))
    return int(output)


def t14(string):
    """
    Преобразуйте математическое выражение (символьное) в буквенное выраэение
    Для операций используйте следующую таблицу
        { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    Примеры:
        4 ** 9 -> Four To The Power Of Nine
        10 - 5 -> Ten Minus Five
        2 = 2  -> Two Equals Two
    """
    numbers = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', 
               '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
    operations = { '+':   ' Plus ',
          '-':   ' Minus ',
          '*':   ' Times ',
          '/':   ' Divided By ',
          '**':  ' To The Power Of ',
          '=':   ' Equals ',
          '!=':  ' Does Not Equal ' }
    lst = string.split()
    return numbers[lst[0]] + operations[lst[1]] + numbers[lst[2]]


def t15(lst):
    """
    Найдите сумму элементов на диагоналях
    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    diag_sum = 0
    for i in range(len(lst)):
        diag_sum += lst[i][i] + lst[len(lst)-i-1][i]
    return diag_sum
        

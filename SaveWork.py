#region Интересное
from collections import Counter #Посчитать сколько и каких букв есть в строке !!!!
s = 'ffffggg' # Counter(s) ответ: Counter({'f': 4, 'g': 3})
s1 = {'f':1,'g':3,'h':2}
s2 = {'f':1,'g':3,'h':1}
print(Counter(s)) # ответ: Counter({'h': 1})
print(len(Counter(s1)-Counter(s2))) # ответ: 1, так как показывает все оставшиеся буквы, а не сумму всех оставшихся
# тут осталась одна (h) значит ответ 1, осталось бы две (h,f) написалобы 2, независимо осталось ли суммарно 5 или 10

s = 'hello world'; print(s.capitalize()) #Capitalize - делает первую букву большой

print([x**2 for x in range(11) if x%2==0]) #Называется списковое включение
# [ выражение for цель! in итерируемый— объект! if условие!
# for цель2 in итерируемый—объект2 if условие2 . . .
# for цель!! in итерируемый_объектЫ if условие N] - Так тоже можно
res = [x+y for x in [1,2,3] for y in [10,20,30]]

mas = [1,2,3,4,5] #Увеличение всех элементов на 10
print(list(map(lambda x:x+10,mas))) #Map - первый аргумент то что должно проходить, второй по чему она проходится

print(list(filter(lambda x:x>0,range(-5,6)))) #Fitler то же, что и map(первый аргумент это функция(def,lambda))
                                              #Но первый аргумент задаёт условия, а по второму оно проходится с этим условием

max_digit = lambda number: max(map(int, str(number))) #Максимальное число из заданного (из 53 max=5)

# * может распаковывать итерируемые объекты print(range(3)) - range(0,3); print(*range(3)) - 0 1 2; или f = dict(hello = 'privet') print(f.keys()) - нормально
# f = dict(hello = 'privet') print(f.keys()) - dict_keys(['hello'])
#endregion

#region Интересное - значения
s=1
s.isdigit() #Проверка, является ли это числом

s = '''hello 
world'''
s.splitlines() #Разделяет на строки

all() #Возращает True если все элементы истинны
# Пример из Site tasks: all(st[i]<st[i+1] for i in range(len(st)-1))
#endregion

#region Site tasks
def first_word(text: str) -> str: #Вывод первого слова
    text = text.split(' ')
    return text[0]

mx = lambda num: len(s := str(num)) - len(s.rstrip('0'))  #Сколько нулей в конце числа

def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0')) #Сколько нулей в начале числа

def replace_first(items: list) -> list: #Первый элемент сделать последним, если список только из 1 элемента, вывести его
    if items:
        items.append(items.pop(0))
    return items

def nearest_value(values: set, one: int) -> int: #Найти ближайшее в списке или вывести это число, если ближайшее одинаковые, вывести меньшее
    return min(values, key=lambda n: (abs(one - n), n))
print(nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10)

def between_markers(text: str, begin: str, end: str) -> str: #Слово между разделителями
    return text[text.index(begin)+1:text.index(end)]
assert between_markers('What is >apple<', '>', '<') == "apple"

def correct_sentence(text: str) -> str: #Первая буква заглавная и в конце точка, но если она есть, то не добавлять
    return text[0].upper()+text[1:]+('.' if text[-1] != '.' else '')

def best_stock(data): #Вывод ключа(key) по максимальному value из словаря
    return max(data, key=data.__getitem__)
assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"

def remove_all_before(items: list, border: int): #От найденного числа до конца
    return items[items.index(border):] if border in items else items

def replace_last(line: list) -> list: #Последний символ теперь первый
    return line[-1:]+line[:-1]

all_the_same = lambda e: e[1:] == e[:-1] #Находяться ли в списке одинаковые элементы

def checkio(data: list) -> list:
    return [x for i, x in enumerate(data) if data.count(x) > 1] #Возвращает одинаковые элементы массива(если нужно индексы заменить i на x перед for)

def checkio(array: list) -> int: # Сложить чётные ИНДЕКСЫ и умножить на последнее число
    return 0 if not array else sum(array[::2])*array[-1]

def left_join(phrases: tuple) -> str: #Замена right на left, даже если они в друом слове
    return (','.join(phrases)).replace('right','left')

def func(text:str): #Сколько строк в тексте
    return sum(bool(line.strip()) for line in text.splitlines())

def func(st): #Каждое следующее число больше предыдущего
    return all(st[i]<st[i+1] for i in range(len(st)-1))

sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit()) #В тексте найти все цифры, но только разделённые пробелом

def checkio(values: list) -> list: #Сортировка списка по abs(абсолютному значению)
    values.sort(key=abs)           #key - проходит по всем элементам с тем что после =
    return values

def goes_after(word: str, first: str, second: str) -> bool: #Буква стоит сразу за другой
    try:
        return word.index(second)-word.index(first)==1
    except:
        return False

def checkio(first, second): #Общие слова в тексте и вывести через заятую отсортирова
    first_set, second_set = set(first.split(',')),set(second.split(','))
    common = first_set.intersection(second_set)
    return ','.join(sorted(common))

def create_phone_number(n): #Записать номер как (123) 456-7895
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)

print(create_phone_number([1,2,3,4,5,6,7,8,9,2]))

def consecutive(arr, a, b): #Определить идут ли числа последовательно в списке []
    return abs(arr.index(a)-arr.index(b)) == 1

def validate_pin(pin): #Количество чисел 4 или 6 и оно число
  return len(pin) in (4,6) and pin.isdigit()
print(validate_pin('12334'))

def rearranging(number): #Нахождение всех вариантов числа
    from itertools import permutations
    mas = [int(x) for x in str(number)] #Делает из числа массив чисел
    f = list(permutations(mas,len(mas))) #Находит все вариации числа

    return [int(''.join(map(str,i))) for i in f] #Объеденяет числа из кортежей: 131, 113, 311 и т.д.
print(121)

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)] #Анаграмма(комбинации слов)
#Дано слово и список, в списке мы находим такое, что при определённой комбинации оно дает заданное слово(word)
#endregion

def dont_give_me_five(start, end): #Проверка, выводит сумму списка без чисел в которых есть 5(можно любое)
    return sum('5' not in str(i) for i in range(start, end+1))
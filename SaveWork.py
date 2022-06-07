mas = [1,2,3,4,5] #Увеличение всех элементов на 10
print(list(map(lambda x:x+10,mas))) #Map - первый аргумент функция(def,lambda), второй по чему она проходится

print(list(filter(lambda x:x>0,range(-5,6)))) #Fitler то же, что и map(первый аргумент это функция(def,lambda))
                                              #Но первый аргумент задаёт условия, а по второму оно проходится с этим условием

max_digit = lambda number: max(map(int, str(number))) #Максимальное число из заданного (из 53 max=5)

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
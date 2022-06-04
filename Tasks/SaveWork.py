
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
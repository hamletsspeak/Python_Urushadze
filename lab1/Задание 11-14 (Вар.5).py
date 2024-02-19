# №2
def average_ascii_weight(char):
    # Функция, которая возвращает средний вес ASCII-кода символа
    return sum(ord(c) for c in char) / len(char)

def sort_string_by_ascii_weight(input_string):
    # Сортируем символы строки по среднему весу ASCII-кода
    sorted_string = sorted(input_string, key=average_ascii_weight)
    return ''.join(sorted_string)
input_string = "abcABC123"
sorted_string = sort_string_by_ascii_weight(input_string)
print("Строка в порядке увеличения среднего веса ASCII-кода символа:", sorted_string)

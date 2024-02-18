# Задания 2-4.
# №5
# import random
# def shuffle_string(input_string):
#     Преобразуем строку в список символов
    # characters = list(input_string)
    # Перемешиваем список символов
    # random.shuffle(characters)
    # Объединяем перемешанные символы в строку
    # shuffled_string = ''.join(characters)
    # return shuffled_string
# input_string = "Привет, я пример"
# shuffled_string = shuffle_string(input_string)
# print("Исходная строка:", input_string)
# print("Перемешанная строка:", shuffled_string)

# №7
# def palindrom(input_string):
    # Преобразуем строку к нижнему регистру для удобства сравнения
    # input_string = input_string.lower()
    # Удаляем все символы, не являющиеся буквами
    # input_string = ''.join(char for char in input_string if char.isalpha())
    # Проверяем, является ли строка палиндромом
    # return input_string == input_string[::-1]
# input_string = "A man, a plan, a canal, Panama"
# if palindrom(input_string):
#     print("Строка образует палиндром.")
# else:
#     print("Строка не образует палиндром.")

# 14
# def sort_words(input_string):
    # Разбиваем строку на слова
    # words = input_string.split()
    # Сортируем слова по их длине с использованием ключа сортировки
    # sorted_words = sorted(words, key=len)
    # Объединяем отсортированные слова обратно в строку
    # sorted_string = ' '.join(sorted_words)
    # return sorted_string
# input_string = "Привет это новая программа"
# sorted_string = sort_words(input_string)
# print("Отсортированная строка:", sorted_string)

# Задания 6-8
# №5
# import re
# def max_cyr(input_string):
    # Используем регулярное выражение для поиска всех последовательностей кириллических символов
    # sequences = re.findall(r'[а-я]+', input_string, flags=re.IGNORECASE)
    # Находим длину самой длинной последовательности
    # max_length = max(len(seq) for seq in sequences)
    # return max_length
# input_string = "Привет я обожаю орфографию"
# max_sequence_length = max_cyr(input_string)
# print("Наибольшее количество идущих подряд символов кириллицы:", max_sequence_length)

# №7
# import re

# def find_min_number(input_string):
    # Используем регулярное выражение для поиска всех натуральных чисел в строке
    # numbers = re.findall(r'\b\d+\b', input_string)
    # Преобразуем найденные числа в список целых чисел
    # numbers = [int(num) for num in numbers]
    # Находим минимальное число
    # min_number = min(numbers)
    # return min_number

# input_string = "10, 5, 25, и 3. Найдем минимальное."
# min_number = find_min_number(input_string)
# print("Минимальное число в строке:", min_number)

# №14
# import re

# def find_max_digit_sequence(input_string):
    # Используем регулярное выражение для поиска всех последовательностей цифр в строке
    # digit_sequences = re.findall(r'\d+', input_string)
    # Находим последовательность с максимальной длиной
    # max_sequence = max(digit_sequences, key=len, default="")
    # return max_sequence
# input_string = "1 22 333 4444 55555 666666"
# max_sequence = find_max_digit_sequence(input_string)
# print("Наибольшая последовательность цифр в строке:", max_sequence)

# Задания 11-14
# №2
# def average_ascii_weight(char):
    # Функция, которая возвращает средний вес ASCII-кода символа
    # return sum(ord(c) for c in char) / len(char)

# def sort_string_by_ascii_weight(input_string):
    # Сортируем символы строки по среднему весу ASCII-кода
    # sorted_string = sorted(input_string, key=average_ascii_weight)
    # return ''.join(sorted_string)
# input_string = "abcABC123"
# sorted_string = sort_string_by_ascii_weight(input_string)
# print("Строка в порядке увеличения среднего веса ASCII-кода символа:", sorted_string)

# Задания 15-19
# №5
# def is_global_minimum(arr, index):
    # Проверяем, является ли элемент по указанному индексу глобальным минимумом
    # if arr[index] == min(arr):
    #     return True
    # else:
    #     return False

# Пример использования
# arr = [3, 5, 2, 8, 1, 6]
# index = 4
# if is_global_minimum(arr, index):
#     print(f"Элемент по индексу {index} является глобальным минимумом.")
# else:
#     print(f"Элемент по индексу {index} не является глобальным минимумом.")

# № 17
# def swap_min_max(arr):
    # Находим индексы минимального и максимального элементов массива
    # min_index = arr.index(min(arr))
    # max_index = arr.index(max(arr))
    # Меняем местами минимальный и максимальный элементы
    # arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

# Пример использования
# array = [3, 7, 2, 8, 1, 6]
# print("Исходный массив:", array)
# swap_min_max(array)
# print("Массив после замены минимального и максимального элементов:", array)

# № 29
# def is_max_in_interval(arr, a, b):
    # Находим максимальный элемент массива
    # max_element = max(arr)
    # Проверяем, находится ли максимальный элемент в интервале a..b
    # if a <= max_element <= b:
    #     return True
    # else:
    #     return False

# Пример использования
# array = [3, 7, 12, 8, 10, 6]
# a = 5
# b = 15
# if is_max_in_interval(array, a, b):
#     print(f"Максимальный элемент массива находится в интервале от {a} до {b}.")
# else:
#     print(f"Максимальный элемент массива не находится в интервале от {a} до {b}.")

# № 41
# def average_abs(arr):
    # Если массив пуст, возвращаем 0
    # if not arr:
    #     return 0

    # Вычисляем сумму модулей элементов массива
    # abs_sum = sum(abs(num) for num in arr)
    # Находим среднее арифметическое модулей элементов массива
    # avg_abs = abs_sum / len(arr)
    # return avg_abs


# Пример использования
# array = [3, -7, 12, -8, 10, -6]
# avg_abs = average_abs(array)
# print("Среднее арифметическое модулей элементов массива:", avg_abs)

# № 53
def filter_list(arr):
    # Находим среднее арифметическое и максимальное значение списка
    avg = sum(arr) / len(arr)
    max_val = max(arr)

    # Строим новый список с элементами, большими, чем среднее арифметическое, и меньшими, чем максимальное значение
    new_list = [x for x in arr if x > avg and x < max_val]
    return new_list

input_list = [3, 7, 12, 8, 10, 6]
new_list = filter_list(input_list)
print("Новый список:", new_list)

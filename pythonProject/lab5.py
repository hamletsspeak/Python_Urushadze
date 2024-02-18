import re

def is_valid_url(url):
    """
    Проверяет, является ли строка валидным URL.
    """
    # Регулярное выражение для проверки URL
    url_regex = re.compile(
        r'^(?:http|ftp)s?://' # схема
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # доменное имя...
        r'localhost|' # или localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...или IP
        r'(?::\d+)?' # необязательный порт
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_regex, url) is not None

def get_url_or_raise_exception(url):
    """
    Возвращает URL или выбрасывает исключение, если строка не является валидным URL.
    """
    if is_valid_url(url):
        return url
    else:
        raise ValueError("Строка не является валидным URL")

# Пример использования
input_url = input("Введите URL: ")

try:
    valid_url = get_url_or_raise_exception(input_url)
    print("Введенная строка является валидным URL:", valid_url)
except ValueError as e:
    print("Ошибка:", e)

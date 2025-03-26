import sys

def read_from_file(input_file: str) -> list:
    """Зчитує файл і повертає список рядків."""
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Помилка: файл {input_file} не знайдено.")
        return []


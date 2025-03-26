import sys
from textFiltration import read_from_file, filter_lines, write_to_file  # Заменил функции на правильные

def main():
    """Основна функція: читає вхідний файл, фільтрує рядки та записує результат."""
    if len(sys.argv) < 3:
        print("Використання: python run.py input.txt keyword")
        return

    input_file = sys.argv[1]
    keyword = sys.argv[2]
    output_file = "filtered.txt"

    # Используем правильные функции
    lines = read_from_file(input_file)  # Чтение из файла
    filtered = filter_lines(lines, keyword)  # Фильтрация строк
    write_to_file(output_file, filtered)  # Запись в файл

if __name__ == "__main__":
    main()

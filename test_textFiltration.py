import pytest
from textFiltration import read_from_file, filter_lines, write_to_file  # Здесь замените your_module на имя своего файла

# Фікстура для тестування
@pytest.fixture
def sample_data():
    return [
        "Hello World\n",
        "Python is awesome\n",
        "Filtering is fun\n",
        "Hello Python\n"
    ]

# Тест для filter_lines
def test_filter_lines(sample_data):
    keyword = "Python"
    filtered = filter_lines(sample_data, keyword)
    assert filtered == [
        "Python is awesome\n",
        "Hello Python\n"
    ]

# Тест для write_to_file
def test_write_to_file(tmp_path, sample_data):
    output_file = tmp_path / "test.txt"  # tmp_path автоматически создаёт временные файлы и директории
    write_to_file(str(output_file), sample_data)  # записываем данные
    with open(str(output_file), "r") as f:
        lines = f.readlines()  # читаем из файла
    assert lines == sample_data  # проверяем, что данные, записанные в файл, совпадают с sample_data

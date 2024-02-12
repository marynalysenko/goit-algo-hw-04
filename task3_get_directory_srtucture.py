from pathlib import Path
from colorama import Fore


def directory_structure(folder_path, tab=0):
    """
    Виводить структуру директорії, використовуючи вкладеність для піддиректорій та кольорове форматування.

    Використовує модуль `pathlib` для ітерації по елементах директорії та `colorama` для кольорового форматування виводу.
    Папки відображаються синім кольором, файли - зеленим.

    Параметри:
    - folder_path (str): Шлях до директорії, структуру якої потрібно відобразити.
    - tab (int): Величина відступу для вкладених елементів директорії. За замовчуванням дорівнює 0.
                 З кожною новою вкладеною директорією відступ збільшується.

    Повертає:
    Нічого не повертає. Результатом є вивід в стандартний потік виводу.
    """
    path = Path(folder_path)
    if path.is_dir():
        directory = path.iterdir()
        for item in directory:
            if item.is_dir():
                print(f"{' '*tab}{Fore.LIGHTBLUE_EX}{item.name}{Fore.RESET}")
                directory_structure(item, tab + 4)
            elif item.is_file():
                print(f"{' '*tab}{Fore.GREEN}{item.name}{Fore.RESET}")


# Виклик функції для демонстрації структури директорії
directory_structure("/Users/marinalysenko/Projects/goit_ds_22_hw")
def get_cats_info(path: str):
    """
    Читає файл та повертає список словників з інформацією про котів.

    Параметри:
    - path (str): Шлях до текстового файлу, який містить дані про котів. Кожен рядок має містити
                  унікальний ідентифікатор кота, його ім'я та вік, розділені комою.

    Функція повертає список словників, де кожен словник містить інформацію про одного кота,
    з ключами "id", "name", "age".

    Виключення:
    - FileNotFoundError: якщо вказаний файл не знайдено.
    - Exception: для будь-яких інших помилок, пов'язаних із читанням файлу або неправильним форматом даних.

    Повертає:
    - Список словників з інформацією про котів або None, якщо сталася помилка.
    """
    try:
        with open(path, "r", encoding="UTF-8") as list_cats:
            outlist = []
            for line in list_cats:
                parts = line.strip().split(",")  # Поділ рядка на частини
                outlist.append({"id": parts[0], "name": parts[1], "age": parts[2].strip()})
    except FileNotFoundError:
        print(f"File {path} not found.")
        return None        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return outlist  # Повернення списку словників з інформацією про котів

# Шлях до файлу з даними про котів
path_to_file = '/Users/marinalysenko/Projects/goit_ds_22_hw/goit-algo-hw-04/cats.txt'
cats_info = get_cats_info(path_to_file)
print(cats_info)


def total_salary(file: str) -> None:
    """
    Обчислює загальну та середню заробітну плату розробників на основі даних із текстового файлу.

    Параметри:
    - file (str): Шлях до текстового файлу, який містить інформацію про заробітні плати розробників.
                  Кожен рядок у файлі має містити прізвище розробника та його заробітну плату, розділені комою.

    Функція читає файл, обчислює загальну суму заробітних плат і кількість розробників,
    і виводить загальну та середню заробітну плату. У випадку помилок при відкритті файлу
    або якщо файл має неправильний формат, виводиться відповідне повідомлення.

    Повертає:
    None. Результати виводяться на екран.
    """
        
    total_salary = 0
    num_developers = 0
    try:
        with open(file, "r", encoding = "UTF-8") as list_salary:
            for line in list_salary:
                parts = line.split(",")
                if len(parts)==2:                    
                    salary = int(parts[1].strip()) 
                    total_salary += salary
                    num_developers += 1
    except FileNotFoundError:
        print(f"file  {file} not found.")
        return None
    if num_developers == 0:
        print("The file is in the wrong format or is empty.")
        return None
    average_salary = int(total_salary / num_developers)
    print (f"Загальна сума заробітної плати: {total_salary}\nСередня заробітна плата розробників: {average_salary}")

path_to_file = '/Users/marinalysenko/Projects/goit_ds_22_hw/goit-algo-hw-04/salary.txt'
total_salary(path_to_file)

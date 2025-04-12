def get_terms_for_table():
    """
    Получает список терминов для отображения в таблице.
    Возвращает список, где каждый элемент — это список с информацией о термине.
    """
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.strip().split(";")
            terms.append([cnt, term, definition])  # Добавляем номер, термин и определение
            cnt += 1
    return terms


def write_term(new_term, new_definition):
    """
    Записывает новый термин и его определение в файл.
    Сортирует термины по алфавиту после добавления нового термина.
    """
    new_term_line = f"{new_term};{new_definition};user"  # Добавляем информацию о том, кто добавил термин
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]  # Заголовок файла
        old_terms = existing_terms[1:]  # Существующие термины
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()  # Сортируем термины
    new_terms = [title] + terms_sorted
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))


def get_terms_stats():
    """
    Получает статистику по терминам.
    Возвращает словарь со статистикой: общее количество терминов,
    количество пользовательских терминов и средняя длина определений.
    """
    db_terms = 0
    user_terms = 0
    defin_len = []
    
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            term, defin, added_by = line.strip().split(";")
            words = defin.split()  # Разделяем определение на слова
            defin_len.append(len(words))  # Сохраняем длину определения
            
            # Увеличиваем счетчики в зависимости от источника термина
            if "user" in added_by:
                user_terms += 1
            elif "db" in added_by:
                db_terms += 1

    # Формируем статистику
    stats = {
        "terms_all": db_terms + user_terms,  # Общее количество терминов
        "terms_own": db_terms,                # Количество терминов из базы данных
        "terms_added": user_terms,            # Количество пользовательских терминов
        "words_avg": sum(defin_len) / len(defin_len) if defin_len else 0,  # Средняя длина определений
        "words_max": max(defin_len) if defin_len else 0,  # Максимальная длина определения
        "words_min": min(defin_len) if defin_len else 0   # Минимальная длина определения
    }
    
    return stats

# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: BugNotebook
def test_bugnotebook_extended():
    from bugnotebook import BugNotebook
    nb = BugNotebook()

    # --- базовые тесты ошибок ---
    assert nb.add_bug("Заголовок", "Шаг 1", "Шаг 2", "Шаг 3", "Критический", "Открыт")
    assert nb.add_bug("Другой", "1", "2", "3", "Высокий", "В работе")
    assert nb.add_bug("Третий", "A", "B", "C", "Средний", "Проверен")

    # --- пограничные случаи ---
    assert nb.add_bug("", "1", "2", "3", "Низкий", "Закрыт")
    assert nb.add_bug("Заголовок", "", "", "", "Критический", "Открыт")
    assert nb.add_bug("Заголовок", "1", "2", "3", "Срочный", "Открыт")

    # --- проверка статусов ---
    nb.add_bug("Тест статусов", "1", "2", "3", "Высокий", "Открыт")
    nb.add_bug("Тест статусов", "1", "2", "3", "Высокий", "В работе")
    nb.add_bug("Тест статусов", "1", "2", "3", "Высокий", "Проверен")
    nb.add_bug("Тест статусов", "1", "2", "3", "Высокий", "Закрыт")

    assert nb.get_bugs_by_status("Открыт") == 2
    assert nb.get_bugs_by_status("В работе") == 1
    assert nb.get_bugs_by_status("Закрыт") == 2
    assert nb.get_bugs_by_status("В работе") == 1

    # --- приоритеты ---
    assert nb.get_bugs_by_priority("Критический") == 1
    assert nb.get_bugs_by_priority("Высокий") == 2
    assert nb.get_bugs_by_priority("Низкий") == 1
    assert nb.get_bugs_by_priority("Срочный") == 1

    # --- поиск по шагам ---
    assert nb.search_bugs("Шаг") == 4
    assert nb.search_bugs("Заголовок") == 1
    assert nb.search_bugs("Не существует") == 0

    # --- сортировка ---
    sorted_bugs = nb.get_sorted_bugs()
    assert len(sorted_bugs) == 6
    assert sorted_bugs[0].status == "Открыт"

    # --- удаление ---
    nb.delete_bug(1)
    assert len(nb.bugs) == 5
    assert nb.get_bug(1) is None

    print("Все расширенные тесты пройдены успешно!")

if __name__ == "__main__":
    test_bugnotebook_extended()

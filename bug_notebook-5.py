# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: BugNotebook
def delete_bug_record(record_id: int) -> bool:
    """Удаление записи по ID с проверкой существования."""
    if record_id not in bug_records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    deleted = bug_records.pop(record_id, None)
    if deleted is not None:
        print(f"Успешно удалена запись #{deleted['id']}: {deleted['title']}")
        return True
    else:
        print(f"Ошибка: удаление записи с ID {record_id} не удалось.")
        return False

def get_bug_record_by_id(record_id: int) -> dict | None:
    """Получение записи по ID, возвращает None если запись отсутствует."""
    return bug_records.get(record_id, None)

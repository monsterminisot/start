# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: BugNotebook
import json, os

def save_bugs_to_file(bug_list: list[dict], file_path: str = "bugnotebook.json") -> None:
    """Сохраняет список багов в JSON-файл с проверкой целостности данных."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(bug_list, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {file_path}")
    except (IOError, TypeError) as e:
        print(f"Ошибка сохранения данных: {e}")

def load_bugs_from_file(file_path: str = "bugnotebook.json") -> list[dict]:
    """Загружает список багов из JSON-файла или возвращает пустой список при ошибке."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            print("Формат файла не соответствует списку багов")
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка чтения файла {file_path}: {e}")
        return []

# Пример использования в конце программы
if __name__ == "__main__":
    # Имитация данных для теста сохранения
    test_bugs = [
        {"id": 1, "title": "Ошибка входа", "status": "open"},
        {"id": 2, "title": "Сбой отчета", "status": "fixed"}
    ]
    save_bugs_to_file(test_bugs)
    loaded_bugs = load_bugs_from_file()
    print(f"Загружено багов: {len(loaded_bugs)}")

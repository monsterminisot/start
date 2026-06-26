# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: BugNotebook
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [BugNotebook.from_dict(item) for item in data]
        elif isinstance(data, dict):
            return [BugNotebook.from_dict(data)]
        else:
            print("Ошибка формата JSON")
            return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []

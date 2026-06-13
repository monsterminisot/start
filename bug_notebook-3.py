# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: BugNotebook
class BugNotebook:
    def __init__(self):
        self._bugs = []
    
    def add_bug(self, title: str, steps_to_reproduce: list[str], priority: int, status: str = "open") -> dict:
        bug_id = len(self._bugs) + 1
        record = {
            "id": bug_id,
            "title": title,
            "steps": steps_to_reproduce,
            "priority": priority,
            "status": status,
            "created_at": self._get_timestamp()
        }
        self._bugs.append(record)
        return record
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

# Пример использования:
if __name__ == "__main__":
    notebook = BugNotebook()
    bug1 = notebook.add_bug(
        title="Ошибка при загрузке страницы",
        steps=["Открыть браузер", "Ввести URL", "Нажать Enter"],
        priority=2,
        status="open"
    )
    print(f"Добавлена ошибка #{bug1['id']}")

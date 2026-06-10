# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: BugNotebook
import json
from datetime import datetime

class BugNotebook:
    def __init__(self):
        self.bugs = []
        self._save_file = "bugnotebook.json"

    def add_bug(self, title, steps, status="open", priority=3):
        bug = {
            "id": len(self.bugs) + 1,
            "title": title,
            "steps": steps,
            "status": status,
            "priority": priority,
            "created_at": datetime.now().isoformat()
        }
        self.bugs.append(bug)
        self._save_to_file()
        return bug

    def _save_to_file(self):
        try:
            with open(self._save_file, 'w', encoding='utf-8') as f:
                json.dump(self.bugs, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

    def list_bugs(self):
        return self.bugs

if __name__ == "__main__":
    app = BugNotebook()
    app.add_bug("Ошибка входа в систему", ["1. Открыть браузер", "2. Ввести URL", "3. Нажать Enter"], status="open", priority=1)
    print(f"Добавлено {len(app.list_bugs())} ошибок.")

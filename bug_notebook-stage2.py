# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: BugNotebook
class BugNotebook:
    def __init__(self):
        self.bugs = []
    
    def add_bug(self, title, steps, status="open", priority=3, check=None):
        if not title or len(title.strip()) < 2:
            raise ValueError("Заголовок ошибки должен быть непустым и содержать минимум 2 символа.")
        if not steps or len(steps.strip()) < 10:
            raise ValueError("Шаги воспроизведения должны содержать описание длиной не менее 10 символов.")
        valid_statuses = {"open", "in_progress", "fixed", "closed"}
        if status.lower() not in valid_statuses:
            raise ValueError(f"Неверный статус. Допустимые значения: {', '.join(valid_statuses)}")
        priority = int(priority)
        if not (1 <= priority <= 5):
            raise ValueError("Приоритет должен быть числом от 1 до 5.")
        check_func = None
        if check is not None and callable(check):
            check_func = check
        bug_entry = {
            "id": len(self.bugs) + 1,
            "title": title.strip(),
            "steps": steps.strip().split('\n'),
            "status": status.lower(),
            "priority": priority,
            "check": check_func
        }
        self.bugs.append(bug_entry)
        return bug_entry

# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: BugNotebook
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив объектов ошибок")
        
        bugs = []
        for item in data:
            required_keys = {"id", "title", "steps_to_reproduce", "status", "priority"}
            missing = required_keys - set(item.keys())
            if missing:
                print(f"Предупреждение: пропущен объект с ID {item.get('id', 'unknown')}, не хватает полей: {missing}")
                continue
            
            bug_id = item["id"]
            
            # Валидация статусов и приоритетов
            valid_statuses = {"open", "in_progress", "fixed", "closed"}
            if item["status"].lower() not in valid_statuses:
                print(f"Ошибка статуса для ID {bug_id}: '{item['status']}' -> установлено 'open'")
                item["status"] = "open"
            
            priority_map = {"critical": 1, "high": 2, "medium": 3, "low": 4}
            if item["priority"].lower() not in priority_map:
                print(f"Ошибка приоритета для ID {bug_id}: '{item['priority']}' -> установлено 'medium'")
                item["priority"] = "medium"
            
            # Обработка шагов воспроизведения (разбиваем строку на список)
            steps_text = item.get("steps_to_reproduce", "")
            if isinstance(steps_text, str):
                step_lines = [s.strip() for s in steps_text.splitlines() if s.strip()]
                item["steps"] = [{"step": i+1, "action": line} for i, line in enumerate(step_lines)]
            else:
                print(f"Ошибка формата шагов для ID {bug_id}: ожидается строка")
            
            # Проверки (placeholder)
            checks = []
            if item.get("checks"):
                checks = [{"check": c["name"], "passed": bool(c.get("result", True))} for c in item["checks"]]
            
            bug_entry = {
                "id": int(bug_id),
                "title": str(item["title"]),
                "steps_to_reproduce": steps_text,
                "status": item["status"],
                "priority": item["priority"],
                "created_at": item.get("created_at", ""),
                "checks": checks or []
            }
            
            bugs.append(bug_entry)
        
        return sorted(bugs, key=lambda x: x["id"])

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных: {e}")
        return []

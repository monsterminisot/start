# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: BugNotebook
def summarize_bug(bug):
    """Выводит одну запись в компактном формате: id, статус, приоритет + шаги + проверка."""
    bug_id = str(bug["id"]) if "id" in bug else ""
    status = bug.get("status", "?")
    priority = bug.get("priority", "?")
    steps = bug.get("steps", [])
    verification = bug.get("verification", "")

    lines = [f"[{bug_id}] {status:<10}  [{priority}]"]
    for i, step in enumerate(steps, 1):
        if isinstance(step, dict):
            action = step.get("action", "N/A")
            result = step.get("result", "")
            lines.append(f"   Шаг {i}: {action} -> {result}")
        else:
            lines.append(f"   Шаг {i}: {step}")

    if verification:
        lines.append(f"   Проверка: {verification}")

    return "\n".join(lines)


# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample = {
        "id": 42,
        "status": "resolved",
        "priority": "high",
        "steps": [
            {"action": "Запустить сервер на порту 8080", "result": "OK"},
            {"action": "Отправить GET /api/items", "result": "500 Internal Server Error"},
        ],
        "verification": "После исправления ответ: 200 OK с JSON-массивом.",
    }
    print(summarize_bug(sample))

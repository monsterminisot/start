# === Stage 32: Добавь журнал действий пользователя ===
# Project: BugNotebook
import json
from datetime import datetime, timezone

def log_user_action(action_type: str, details: dict) -> dict:
    """Записывает действие пользователя в файл actions.json."""
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action_type": action_type,
        "details": details,
    }
    try:
        with open("actions.json", "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    if not isinstance(history, list):
        history = []
    history.append(entry)
    with open("actions.json", "w") as f:
        json.dump(history, f, indent=2)
    return entry

def load_action_history() -> list[dict]:
    """Загружает историю действий из файла."""
    try:
        with open("actions.json", "r") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        raise ValueError("Некорректный формат файла действий.")
    except FileNotFoundError:
        return []

def filter_actions(action_type: str | None = None, start_from: str | None = None) -> list[dict]:
    """Фильтрует историю по типу действия и/или дате."""
    history = load_action_history()
    if action_type is not None:
        history = [a for a in history if a["action_type"] == action_type]
    if start_from is not None:
        from datetime import datetime as dt
        cutoff = dt.fromisoformat(start_from)
        history = [a for a in history if dt.fromisoformat(a["timestamp"]) >= cutoff]
    return history

def clear_action_history() -> int:
    """Удаляет всю историю действий, возвращая количество удалённых записей."""
    count = len(load_action_history())
    with open("actions.json", "w") as f:
        json.dump([], f)
    return count

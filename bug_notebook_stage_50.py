# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: BugNotebook
def finalize_bug_notebook():
    """Финальная полировка: аккуратные сообщения, названия и комментарии."""
    BUG_STATUSES = {
        "NEW": "Новая ошибка",
        "CONFIRMED": "Подтверждено",
        "IN_PROGRESS": "В работе",
        "FIXED": "Исправлено",
        "CLOSED": "Закрыто",
    }
    BUG_PRIORITIES = {
        "CRITICAL": "Критическая",
        "HIGH": "Высокая",
        "MEDIUM": "Средняя",
        "LOW": "Низкая",
    }
    BUG_TYPES = {
        "MEMORY_LEAK": "Утечка памяти",
        "NULL_POINTER": "Null-ссылка",
        "LOGIC_ERROR": "Логическая ошибка",
        "INTERFACE": "Проблема интерфейса",
        "PERFORMANCE": "Проблема производительности",
        "SECURITY": "Безопасность",
    }
    BUG_SEVERITY = {
        "CRITICAL": "Высокий",
        "HIGH": "Средний",
        "MEDIUM": "Низкий",
        "LOW": "Минимальный",
    }
    BUG_STATUS_ORDER = ["NEW", "CONFIRMED", "IN_PROGRESS", "FIXED", "CLOSED"]
    BUG_PRIORITY_ORDER = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]

    return BUG_STATUSES, BUG_PRIORITIES, BUG_TYPES, BUG_SEVERITY, BUG_STATUS_ORDER, BUG_PRIORITY_ORDER

# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: BugNotebook
def check_overdue_reminders():
    """Проверяет просроченные напоминания для задач с дедлайном."""
    overdue = []
    for bug in bugs:
        if hasattr(bug, 'deadline') and bug.deadline:
            from datetime import datetime
            if datetime.now() > bug.deadline:
                overdue.append({
                    'id': bug.id,
                    'title': getattr(bug, 'title', 'Unknown'),
                    'deadline': str(bug.deadline),
                    'status': getattr(bug, 'status', 'unknown')
                })
    if overdue:
        print("⚠️ Просроченные напоминания:")
        for item in overdue:
            print(f"  - #{item['id']}: {item['title']} (дедлайн: {item['deadline']}, статус: {item['status']})")
    else:
        print("✅ Все напоминания актуальны.")

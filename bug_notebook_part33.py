# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: BugNotebook
def undo_last_action():
    """Откат последнего действия: возвращает журнал в состояние до последнего добавления."""
    if not bug_log or len(bug_log) == 0:
        print("Нет действий для отката.")
        return
    last = bug_log[-1]
    del bug_log[-1]
    # Восстанавливаем историю изменений (если она ведётся)
    if change_history and len(change_history) > 0:
        prev = change_history[-1].copy()
        del change_history[-1]
        for key, val in prev.items():
            current_state[key] = val
    print(f"Отменено действие: {last.get('title', 'неизвестно')}.")

# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: BugNotebook
def generate_summary(bugs):
    if not bugs:
        print("Журнал пуст.")
        return
    
    total = len(bugs)
    statuses = {}
    priorities = {}
    
    for bug in bugs:
        status = bug['status']
        priority = bug['priority']
        statuses[status] = statuses.get(status, 0) + 1
        priorities[priority] = priorities.get(priority, 0) + 1
    
    print(f"Всего ошибок: {total}")
    print("Статусы:")
    for status, count in sorted(statuses.items()):
        print(f"  - {status}: {count}")
    
    print("Приоритеты:")
    for priority, count in sorted(priorities.items(), key=lambda x: {'high': 3, 'medium': 2, 'low': 1}.get(x[0], 0), reverse=True):
        print(f"  - {priority}: {count}")

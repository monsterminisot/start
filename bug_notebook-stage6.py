# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: BugNotebook
def filter_bugs(status=None, category=None, tags=None):
    filtered = []
    for bug in bugs:
        if status and bug['status'] != status: continue
        if category and bug.get('category') != category: continue
        if tags:
            bug_tags = bug.get('tags', [])
            if not any(tag in bug_tags for tag in tags): continue
        filtered.append(bug)
    return filtered

def print_filtered_bugs(filter_func, title="Фильтр"):
    results = filter_func()
    if not results:
        print(f"{title}: Записей не найдено.")
        return
    print(f"\n{title} ({len(results)} записей):")
    for i, bug in enumerate(results, 1):
        tags_str = ", ".join(bug.get('tags', [])) if bug.get('tags') else "Нет"
        print(f"{i}. [{bug['status']}] {bug['category']} | Приоритет: {bug['priority']} | Теги: {tags_str}")
        print(f"   Ошибка: {bug['description']}\n")

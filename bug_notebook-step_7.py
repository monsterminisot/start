# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: BugNotebook
def sort_bugs(bug_list, key='date'):
    """Сортировка списка багов по дате (по умолчанию), приоритету или названию."""
    if not bug_list:
        return []
    
    # Определяем ключ сортировки и направление
    reverse = False
    if key == 'priority':
        reverse = True  # Высокий приоритет первыми
        def sort_key(bug):
            priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
            return priority_map.get(bug['status'].get('priority', 'low'), 4)
    elif key == 'name':
        reverse = False
        def sort_key(bug):
            return bug['title']
    else: # date (default)
        reverse = False
        def sort_key(bug):
            try:
                return datetime.fromisoformat(bug['created_at'].replace('Z', '+00:00'))
            except ValueError:
                return datetime.min
    
    return sorted(bug_list, key=sort_key, reverse=reverse)

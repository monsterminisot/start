# === Stage 20: Добавь восстановление записей из архива ===
# Project: BugNotebook
def load_from_archive(file_path):
    """Восстанавливает записи из архивного файла, если он существует."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    bugs = []
    current = {}
    for line in lines:
        key, val = line.split('=', 1)
        if key == '_':
            if current.get('_id'):
                bugs.append(current)
            current = {}
        else:
            current[key] = val
    if current.get('_id'):
        bugs.append(current)
    return bugs


def save_to_archive(bugs, file_path):
    """Сохраняет список записей в архивный файл."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for bug in bugs:
            f.write('_'.join(f'{k}={v}' for k, v in sorted(bug.items())) + '\n')

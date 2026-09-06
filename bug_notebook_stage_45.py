# === Stage 45: Добавь восстановление из резервной копии ===
# Project: BugNotebook
import pickle, os

def restore_backup(backup_path):
    if not os.path.exists(backup_path):
        print(f"Файл резервной копии не найден: {backup_path}")
        return False
    try:
        with open(backup_path, 'rb') as f:
            data = pickle.load(f)
        if isinstance(data, dict) and 'bugs' in data:
            bugbook.bugs = data['bugs']
            print(f"Восстановлено {len(bugbook.bugs)} записей из {backup_path}")
            return True
        print("Некорректный формат резервной копии")
        return False
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False

backup_path = 'bugbook_backup.dat'
if restore_backup(backup_path):
    input("Нажмите Enter, чтобы продолжить...")

# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: BugNotebook
import shutil, os, datetime, json

def backup_data_file(data_path, backup_dir="backups"):
    if not os.path.exists(data_path):
        return None
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"data_backup_{timestamp}.json")
    shutil.copy2(data_path, backup_path)
    return backup_path

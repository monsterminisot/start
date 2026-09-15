# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: BugNotebook
class AuditLog:
    def __init__(self):
        self.entries = []

    def log(self, action, entity, details, user=None):
        entry = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'action': action,
            'entity': entity,
            'details': details,
            'user': user
        }
        self.entries.append(entry)
        return entry

    def get_log(self):
        return list(self.entries)

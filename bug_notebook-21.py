# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: BugNotebook
class Reminder:
    def __init__(self, title, date, priority="low"):
        self.title = title
        self.date = date
        self.priority = priority
        self.done = False
        
    def is_overdue(self):
        if not self.done and self.date < datetime.now().date():
            return True
        return False
    
    def __repr__(self):
        status = "✅" if self.done else ("🔴" if self.is_overdue() else "⏳")
        return f"{status} [{self.priority}] {self.title} (до: {self.date})"

def manage_reminders(reminders_list):
    today = datetime.now().date()
    overdue = [r for r in reminders_list if r.is_overdue()]
    
    print("\n📋 Напоминания:")
    for i, r in enumerate(reminders_list, 1):
        print(f"  {i}. {r}")
    
    if overdue:
        print(f"\n⚠️  Просрочено ({len(overdue)}):")
        for r in overdue:
            print(f"   - {r.title} (было: {r.date})")

# Пример использования
reminders = [
    Reminder("Сделать домашку", datetime.now().date() + timedelta(days=2)),
    Reminder("Купить молоко", datetime.now().date()),  # уже просрочено!
]
manage_reminders(reminders)

# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: BugNotebook
def demo():
    print("=== BugNotebook Demo ===")
    for i in range(1, 4):
        bug = {"id": f"BUG-{i:03d}", "title": f"Error {i} - Sample Issue", "status": "Open", "priority": 2, "steps": ["Step 1", "Step 2"], "checks": True}
        BugNotebook.add_bug(bug)
    print(f"Added {len(BugNotebook.bugs)} bugs")
    for bug in BugNotebook.bugs:
        print(f"{bug['id']}: {bug['title']} [{bug['status']}] Priority={bug['priority']}")

demo()

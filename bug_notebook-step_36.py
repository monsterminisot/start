# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: BugNotebook
def check_data_integrity():
    """Проверяет целостность записей журнала: статусы, приоритеты, шаги и проверки."""
    valid_statuses = {"CONFIRMED", "PENDING", "INVALIDATED", "FIXED", "WONTFIX", "DUPLICATE"}
    valid_priorities = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
    issues = db.get_issues()
    errors = []
    for issue in issues:
        if issue["status"] not in valid_statuses:
            errors.append(f"Недопустимый статус в issue {issue['id']}: {issue['status']}")
        if issue["priority"] not in valid_priorities:
            errors.append(f"Недопустимый приоритет в issue {issue['id']}: {issue['priority']}")
        if not issue["steps_reproduce"]:
            errors.append(f"Отсутствуют шаги воспроизведения в issue {issue['id']}")
        if issue["title"] and not issue["title"].strip():
            errors.append(f"Пустой заголовок в issue {issue['id']}")
    if errors:
        print("⚠️  Обнаружены нарушения целостности:")
        for e in errors:
            print(f"  - {e}")
        return False
    print("✅ Проверка целостности пройдена.")
    return True


def repair_simple_issues():
    """Автоматический ремонт простых проблем: очистка пустых заголовков, нормализация статусов."""
    repaired = 0
    issues = db.get_issues()
    for issue in issues:
        if not issue.get("title"):
            issue["title"] = f"[Issue #{issue['id']}] Не описан"
            repaired += 1
        if issue["status"] not in valid_statuses:
            issue["status"] = "PENDING"
            repaired += 1
    if repaired:
        print(f"🔧 Исправлено {repaired} записей.")
        db.save_all_issues(issues)
    return repaired

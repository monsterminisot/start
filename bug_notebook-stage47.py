# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: BugNotebook
def demo():
    print("=" * 60)
    print("BugNotebook — Демо: добавление и просмотр багов")
    print("=" * 60)
    print()
    
    # Создаём менеджер
    manager = BugManager()
    
    # 1-й баг: критичный
    b1 = BugNote(
        title="Crash при нажатии кнопки X",
        steps=["Открыть приложение", "Нажать кнопку X", "Наблюдать краш"],
        status="New",
        priority="Critical",
    )
    manager.add_bug(b1)
    
    # 2-й баг: средний
    b2 = BugNote(
        title="Текст обрезается в поле ввода",
        steps=["Ввести текст > 100 символов", "Наблюдать обрезку"],
        status="Reproducing",
        priority="Medium",
    )
    manager.add_bug(b2)
    
    # 3-й баг: низкий
    b3 = BugNote(
        title="Незакрытый алерт после отмены",
        steps=["Нажать 'Отмена' в диалоге", "Обратить внимание на алерт"],
        status="Verified",
        priority="Low",
    )
    manager.add_bug(b3)
    
    # Просмотр всех багов
    print("\n--- Журнал багов ---")
    for bug in manager.bugs:
        print(f"  [{bug.priority}] {bug.title} — Статус: {bug.status}")
    
    # Фильтрация по статусу
    new_bugs = manager.get_bugs_by_status("New")
    print(f"\n--- Новые баги: {len(new_bugs)} ---")
    for bug in new_bugs:
        print(f"  • {bug.title}")
    
    # Обновление статуса
    b1.status = "In Progress"
    print(f"\nОбновлён статус бага: {b1.title} → {b1.status}")
    
    # Итоговая статистика
    print(f"\n--- Статистика ---")
    print(f"  Всего: {manager.count()}")
    print(f"  Критичные: {manager.count_critical()}")
    print(f"  В работе: {manager.count_in_progress()}")
    print(f"  Разрешено: {manager.count_verified()}")
    
    print("\nДемо завершено. Спасибо за использование BugNotebook!")

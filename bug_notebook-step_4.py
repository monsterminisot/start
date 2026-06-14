# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: BugNotebook
def edit_bug_notebook_entry(entry_id: int, **kwargs) -> dict | None:
    if entry_id not in bug_notes:
        return {"success": False, "error": f"Запись с ID {entry_id} не найдена."}
    
    existing = bug_notes[entry_id]
    fields_to_update = ["status", "priority", "steps_to_reproduce", "verification_status"]
    for field in fields_to_update:
        if field in kwargs and kwargs[field]:
            setattr(existing, field, kwargs[field])
            
    return {"success": True, "message": f"Запись {entry_id} обновлена.", "data": dict(existing)}

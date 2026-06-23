# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: BugNotebook
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "exported_at": datetime.now().isoformat(),
        "bugs": [
            {
                "id": bug["id"],
                "title": bug["title"],
                "status": bug["status"],
                "priority": bug["priority"],
                "steps_to_reproduce": bug.get("steps_to_reproduce", []),
                "verification_steps": bug.get("verification_steps", [])
            }
            for bug in _bugs_list
        ],
        "summary": {
            "total_count": len(_bugs_list),
            "open_count": sum(1 for b in _bugs_list if b["status"] == "OPEN"),
            "closed_count": sum(1 for b in _bugs_list if b["status"] == "CLOSED")
        }
    }
    return json.dumps(data, indent=2, ensure_ascii=False)

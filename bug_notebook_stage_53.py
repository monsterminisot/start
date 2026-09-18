# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: BugNotebook
import re

def parse_bug_log(text):
    records = []
    pattern = re.compile(
        r"ID:\s*(\d+)\s*\n"
        r"Title:\s*(.*?)\n"
        r"Steps:\s*(.*?)\n"
        r"Status:\s*(.*?)\n"
        r"Priority:\s*(.*?)\n",
        re.DOTALL
    )
    matches = pattern.findall(text)
    for m in matches:
        records.append({
            "id": int(m[0]),
            "title": m[1].strip(),
            "steps": m[2].strip(),
            "status": m[3].strip(),
            "priority": m[4].strip(),
        })
    return records

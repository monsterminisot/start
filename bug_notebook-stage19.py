# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: BugNotebook
def archive_notes(archive_path="notes_archive.txt"):
    """Archive completed or old notes to a separate file."""
    archived = []
    with open("bug_notebook.py", "r") as f:
        content = f.read()
    
    for match in re.finditer(r'\[STATUS\]:(COMPLETED|FIXED)\s+\[(\d+)\]\s+(.+?)\s*\n', content, re.DOTALL):
        status = match.group(1)
        note_id = int(match.group(2))
        note_text = match.group(3).strip()
        archived.append(f"[ARCHIVED] [{note_id}] {status}: {note_text}")
    
    if archived:
        with open(archive_path, "w") as f:
            for entry in archived:
                f.write(entry + "\n")
        print(f"Archived {len(archived)} notes to {archive_path}")

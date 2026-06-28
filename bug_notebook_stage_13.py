# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: BugNotebook
class BugNotebook:
    def __init__(self):
        self._bugs = []

    def add_bug(self, title, steps, status="open", priority=3, check=None):
        bug_id = len(self._bugs) + 1
        self._bugs.append({
            "id": bug_id,
            "title": title.lower(),
            "steps": steps,
            "status": status.lower(),
            "priority": int(priority),
            "check": check or ""
        })

    def search(self, query=None, fields=["title", "steps"], case_insensitive=True):
        if not self._bugs:
            return []
        
        results = []
        for bug in self._bugs:
            match = False
            text_to_search = (bug["title"] + " " + bug["steps"]).lower() if case_insensitive else (bug["title"] + " " + bug["steps"])
            
            if query is None or query.lower() == "" or query.lower() in text_to_search:
                match = True
            
            for field in fields:
                if field in bug and query is not None:
                    search_text = bug[field].lower() if case_insensitive else bug[field]
                    if query.lower() in search_text:
                        match = True
                        break
            
            if match:
                results.append(bug)
        
        return sorted(results, key=lambda x: x["priority"])

    def get_bug(self, id):
        for bug in self._bugs:
            if bug["id"] == id:
                return bug
        return None

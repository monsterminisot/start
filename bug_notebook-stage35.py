# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: BugNotebook
def suggest_next_action(bugs):
    """Recommend next step based on current bug journal state."""
    if not bugs:
        return "No bugs found — all clear!"
    
    open_bugs = [b for b in bugs if b['status'] == 'open']
    critical_bugs = [b for b in open_bugs if b.get('priority', 3) <= 2]
    no_steps = [b for b in open_bugs if not b.get('steps', [])]
    
    if critical_bugs:
        return f"🔴 Fix {len(critical_bugs)} critical bug(s) first. Most urgent."
    elif no_steps:
        return "⚠️  Reproduce steps missing for some bugs — add them before testing fixes."
    else:
        sorted_bugs = sorted(open_bugs, key=lambda b: (b.get('priority', 3), -len(b.get('steps', []))))
        top_bug = sorted_bugs[0]
        return f"🟡 Next: Investigate bug #{top_bug['id']} ({top_bug['title']}). Priority {top_bug['priority']}."

# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: BugNotebook
import datetime

def export_bug_report(bugs):
    """Export a compact text report of all bugs sorted by priority."""
    if not bugs:
        return "BugNotebook Report — no bugs recorded."
    
    lines = ["BugNotebook Report — Generated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    lines.append("=" * 60)
    lines.append(f"Total bugs: {len(bugs)}")
    lines.append("")
    
    sorted_bugs = sorted(bugs, key=lambda b: b["priority"])
    for i, bug in enumerate(sorted_bugs, 1):
        lines.append(f"[{i}] ID: {bug['id']}")
        lines.append(f"    Title: {bug['title']}")
        lines.append(f"    Priority: {bug['priority']}")
        lines.append(f"    Status: {bug['status']}")
        lines.append(f"    Steps: {'; '.join(bug['steps'])}")
        lines.append(f"    Verification: {bug.get('verification', 'Not verified')}")
        lines.append("")
    
    lines.append("=" * 60)
    return "\n".join(lines)

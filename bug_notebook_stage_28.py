# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: BugNotebook
def compute_metrics():
    metrics = {}
    if not bugs: return metrics
    total = len(bugs)
    open_count = sum(1 for b in bugs if b.status == "open")
    closed_count = sum(1 for b in bugs if b.status in ("closed", "fixed"))
    high_priority = sum(1 for b in bugs if b.priority == 2)
    avg_steps = sum(len(b.steps) for b in bugs) / total if total else 0
    avg_severity = sum(b.severity for b in bugs) / total if total else 0
    closed_ratio = (closed_count / total * 100) if total else 0
    metrics["total_bugs"] = total
    metrics["open_bugs"] = open_count
    metrics["closed_bugs"] = closed_count
    metrics["high_priority"] = high_priority
    metrics["avg_steps_to_reproduce"] = round(avg_steps, 1)
    metrics["avg_severity"] = round(avg_severity, 2)
    metrics["resolution_ratio_pct"] = round(closed_ratio, 1)
    return metrics

print(compute_metrics())

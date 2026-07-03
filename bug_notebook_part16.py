# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: BugNotebook
def calculate_monthly_stats(bugs):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'open': 0, 'closed': 0, 'high_priority': 0})
    for bug in bugs:
        date_key = f"{bug['date'][:7]}"
        status = bug.get('status', 'open')
        priority = bug.get('priority', 'medium')
        stats[date_key]['total'] += 1
        if status == 'open':
            stats[date_key]['open'] += 1
        else:
            stats[date_key]['closed'] += 1
        if priority in ('high', 'critical'):
            stats[date_key]['high_priority'] += 1
    return dict(sorted(stats.items()))

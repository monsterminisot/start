# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: BugNotebook
def calculate_weekly_stats(bugs):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'open': 0, 'closed': 0})
    for bug in bugs:
        date_str = bug.get('created_at', '').split('-')[0] + '-' + bug.get('created_at', '').split('-')[1]
        week_start = (int(date_str[:4]) - 1) * 7 if int(date_str[:2]) <= 5 else int(date_str[:4]) * 7
        key = f"{week_start}-01"
        stats[key]['total'] += 1
        if bug.get('status') == 'open':
            stats[key]['open'] += 1
        elif bug.get('status') == 'closed':
            stats[key]['closed'] += 1
    return dict(sorted(stats.items()))

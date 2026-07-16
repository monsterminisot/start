# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: BugNotebook
def print_bug_table(bugs):
    if not bugs:
        print("Список пуст.")
        return
    col_w = [len(f) for f in ("BugID", "Status", "Priority", "Steps", "Repro?")]
    header = " | ".join(f"{f:<{col_w[i]}}" for i, f in enumerate(col_w))
    print(header)
    print("-" * len(header))
    for b in bugs:
        steps_trunc = (b["steps"][: col_w[3] - 3] + "...") if len(b["steps"]) > col_w[3] - 3 else b["steps"]
        repro_tag = "✅" if b.get("repro_verified", False) else "❌"
        row = f"{b['bug_id']:<{col_w[0]}} | {b['status']:<{col_w[1]}} | {b['priority']:<{col_w[2]}} | {steps_trunc:<{col_w[3]}} | {repro_tag}"
        print(row)

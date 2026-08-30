# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: BugNotebook
def main():
    import argparse
    parser = argparse.ArgumentParser(description="BugNotebook CLI")
    parser.add_argument("action", choices=["add", "list", "search", "status", "export"], help="Операция")
    parser.add_argument("--file", help="Путь к файлу журнала")
    parser.add_argument("--id", help="ID бага")
    parser.add_argument("--title", help="Заголовок бага")
    parser.add_argument("--status", choices=["open", "in_progress", "fixed", "closed"])
    parser.add_argument("--priority", choices=["low", "medium", "high", "critical"])
    parser.add_argument("--output", help="Файл для экспорта")
    args = parser.parse_args()
    if args.action == "add":
        _add_bug(args)
    elif args.action == "list":
        _list_bugs(args)
    elif args.action == "search":
        _search_bugs(args)
    elif args.action == "status":
        _show_status(args)
    elif args.action == "export":
        _export(args)

def _add_bug(args):
    from bug_notebook import BugNotebook
    nb = BugNotebook(args.file)
    bug = nb.add_bug(args.title, steps=args.steps, status=args.status or "open", priority=args.priority or "medium")
    print(f"Добавлен баг {bug.id}")

def _list_bugs(args):
    from bug_notebook import BugNotebook
    nb = BugNotebook(args.file)
    for bug in nb.list_bugs():
        print(f"[{bug.id}] {bug.title} [{bug.status}] [{bug.priority}]")

def _search_bugs(args):
    from bug_notebook import BugNotebook
    nb = BugNotebook(args.file)
    results = nb.search_bugs(args.query)
    for bug in results:
        print(f"[{bug.id}] {bug.title}")

def _show_status(args):
    from bug_notebook import BugNotebook
    nb = BugNotebook(args.file)
    nb.show_status()

def _export(args):
    from bug_notebook import BugNotebook
    nb = BugNotebook(args.file)
    nb.export(args.output)

if __name__ == "__main__":
    main()

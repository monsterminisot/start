# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: BugNotebook
def show_menu():
    print("\n--- BugNotebook Menu ---")
    print("1. Add new bug report")
    print("2. List all bugs")
    print("3. Filter bugs by status")
    print("4. Exit")
    try:
        choice = input("Select option (1-4): ").strip()
        return int(choice) if choice.isdigit() else None
    except ValueError:
        return None

def handle_add_bug():
    title = input("Bug Title: ")
    steps = input("Steps to Reproduce:\n")
    status = input("Status (Open/Closed/Fixed): ").strip().capitalize() or "Open"
    priority = input("Priority (Low/Medium/High): ").strip().capitalize() or "Medium"
    checks = input("Verification Steps: ") if input("Add verification steps? (y/n): ").lower() == 'y' else ""
    print(f"[+] Bug '{title}' added with status {status}.\n")

def handle_list_bugs():
    bugs = get_all_bugs()
    if not bugs:
        print("- No bugs recorded yet.")
    else:
        for i, bug in enumerate(bugs, 1):
            print(f"{i}. [{bug['status']}] {bug['title']} (Priority: {bug['priority']})")

def handle_filter_bugs():
    status = input("Filter by Status (Open/Closed/Fixed): ").strip().capitalize() or "All"
    bugs = get_all_bugs()
    filtered = [b for b in bugs if status == 'All' or b.get('status', '').lower() == status.lower()]
    print(f"\n--- Bugs with status '{status}' ---")
    if not filtered:
        print("- No matching bugs found.")
    else:
        for i, bug in enumerate(filtered, 1):
            print(f"{i}. {bug['title']} ({bug['priority']})")

def main_cli():
    while True:
        opt = show_menu()
        if opt == 1: handle_add_bug()
        elif opt == 2: handle_list_bugs()
        elif opt == 3: handle_filter_bugs()
        elif opt == 4: print("Exiting BugNotebook."); break
        else: print("Invalid option, please try again.")

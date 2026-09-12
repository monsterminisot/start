# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: BugNotebook
def self_check():
    print("=== BugNotebook Self-Check ===")
    checks = [
        ("BugEntry", lambda: BugEntry is not None),
        ("BugStatus", lambda: BugStatus is not None),
        ("BugPriority", lambda: BugPriority is not None),
        ("BugVerification", lambda: BugVerification is not None),
        ("BugNotebook", lambda: BugNotebook is not None),
    ]
    for name, check in checks:
        print(f"  {name}: {'OK' if check() else 'FAIL'}")

    try:
        e = BugEntry(title="test", description="test", steps="step1", status="open", priority=1, verification="none")
        print(f"  BugEntry creation: OK, id={e.id}")
    except Exception as exc:
        print(f"  BugEntry creation: FAIL - {exc}")

    try:
        nb = BugNotebook()
        nb.add(e)
        nb.save("bugnotebook_test.txt")
        print(f"  BugNotebook save: OK, file size={os.path.getsize('bugnotebook_test.txt')}")
        nb.load("bugnotebook_test.txt")
        print(f"  BugNotebook load: OK, count={len(nb.entries)}")
        os.remove("bugnotebook_test.txt")
    except Exception as exc:
        print(f"  BugNotebook save/load: FAIL - {exc}")

    print("=== Self-Check complete ===")

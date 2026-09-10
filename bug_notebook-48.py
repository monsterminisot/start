# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: BugNotebook
def _split_lines(text: str) -> list[str]:
    return text.splitlines()


def _join_lines(lines: list[str]) -> str:
    return "\n".join(lines)

# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: BugNotebook
def parse_date(date_str):
    """Парсит дату в формате 'ГГГГ-ММ-ДД', возвращает datetime или None."""
    try:
        from datetime import datetime
        return datetime.strptime(date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        return None

def show_error(message=""):
    """Выводит ошибку красным цветом в консоль."""
    print(f"\033[91мОшибка: {message}\033[0м", flush=True)

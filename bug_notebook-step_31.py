# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: BugNotebook
def switch_profile():
    if not current_user:
        print("Сначала авторизуйтесь")
        return
    new = input(f"Текущий профиль: {current_user}\nВведите новый логин: ")
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    if new not in users or users[new]['password'] != current_user['password']:
        print("Ошибка профиля")
        return
    current_user = users[new]
    print(f"Переключено на {current_user}")

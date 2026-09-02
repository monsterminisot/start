# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: BugNotebook
class BugNotebook:
    def __init__(self):
        self.ansi_enabled = True

    def _set_ansi(self, enabled):
        self.ansi_enabled = enabled

    @property
    def _colors(self):
        if not self.ansi_enabled:
            return ''
        return {
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'cyan': '\033[36m',
            'bold': '\033[1m',
            'reset': '\033[0m',
        }

    def _reset(self):
        return self._colors['reset']

    def _colorize(self, text, color):
        if not self.ansi_enabled:
            return text
        return f'{self._colors[color]}{text}{self._reset()}'

    def log_bug(self, title, description, steps, status, priority):
        title_c = self._colorize(title, 'bold')
        status_c = self._colorize(status, 'red' if status == 'Critical' else
                           'yellow' if status == 'High' else
                           'green' if status == 'Low' else 'blue')
        priority_c = self._colorize(f'[{priority}]', 'cyan')
        print(f'{title_c}\n{self._colorize("─" * len(title_c), "blue")}\n')
        print(f'{self._colorize("Описание:", "bold")} {description}')
        print(f'{self._colorize("Шаги воспроизведения:", "bold")}\n')
        for i, step in enumerate(steps, 1):
            print(f'  {i}. {step}')
        print(f'{self._colorize("Статус:", "bold")} {status_c}')
        print(f'{self._colorize("Приоритет:", "bold")} {priority_c}')
        print()

    def log_fix(self, bug_title, solution):
        print(f'{self._colorize("Решение найдено!", "green", "bold")}')
        print(f'  {bug_title}: {solution}')
        print()

    def log_error(self, message):
        print(f'{self._colorize("ОШИБКА:", "red", "bold")} {message}')
        print()

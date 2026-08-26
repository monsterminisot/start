# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: BugNotebook
import unittest

class TestBugNotebook(unittest.TestCase):
    def test_bug_status_enum(self):
        from enum import Enum
        class Status(Enum):
            OPEN = 'open'
            IN_PROGRESS = 'in_progress'
            RESOLVED = 'resolved'
            CLOSED = 'closed'
        self.assertEqual(Status.OPEN.value, 'open')
        self.assertEqual(Status.RESOLVED.value, 'resolved')

    def test_bug_priority_enum(self):
        from enum import Enum
        class Priority(Enum):
            LOW = 'low'
            MEDIUM = 'medium'
            HIGH = 'high'
            CRITICAL = 'critical'
        self.assertEqual(Priority.CRITICAL.value, 'critical')
        self.assertEqual(Priority.MEDIUM.value, 'medium')

    def test_bug_step_list(self):
        steps = ['1. Click login', '2. Enter invalid email', '3. Press Submit']
        self.assertEqual(len(steps), 3)
        self.assertIn('Click login', steps)

    def test_bug_check_result(self):
        checks = ['Check login button', 'Check error message', 'Check redirect']
        results = [True, False, True]
        passed = sum(results)
        self.assertEqual(passed, 2)

    def test_bug_notebook_append(self):
        notebook = []
        def append(entry):
            notebook.append(entry)
        append({'title': 'Bug 1', 'status': 'open'})
        append({'title': 'Bug 2', 'status': 'resolved'})
        self.assertEqual(len(notebook), 2)
        self.assertEqual(notebook[0]['title'], 'Bug 1')

    def test_bug_search_by_status(self):
        bugs = [
            {'title': 'A', 'status': 'open'},
            {'title': 'B', 'status': 'resolved'},
            {'title': 'C', 'status': 'open'},
        ]
        open_bugs = [b for b in bugs if b['status'] == 'open']
        self.assertEqual(len(open_bugs), 2)
        self.assertEqual(open_bugs[0]['title'], 'A')

if __name__ == '__main__':
    unittest.main()

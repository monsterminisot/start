# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: BugNotebook
class BugTemplate:
    """Simple template system for quick bug entry creation."""

    def __init__(self, name="", description="", severity="medium", status="open"):
        self.name = name
        self.description = description
        self.severity = severity
        self.status = status

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            severity=data.get("severity", "medium"),
            status=data.get("status", "open"),
        )


TEMPLATES = [
    BugTemplate(name="UI Glitch", description="Visual issue in UI", severity="low", status="open"),
    BugTemplate(name="Crash on Start", description="App crashes immediately after launch", severity="critical", status="open"),
    BugTemplate(name="Data Loss", description="User data is lost during operation", severity="high", status="open"),
]


def get_template_by_name(name):
    for t in TEMPLATES:
        if name.lower() in t.name.lower():
            return t
    return None


def apply_template(template, title=None, steps=None, expected_result=None, actual_result=None, check=None):
    bug = {
        "title": title or template.name,
        "description": f"[Template: {template.name}] - {template.description}",
        "severity": template.severity,
        "status": template.status,
        "steps": steps if isinstance(steps, list) else [steps] if steps else [],
        "expected_result": expected_result or "",
        "actual_result": actual_result or "",
        "check": check if isinstance(check, str) else {"method": "manual", "result": ""},
    }
    return bug


def add_from_template(name=None, **kwargs):
    template = get_template_by_name(name) if name else TEMPLATES[0]
    return apply_template(template, **kwargs)

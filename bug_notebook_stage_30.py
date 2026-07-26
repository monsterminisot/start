# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: BugNotebook
class UserProfile:
    def __init__(self, name, role="viewer", theme="light"):
        self.name = name
        self.role = role  # viewer, editor, admin
        self.theme = theme  # light, dark
        self.notes = []

class ProfileManager:
    _profiles = {}

    @classmethod
    def register(cls, profile):
        cls._profiles[profile.name] = profile

    @classmethod
    def get(cls, name):
        return cls._profiles.get(name)

    @classmethod
    def list_profiles(cls):
        return list(cls._profiles.values())

    @classmethod
    def current_profile(cls):
        return cls._profiles.get("default") or None

# Pre-register default profile if not already set
if "default" not in ProfileManager._profiles:
    ProfileManager.register(UserProfile("default", "viewer", "light"))

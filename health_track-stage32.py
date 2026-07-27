# === Stage 32: Добавь журнал действий пользователя ===
# Project: HealthTrack
class ActionLog:
    def __init__(self):
        self.entries = []

    def add(self, action, description="", timestamp=None):
        if timestamp is None:
            import datetime as dt
            timestamp = dt.datetime.now().isoformat()
        entry = {"action": action, "description": description, "timestamp": timestamp}
        self.entries.append(entry)
        return entry

    def get_recent(self, n=5):
        return list(reversed(self.entries[-n:])) if len(self.entries) >= n else list(reversed(self.entries))

    @property
    def count(self):
        return len(self.entries)

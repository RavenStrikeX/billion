# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: HealthTrack
class HealthTrack:
    def __init__(self):
        self.records = []
        self.habits = {}
        self.notes = {}
    
    def add_measurement(self, date, metric_name, value):
        record = {
            "date": date,
            "metric": metric_name,
            "value": float(value) if isinstance(value, str) else value
        }
        self.records.append(record)
        return record
    
    def set_habit(self, habit_name, status="active"):
        self.habits[habit_name] = {"status": status, "count": 0}
    
    def log_note(self, date, content):
        if date not in self.notes:
            self.notes[date] = []
        self.notes[date].append(content)

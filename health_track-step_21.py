# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: HealthTrack
import json
from datetime import date, timedelta

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, text, due_date_str):
        try:
            due_date = date.fromisoformat(due_date_str)
        except ValueError:
            print("Неверный формат даты. Используйте YYYY-MM-DD.")
            return None
        reminder = {
            "text": text,
            "due_date": due_date.isoformat(),
            "done": False
        }
        self.reminders.append(reminder)
        print(f"Напоминание добавлено: '{text}' на {due_date_str}")
        return reminder

    def show_reminders(self):
        if not self.reminders:
            print("Нет напоминаний.")
            return
        today = date.today().isoformat()
        for r in self.reminders:
            status = "✅ Выполнено" if r["done"] else (
                "⚠️ Пропущено" if r["due_date"] < today else f"📅 Через {r['due_date']}")
            print(f"  • [{status}] {r['text']} — {r['due_date']}")

    def mark_done(self, index):
        if 0 <= index < len(self.reminders) and not self.reminders[index]["done"]:
            self.reminders[index]["done"] = True
            print(f"Напоминание #{index + 1} помечено как выполненное.")
        else:
            print("Ошибка: напоминание не найдено или уже выполнено.")

    def save_reminders(self, filename="reminders.json"):
        with open(filename, "w") as f:
            json.dump(self.reminders, f, indent=2)
        print(f"Напоминания сохранены в {filename}")

    def load_reminders(self, filename="reminders.json"):
        try:
            with open(filename, "r") as f:
                self.reminders = json.load(f)
            print("Напоминания загружены.")
        except FileNotFoundError:
            print("Файл напоминаний не найден. Начну с нуля.")

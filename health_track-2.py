# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: HealthTrack
class HealthData:
    def __init__(self):
        self.records = []

    def add_record(self, date, weight=None, mood=None, habit=None, note=None):
        if not isinstance(date, str) or len(date) < 10:
            raise ValueError("Некорректная дата. Используйте формат 'YYYY-MM-DD'.")
        if weight is not None and (not isinstance(weight, (int, float)) or weight <= 0):
            raise ValueError("Вес должен быть положительным числом.")
        if mood is not None and not isinstance(mood, str) or len(mood.strip()) < 1:
            raise ValueError("Настроение должно быть непустой строкой.")
        if habit is not None and not isinstance(habit, bool):
            raise ValueError("Привычка должна быть булевым значением (True/False).")
        if note is not None and not isinstance(note, str) or len(note.strip()) > 500:
            raise ValueError("Заметка должна быть строкой длиной до 500 символов.")

        record = {
            "date": date,
            "weight": weight,
            "mood": mood,
            "habit": habit,
            "note": note
        }
        self.records.append(record)
        return record

    def get_weekly_report(self):
        if not self.records:
            return "Нет данных для отчёта."
        today = datetime.date.today()
        week_start = today - timedelta(days=7)
        week_records = [r for r in self.records if week_start <= datetime.strptime(r["date"], "%Y-%m-%d").date() <= today]
        avg_weight = sum(float(r["weight"]) for r in week_records if r.get("weight")) / max(1, len([r for r in week_records if r.get("weight")]))
        avg_mood_score = sum(len(r["mood"].strip()) for r in week_records if r.get("mood")) / max(1, len([r for r in week_records if r.get("mood")]))
        habit_count = len([r for r in week_records if r.get("habit")])
        return f"Средний вес: {avg_weight:.2f} кг. Средняя длина записи о настроении: {avg_mood_score:.1f} символов. Выполнено привычек: {habit_count}/{len(week_records)}."

import datetime
from datetime import timedelta

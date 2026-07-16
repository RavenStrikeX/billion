# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: HealthTrack
def print_record(record):
    """Компактный вывод одной записи."""
    if not record:
        return "Нет записей."
    
    entry = record.get("entry", {})
    metrics = entry.get("metrics", [])
    notes = entry.get("notes", "")
    tags = entry.get("tags", [])
    
    date_str = entry.get("date", "без даты")
    mood = entry.get("mood", 3)
    mood_emoji = {"1": "😞", "2": "😐", "3": "🙂", "4": "😊", "5": "🤩"}[str(mood)] if str(mood) in mood_emoji else "🙂"
    
    print(f"[{date_str}] {mood_emoji} Настроение: {mood}/5")
    
    if metrics:
        metric_strs = []
        for m in metrics:
            name, value = m.get("name", "?"), m.get("value", "")
            unit = m.get("unit", "")
            metric_strs.append(f"{name}: {value}{unit}" if unit else f"{name}: {value}")
        print(f"  Показатели: {'; '.join(metric_strs)}")
    
    if notes.strip():
        print(f"  Заметки: {notes[:80]}{'...' if len(notes) > 80 else ''}")
    
    if tags:
        tag_str = ", ".join(tags)
        print(f"  Теги: {tag_str}")

# Пример использования (разкомментируй для проверки):
if __name__ == "__main__":
    sample = {
        "entry": {
            "date": "2024-03-15",
            "mood": 4,
            "metrics": [
                {"name": "шаги", "value": 8500, "unit": ""},
                {"name": "сон", "value": 7.5, "unit": "ч"},
                {"name": "вес", "value": 72.3, "unit": "кг"}
            ],
            "notes": "Сегодня тренировка была отличной! Съел кашу на завтрак.",
            "tags": ["спорт", "каша"]
        }
    }
    print_record(sample)

# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: HealthTrack
TEMPLATES = {
    "morning_check": "Morning Check\n---\nВремя: 07:00\nНастроение:\nСон (ч): {}\nУровень энергии: {}\nЗаметка:",
    "daily_habits": "Daily Habits Log\n---\nДата: {}\nПривычки:\n[ ] Пить воду\n[ ] Двигаться\n[ ] Читать\n[ ] Медитировать\n[ ] Ужинать вовремя\nЗаметка:",
}

def get_template(name):
    return TEMPLATES.get(name)

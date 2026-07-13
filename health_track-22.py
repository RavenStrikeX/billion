# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: HealthTrack
def check_overdue_reminders(reminders):
    """Проверяет напоминания, которые были просрочены (пропущены к выполнению)."""
    overdue = []
    today = datetime.date.today()
    for reminder in reminders:
        if not reminder["done"]:
            due_date = datetime.date.fromisoformat(reminder.get("due", today.isoformat()))
            if due_date <= today:
                overdue.append({**reminder, "overdue_days": (today - due_date).days})
    return overdue

# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: HealthTrack
def _format_weekly_report(week_data):
    """Форматирует недельный отчёт из данных за неделю."""
    lines = []
    lines.append(f"=== Отчёт за неделю ===")
    for day, value in week_data.items():
        lines.append(f"  {day}: {value}")
    lines.append("======================")
    return "\n".join(lines)

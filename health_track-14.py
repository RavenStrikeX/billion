# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: HealthTrack
def generate_weekly_summary(data):
    if not data.get('entries'):
        return "Нет данных для отчёта."
    
    entries = data['entries']
    metrics = ['heart_rate', 'steps', 'sleep_hours', 'water_ml']
    habits = data.get('habits', [])
    notes = data.get('notes', [])
    
    report_lines = ["=== Недельный отчёт HealthTrack ==="]
    
    # Статистика по метрикам
    for metric in metrics:
        if metric in entries[0]:
            values = [e[metric] for e in entries if metric in e and e[metric] is not None]
            if values:
                avg_val = sum(values) / len(values)
                report_lines.append(f"{metric.replace('_', ' ').title()}: {avg_val:.1f} (среднее)")
    
    # Статистика по привычкам
    habit_counts = {}
    for h in habits:
        name = h.get('name', 'unknown')
        count = sum(1 for e in entries if e.get(name))
        if count > 0:
            habit_counts[name] = count
    
    if habit_counts:
        report_lines.append("Привычки:")
        for name, count in sorted(habit_counts.items(), key=lambda x: -x[1]):
            pct = (count / len(entries)) * 100
            report_lines.append(f"  {name}: {count} раз ({pct:.0f}%)")
    
    # Краткие заметки
    if notes and len(notes) > 0:
        recent_notes = [n for n in notes[-3:] if n.get('content')]
        if recent_notes:
            report_lines.append("Заметки:")
            for note in recent_notes:
                report_lines.append(f"  - {note['content']}")
    
    return "\n".join(report_lines)

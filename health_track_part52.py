# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: HealthTrack
def export_text_report(self):
    lines = []
    lines.append("=== HealthTrack Weekly Report ===")
    lines.append(f"Date: {self.date.strftime('%Y-%m-%d')}")
    lines.append("")
    for metric in self.metrics:
        lines.append(f"Metric: {metric.name}")
        lines.append(f"  Value: {metric.value}")
        lines.append(f"  Target: {metric.target}")
        lines.append(f"  Status: {'On Track' if metric.value >= metric.target else 'Below Target'}")
        lines.append("")
    for habit in self.habits:
        lines.append(f"Habit: {habit.name}")
        lines.append(f"  Streak: {habit.streak} days")
        lines.append(f"  Completion Rate: {habit.completion_rate:.1f}%")
        lines.append("")
    if self.notes:
        lines.append("Notes:")
        for note in self.notes:
            lines.append(f"  - {note}")
        lines.append("")
    lines.append("---")
    return "\n".join(lines)

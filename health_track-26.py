# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: HealthTrack
def demo_commands():
    """Демо-команды для быстрого ручного тестирования HealthTrack."""
    print("=== Демо: показатели ===")
    show_health_metrics()
    
    print("\n=== Демо: привычки ===")
    show_habits_list()
    
    print("\n=== Демо: заметки ===")
    show_notes_list()
    
    print("\n=== Демо: недельный отчёт ===")
    show_weekly_report()

if __name__ == "__main__":
    demo_commands()

# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: HealthTrack
def demo():
    print("=" * 50)
    print("HealthTrack — Демо сценарий")
    print("=" * 50)

    # Создаём объекты
    user = User("Алексей")
    print(f"\nСоздан пользователь: {user}")

    # Добавляем показатели
    blood_pressure = BloodPressure(120, 80)
    weight = Weight(75.5)
    temperature = Temperature(36.6)
    mood = Mood("Отлично")
    energy = Energy(8)
    sleep_quality = SleepQuality(7)
    water_intake = WaterIntake(2000)
    steps = Steps(8000)

    print(f"  Показатели: {blood_pressure}, {weight}, {temperature}, {mood}, {energy}, {sleep_quality}, {water_intake}, {steps}")

    # Добавляем привычки
    habits = [
        Habit("Утренняя зарядка", "Спорт"),
        Habit("Пить воду", "Здоровье"),
        Habit("Чтение", "Развитие"),
    ]
    print(f"  Привычки: {habits}")

    # Добавляем заметки
    notes = [
        Note("Начать неделю с планом"),
        Note("Купить витамины"),
    ]
    print(f"  Заметки: {notes}")

    # Записываем дневной журнал
    journal = DailyJournal("2024-01-15", user, blood_pressure, weight, temperature, mood, energy, sleep_quality, water_intake, steps, habits, notes)
    print(f"  Дневной журнал за 2024-01-15 создан: {journal.date}")

    # Генерируем недельный отчёт
    weekly_report = WeeklyReport(journal)
    print(f"  Недельный отчёт: {weekly_report.summary}")

    print("\nДемо завершено успешно!")
    return weekly_report

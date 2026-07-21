# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: HealthTrack
def reset_demo_data():
    """Сбрасывает все данные в дефолтные значения для демо-режима."""
    global indicators, habits, notes, weekly_reports, current_date
    
    default_indicators = {
        'heart_rate': 72,
        'blood_pressure_systolic': 120,
        'blood_pressure_diastolic': 80,
        'weight': 75.5,
        'sleep_hours': 7.5,
        'water_intake_ml': 2000,
    }
    
    default_habits = {
        'exercise_minutes': 30,
        'meditation_minutes': 15,
        'reading_minutes': 20,
        'screen_time_hours': 4,
        'social_interactions': 5,
    }
    
    default_notes = [
        "Добро пожаловать в HealthTrack! Заполните профиль и начните отслеживать показатели.",
        "Помните: регулярность важнее интенсивности.",
        "",
    ]
    
    default_weekly_reports = []
    
    indicators.update(default_indicators)
    habits.update(default_habits)
    notes.clear()
    weekly_reports.clear()
    current_date = datetime.now().date()


def clear_all_data():
    """Полностью очищает все данные приложения."""
    global indicators, habits, notes, weekly_reports, current_date
    
    indicators.clear()
    habits.clear()
    notes.clear()
    weekly_reports.clear()
    current_date = datetime.now().date()
    
    print("Все данные успешно очищены!")


# Пример использования:
if __name__ == "__main__":
    reset_demo_data()
    clear_all_data()

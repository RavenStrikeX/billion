# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: HealthTrack
def get_app_settings():
    return {
        "app_name": "HealthTrack",
        "version": 29,
        "max_readings_per_day": 10,
        "habit_days_to_show_history": 7,
        "report_weeks_back_default": 4,
        "note_max_length": 500,
        "metric_defaults": {
            "weight": {"unit": "kg", "min": 30, "max": 200},
            "height": {"unit": "cm", "fixed": True},
            "temperature": {"unit": "°C", "normal_min": 36.1, "normal_max": 37.2},
            "heart_rate": {"unit": "bpm", "rest_normal_min": 50, "rest_normal_max": 100},
        },
    }

def check_metric_value(metric_name, value):
    defaults = get_app_settings()["metric_defaults"]
    if metric_name in defaults:
        cfg = defaults[metric_name]
        if "min" in cfg and value < cfg["min"]:
            return False
        if "max" in cfg and value > cfg["max"]:
            return False
    return True

def get_weekly_report_period():
    week_count = get_app_settings().get("report_weeks_back_default", 4)
    import datetime
    today = datetime.date.today()
    start = today - datetime.timedelta(weeks=week_count)
    end = today
    return (start, end)

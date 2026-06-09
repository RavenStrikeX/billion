# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: HealthTrack
import json
from datetime import datetime, timedelta

# Инициализация структуры данных приложения
APP_DATA = {
    "user": {
        "name": "Олег",
        "age": 34
    },
    "health_metrics": {
        "weight_history": [],
        "blood_pressure": [],
        "sleep_hours": []
    },
    "habits": {
        "water_intake": 0,
        "exercise_minutes": 0,
        "meditation_minutes": 0
    },
    "notes": [],
    "reports": {}
}

# Функция для безопасного сохранения данных в файл (демонстрация работы с файлами)
def save_data_to_file(filepath="healthtrack_data.json"):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(APP_DATA, f, ensure_ascii=False, indent=2)
        print(f"[INFO] Данные успешно сохранены в {filepath}")
        return True
    except IOError as e:
        print(f"[ERROR] Ошибка сохранения файла: {e}")
        return False

# Функция для загрузки данных из файла (демонстрация работы с файлами)
def load_data_from_file(filepath="healthtrack_data.json"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"[INFO] Данные успешно загружены из {filepath}")
        return data
    except FileNotFoundError:
        print("[INFO] Файл данных не найден. Создаётся новый.")
        return APP_DATA
    except json.JSONDecodeError as e:
        print(f"[ERROR] Ошибка чтения JSON файла: {e}")
        return APP_DATA

# Генератор демонстрационных данных для тестирования
def generate_demo_data():
    today = datetime.now()
    demo_metrics = []
    
    # Создаём историю за последние 7 дней
    for i in range(7):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        demo_metrics.append({
            "date": date,
            "weight": 75.0 + (i * 0.1),
            "blood_pressure": {"systolic": 120 + i, "diastolic": 80 + i},
            "sleep_hours": 7.0 + (i * 0.2)
        })
    
    APP_DATA["health_metrics"]["weight_history"] = demo_metrics
    APP_DATA["health_metrics"]["blood_pressure"] = demo_metrics
    APP_DATA["health_metrics"]["sleep_hours"] = demo_metrics
    
    # Добавляем пару заметок
    APP_DATA["notes"].append({
        "id": 1,
        "text": "Начал вести дневник самочувствия.",
        "date": today.strftime("%Y-%m-%d")
    })
    
    return APP_DATA

# Точка входа: Загрузка или создание данных и сохранение
if __name__ == "__main__":
    print("--- HealthTrack: Инициализация ---")
    
    # Попытка загруз

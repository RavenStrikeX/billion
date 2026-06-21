# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: HealthTrack
import json, os, datetime as dt
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки и валидирует структуру."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_keys = ['measurements', 'habits', 'notes']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле: {key}")
            
            if key == 'measurements':
                # Проверка формата записей измерений (дата, тип, значение)
                for item in data[key]:
                    assert isinstance(item.get('date'), str), "Дата должна быть строкой"
                    assert isinstance(item.get('value'), (int, float)), "Значение должно быть числом"
            
            elif key == 'habits':
                # Проверка формата привычек (название, статус)
                for item in data[key]:
                    assert isinstance(item.get('name'), str), "Название привычки должно быть строкой"
                    assert isinstance(item.get('status'), bool), "Статус должен быть булевым"
            
            elif key == 'notes':
                # Проверка формата заметок (дата, текст)
                for item in data[key]:
                    assert isinstance(item.get('text'), str), "Текст заметки должен быть строкой"

        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON: {e}") from e

# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: HealthTrack
def load_initial_data(json_string):
    import json
    data = json.loads(json_string)
    
    def parse_date(date_str):
        if not date_str: return None
        try:
            parts = date_str.split('-')
            if len(parts) == 3:
                y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
                return (y, m, d)
        except ValueError: pass
        return None

    def parse_value(val):
        try: return float(val) if val else None
        except ValueError: return None

    metrics = []
    habits = {}
    notes = []
    
    for entry in data.get('entries', []):
        date = parse_date(entry.get('date'))
        if not date: continue
        
        metric_entry = {
            'date': date,
            'weight': parse_value(entry.get('weight')),
            'blood_pressure': [parse_value(x) for x in entry.get('bp', ['0/0']).split('/')],
            'mood': int(entry.get('mood', 5)) if entry.get('mood') else None,
            'sleep_hours': parse_value(entry.get('sleep'))
        }
        metrics.append(metric_entry)
        
        habit_status = {h: bool(int(v)) for h, v in (entry.get('habits', {}).items())}
        habits[date] = habit_status
        
        if entry.get('note'):
            notes.append({'date': date, 'text': entry['note']})

    return {'metrics': metrics, 'habits': habits, 'notes': notes}

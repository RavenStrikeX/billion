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

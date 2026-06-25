# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: HealthTrack
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Загружено {len(data)} записей из '{filepath}'")
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{filepath}': {e}")
        return []
    except PermissionError:
        print(f"Нет прав для чтения файла: {filepath}")
        return []

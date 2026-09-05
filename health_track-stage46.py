# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: HealthTrack
def migrate_data():
    """
    Миграция версии структуры данных HealthTrack.
    Проверяет текущую версию и при необходимости обновляет структуру данных.
    """
    current_version = 1  # Текущая версия структуры данных

    # Проверка на наличие данных в старом формате
    if 'data' not in globals() or not isinstance(data, dict):
        print("Ошибка: данные не найдены или не являются словарем")
        return

    # Проверка на наличие ключа 'version'
    if 'version' not in data:
        print("Ошибка: версия не найдена в данных")
        return

    # Обновление структуры данных при необходимости
    if data['version'] < current_version:
        print(f"Обновление структуры данных с версии {data['version']} до {current_version}")
        # Здесь можно добавить логику обновления структуры данных
        data['version'] = current_version
        print("Структура данных обновлена")
    else:
        print("Структура данных актуальна")

    return data['version']

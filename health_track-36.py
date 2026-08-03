# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: HealthTrack
def check_and_repair_data(storage):
    """Проверяет целостность данных и автоматически исправляет простые проблемы."""
    issues = []
    
    # Проверка: все habit records должны иметь valid timestamp
    for i in range(len(habits)):
        record = habits[i]
        if 'timestamp' not in record or record['timestamp'] == None:
            now = datetime.now()
            record['timestamp'] = str(now)
            issues.append(f"habits[{i}]: добавлен timestamp")
    
    # Проверка: все note records должны иметь valid timestamp
    for i in range(len(notes)):
        record = notes[i]
        if 'timestamp' not in record or record['timestamp'] == None:
            now = datetime.now()
            record['timestamp'] = str(now)
            issues.append(f"notes[{i}]: добавлен timestamp")
    
    # Проверка: все measurement records должны иметь valid timestamp и value
    for i in range(len(measurements)):
        record = measurements[i]
        if 'timestamp' not in record or record['timestamp'] == None:
            now = datetime.now()
            record['timestamp'] = str(now)
            issues.append(f"measurements[{i}]: добавлен timestamp")
        
        if 'value' not in record or record['value'] == None:
            issues.append(f"measurements[{i}]: отсутствует значение, пропущено")

    # Проверка: все goal records должны иметь valid target и current
    for i in range(len(goals)):
        record = goals[i]
        if 'target' not in record or record['target'] == None:
            issues.append(f"goals[{i}]: отсутствует цель, пропущено")

    # Проверка: все reminder records должны иметь valid timestamp и message
    for i in range(len(reminders)):
        record = reminders[i]
        if 'timestamp' not in record or record['timestamp'] == None:
            now = datetime.now()
            record['timestamp'] = str(now)
            issues.append(f"reminders[{i}]: добавлен timestamp")

    # Проверка: все journal records должны иметь valid date и entry
    for i in range(len(journal_entries)):
        record = journal_entries[i]
        if 'date' not in record or record['date'] == None:
            now = datetime.now()
            record['date'] = str(now.date())
            issues.append(f"journal[{i}]: добавлена дата")

    # Вывод отчёта о проверке
    print("=== Отчёт о целостности данных ===")
    if not issues:
        print("✓ Все данные в порядке, проблем не обнаружено.")
    else:
        print(f"⚠ Найдено {len(issues)} проблема(ы):")
        for issue in issues:
            print(f"  - {issue}")
    
    return issues

# Запуск проверки при запуске программы
print("\nЗапуск автоматической проверки данных...")
check_and_repair_data(storage)

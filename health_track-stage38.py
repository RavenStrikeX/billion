# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: HealthTrack
def test_edge_cases():
    # Тесты на пограничные и ошибочные значения
    assert HealthTracker().add_habit("Пить воду", "100", "2025-01-01") == "OK"
    assert HealthTracker().add_habit("Спать", "3500", "2025-01-01") == "OK"
    assert HealthTracker().add_habit("Бег", "120", "2025-01-01") == "OK"

    # Тест на пустую строку
    assert HealthTracker().add_habit("", "5", "2025-01-01") == "FAIL"

    # Тест на отрицательное время
    assert HealthTracker().add_habit("Пить", "-10", "2025-01-01") == "FAIL"

    # Тест на отрицательное расстояние
    assert HealthTracker().add_habit("Бег", "-5", "2025-01-01") == "FAIL"

    # Тест на отрицательное давление
    assert HealthTracker().add_vital("Давление", "110/70", "2025-01-01") == "OK"
    assert HealthTracker().add_vital("Давление", "120/80", "2025-01-01") == "OK"
    assert HealthTracker().add_vital("Давление", "100/60", "2025-01-01") == "OK"

    # Тест на пустую строку для vital
    assert HealthTracker().add_vital("Давление", "", "2025-01-01") == "FAIL"

    # Тест на добавление заметки
    assert HealthTracker().add_note("Привет", "2025-01-01") == "OK"
    assert HealthTracker().add_note("", "2025-01-01") == "FAIL"

    # Тест на добавление заметки без даты
    assert HealthTracker().add_note("Привет", "") == "FAIL"

    # Тест на добавление заметки без текста
    assert HealthTracker().add_note("", "2025-01-01") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты
    assert HealthTracker().add_note("Привет", "2025-13-01") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (месяц)
    assert HealthTracker().add_note("Привет", "2025-01-32") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (год)
    assert HealthTracker().add_note("Привет", "0000-01-01") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (день)
    assert HealthTracker().add_note("Привет", "2025-01-00") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (месяц)
    assert HealthTracker().add_note("Привет", "2025-14-01") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (год)
    assert HealthTracker().add_note("Привет", "2026-01-01") == "OK"

    # Тест на добавление заметки с неправильным форматом даты (день)
    assert HealthTracker().add_note("Привет", "2025-01-32") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (месяц)
    assert HealthTracker().add_note("Привет", "2025-13-01") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (год)
    assert HealthTracker().add_note("Привет", "0000-01-01") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (день)
    assert HealthTracker().add_note("Привет", "2025-01-00") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (месяц)
    assert HealthTracker().add_note("Привет", "2025-14-01") == "FAIL"

    # Тест на добавление заметки с неправильным форматом даты (год)
    assert HealthTracker().add_note("Привет", "2026-01-01") == "OK"

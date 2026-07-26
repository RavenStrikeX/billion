# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: HealthTrack
def switch_profile():
    """Переключить активный профиль, если выбран другой."""
    global active_profile
    if not any((active_profile == p for p in profiles)):
        return False
    new = input("Введите имя профиля для переключения: ").strip()
    if new not in profiles:
        print(f"Профиль '{new}' не найден.")
        return False
    active_profile = new
    print(f"Теперь активен профиль: {active_profile}")
    return True

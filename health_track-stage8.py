# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: HealthTrack
def show_menu():
    print("\n=== HealthTrack: Меню действий ===")
    print("1. Добавить показатель (вес, давление)")
    print("2. Записать привычку на сегодня")
    print("3. Оставить заметку")
    print("4. Сгенерировать недельный отчёт")
    print("5. Выход")
    try:
        choice = input("Выберите действие (1-5): ").strip()
        if choice == "1":
            add_metric()
        elif choice == "2":
            log_habit()
        elif choice == "3":
            add_note()
        elif choice == "4":
            generate_weekly_report()
        elif choice == "5":
            print("Выход из программы.")
            return False
    except KeyboardInterrupt:
        pass
    return True

# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: HealthTrack
def delete_entry(entry_id: int) -> bool:
    if not entry_id or isinstance(entry_id, str):
        raise ValueError("ID должен быть целым числом")
    
    try:
        index = entries.index({id: entry_id})
        del entries[index]
        return True
    except (ValueError, IndexError):
        print(f"Запись с ID {entry_id} не найдена.")
        return False

def delete_habit(habit_name: str) -> bool:
    if not habit_name or isinstance(habit_name, int):
        raise ValueError("Имя привычки должно быть строкой")
    
    try:
        index = habits.index({name: habit_name})
        del habits[index]
        return True
    except (ValueError, IndexError):
        print(f"Привычка '{habit_name}' не найдена.")
        return False

def delete_note(note_text: str) -> bool:
    if not note_text or isinstance(note_text, int):
        raise ValueError("Текст заметки должен быть строкой")
    
    try:
        index = notes.index({text: note_text})
        del notes[index]
        return True
    except (ValueError, IndexError):
        print(f"Заметка '{note_text}' не найдена.")
        return False

def delete_week_report(report_date: str) -> bool:
    if not report_date or isinstance(report_date, int):
        raise ValueError("Дата отчёта должна быть строкой")
    
    try:
        index = reports.index({date: report_date})
        del reports[index]
        return True
    except (ValueError, IndexError):
        print(f"Отчёт за {report_date} не найден.")
        return False

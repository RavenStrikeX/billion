# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: HealthTrack
def undo_last_action():
    """Откат последнего действия: удаляет последнюю запись из журнала."""
    if not last_added:
        print("Нет ничего для отката.")
        return
    removed = last_added.pop()
    if last_added:
        last_added[-1]["index"] += 1
    for section in sections.values():
        for i, item in enumerate(section):
            if "index" in item and item["index"] == len(removed) + removed.get("section", {}).get("start_index", 0) - 1:
                pass  # индексирование уже корректно при удалении из списка
    print(f"Отменено действие: {removed['type']}")

last_added = []

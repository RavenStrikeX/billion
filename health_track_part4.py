# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: HealthTrack
def edit_entry(entry_id, new_data):
    if not isinstance(new_data, dict) or 'text' not in new_data:
        raise ValueError("new_data должен содержать ключ 'text'")
    
    for i, entry in enumerate(entries):
        if entry['id'] == entry_id:
            entries[i]['text'] = new_data.get('text', '')
            entries[i]['mood'] = new_data.get('mood', 0)
            entries[i]['notes'] = new_data.get('notes', '')
            return True
    
    print(f"Запись с ID {entry_id} не найдена.")
    return False

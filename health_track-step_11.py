# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: HealthTrack
import json, os

DATA_FILE = "healthtrack_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"entries": [], "habits": {}, "notes": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Ошибка чтения файла данных. Создание нового.")
        return {"entries": [], "habits": {}, "notes": []}

def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Ошибка сохранения данных: {e}")
        return False

def get_entry(id):
    data = load_data()
    for entry in data["entries"]:
        if entry.get("id") == id:
            return entry
    return None

def add_entry(entry):
    data = load_data()
    entry["id"] = len(data["entries"]) + 1
    data["entries"].append(entry)
    save_data(data)
    return entry

def update_habit(habit_name, status):
    data = load_data()
    if habit_name in data["habits"]:
        data["habits"][habit_name]["status"] = status
        save_data(data)
    else:
        data["habits"][habit_name] = {"count": 0, "streak": 0, "status": status}
        save_data(data)

def add_note(note):
    data = load_data()
    note_id = len(data["notes"]) + 1
    data["notes"].append({"id": note_id, "text": note})
    save_data(data)
